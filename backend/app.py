import os
from http import HTTPStatus

from flask import Flask, Response, redirect, request, session
from flask_cors import CORS
from httplib2 import HttpLib2Error
from pydrive2.auth import GoogleAuth, RefreshError
from pydrive2.drive import GoogleDrive

app = Flask(__name__)
app.config.from_prefixed_env()

CORS(
    app,
    supports_credentials=True,
    expose_headers=['auth-url', 'page-token']
)


class AppGoogleAuth(GoogleAuth):
    DEFAULT_SETTINGS = {
        'client_config_backend': 'settings',
        'client_config': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID'),
            'client_secret': os.getenv('GOOGLE_CLIENT_SECRET'),
            'redirect_uri': os.getenv('GOOGLE_REDIRECT_URI'),
        },
        'save_credentials': True,
        'save_credentials_backend': 'dictionary',
        'save_credentials_dict': session,
        'save_credentials_key': 'google_creds',
        'get_refresh_token': True,
    }


def google_drive_api(func):
    def wrapper(*args, **kwargs):
        gauth = AppGoogleAuth()
        gauth.LoadCredentials()

        unauthorized = Response(
            status=HTTPStatus.UNAUTHORIZED,
            headers={'auth-url': gauth.GetAuthUrl()}
        )

        if gauth.credentials is None:
            return unauthorized

        if gauth.access_token_expired:
            try:
                gauth.Refresh()
            except RefreshError:
                return unauthorized

            gauth.SaveCredentials()

            session.modified = True

        try:
            return func(GoogleDrive(gauth), *args, **kwargs)
        except HttpLib2Error as e:
            return str(e), HTTPStatus.BAD_GATEWAY

    wrapper.__name__ = func.__name__

    return wrapper


@app.route('/directories/<directory_id>/file-list')
@google_drive_api
def directories_file_list(drive, directory_id):
    params = {
        'q': f"'{directory_id}' in parents and trashed = false",
        'orderBy': 'folder',
        'maxResults': 100,
    }

    if (order_by := request.args.get('orderBy')):
        params['orderBy'] = ','.join([params['orderBy'], order_by])

    if (page_token := request.headers.get('page-token')):
        params['pageToken'] = page_token

    response = drive.ListFile(params)
    result = response.GetList()

    if response['pageToken']:
        headers = {'page-token': response['pageToken']}
    else:
        headers = {}

    return result, headers


@app.route('/directories/<directory_id>/parents')
@google_drive_api
def directories_parents(drive, directory_id):
    root_directory = {'id': 'root', 'title': 'My Drive'}

    if directory_id == 'root':
        return [root_directory]

    directories = {
        directory['id']: directory
        for directory in drive.ListFile({
            'q': "mimeType='application/vnd.google-apps.folder'",
            'fields': 'items(id,title,parents)',
        }).GetList()
    }

    parent = directories[directory_id]
    parents = [parent]

    while not parent['parents'][0]['isRoot']:
        parent = directories[parent['parents'][0]['id']]
        parents.append(parent)

    return [root_directory] + parents[::-1]


@app.route('/google-auth')
def google_auth():
    gauth = AppGoogleAuth()
    gauth.Auth(request.args['code'])
    gauth.SaveCredentials()

    session.modified = True
    session.permanent = True

    return redirect(os.getenv('APP_URL'))

## Local setup
1. [Create OAuth client ID](https://console.cloud.google.com/apis/credentials)
    - Default Redirect URI: `http://localhost:5000/google-auth`
2. [Enable Google Drive API](https://console.cloud.google.com/apis/api/drive.googleapis.com/metrics)
3. `cp frontend/.env.example frontend/.env`
4. `cp backend/.env.example backend/.env`
5. Set credentials in `/backend/.env`
6. `docker compose up --build`
7. Open `http://localhost:5173/`

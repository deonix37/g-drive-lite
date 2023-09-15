const API_URL = import.meta.env.VITE_API_URL;

export async function apiFetch(path, params, headers) {
    const url = `${API_URL}${path}?` + new URLSearchParams(params);

    const res = await fetch(url, {
        credentials: 'include',
        headers,
    });

    if (!res.ok) {
        if (res.status === 401) {
            window.location.replace(res.headers.get('auth-url'));
        } else {
            alert(await res.text());
        }

        return Promise.reject(res);
    }

    return res;
}

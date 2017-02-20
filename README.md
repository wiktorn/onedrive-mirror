# onedrive-mirror
OneDrive mirroring script

Install:
```
python setup.py install
```

First you need to create an application at Microsoft. Go to [Microsoft Application Registration Portal](https://apps.dev.microsoft.com/?referrer=https%3A%2F%2Fdev.onedrive.com%2Fapp-registration.htm) and register your app.

You will get Client ID and Client Secret for your application. Create session file:
```sh
export ONEDRIVEMIRROR_CLIENTID={your_client_id}
export ONEDRIVEMIRROR_CLIENT_SECRET={your_client_secret}
onedrivemirror init
```

The script will ask you to open an URL in browser. Do it, login to your Microsoft Account and grant your app right to access your OneDrive.

If successful, your browser should be redirected to localhost. Copy everything after code= to the terminal.

The session file will be created as a `.onedrive.session`.

Now you can use:
```
onedrivemirror cp remote_path local_path
```
To copy folders from OneDrive to your local disk. In each folder `.etags.db` file will be created that caches OneDrive etags and is used to only send the files that are different.

import onedrivesdk
import onedrivesdk.request
import os
import shelve


class MirrorClient:
    def __init__(self, session_file):
        self.client = get_client()

        if not os.path.exists(session_file):
            raise ValueError("Session file does not exist")

        self.client.auth_provider.load_session(path=session_file)
        self.client.auth_provider.refresh_token()
        self.client.auth_provider.save_session(path=session_file)

    def mirror(self, onedrive_path, local_path):
        if not os.path.exists(local_path):
            os.mkdir(local_path)

        with shelve.open(os.path.join(local_path, ".etags")) as etags:
            for item in self.client.item(drive='me', path=onedrive_path).children.request().get():
                if item.folder:
                    self.mirror(os.path.join(onedrive_path, item.name), os.path.join(local_path, item.name))
                else:
                    if item.e_tag != etags.get(item.id):
                        self.client.item(drive='me', id=item.id).download(os.path.join(local_path, item.name))
                        etags[item.id] = item.e_tag


def get_client() -> onedrivesdk.request.one_drive_client.OneDriveClient:
    return onedrivesdk.get_consumer_client(
        client_id=os.getenv("ONEDRIVEMIRROR_CLIENTID"),
        scopes=['offline_access', 'onedrive.readonly']
    )


def create_session_file(session_file):
    client = get_client()
    client_secret = os.getenv("ONEDRIVEMIRROR_CLIENT_SECRET")
    redirect_uri = "http://localhost"
    print('Paste this URL into your browser, approve the app\'s access.')
    print(client.auth_provider.get_auth_url(redirect_uri))
    print('Copy everything in the address bar after "code=", and paste it below.')
    code = input('Paste code here: ')
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    client.auth_provider.save_session(path=session_file)

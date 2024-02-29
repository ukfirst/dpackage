from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import pandas as pd
from src.utils import get_project_root
from pathlib import Path
from io import StringIO

def login():
    root = get_project_root()
    google_auth = GoogleAuth(settings_file=str(root) + 'config_files\pydrive_settings.yaml')
    client_json_path = str(root) + '\config_files\client_secrets.json'
    credentials_path = str(root) + '\config_files\credentials.json'
    google_auth.DEFAULT_SETTINGS['client_config_file'] = client_json_path
    google_auth.DEFAULT_SETTINGS['client_secrets.json'] = credentials_path
    if Path(credentials_path).exists() is False:
        google_auth.DEFAULT_SETTINGS['get_refresh_token'] = True
        google_auth.LocalWebserverAuth()
        google_drive = GoogleDrive(google_auth)
        google_auth.SaveCredentialsFile(credentials_path)
    else:
        google_auth.LoadCredentialsFile(credentials_path)
        if google_auth.access_token_expired:
            google_auth.Refresh()
        else:
            google_auth.Authorize()
            google_drive = GoogleDrive(google_auth)
    return google_drive


def read_file(id_file):
    google_drive = login()
    metadata = dict(id=id_file)
    google_file = google_drive.CreateFile(metadata=metadata)
    # Save the content as a string
    content = google_file.GetContentString()
    # Transform the content into a dataframe
    df = pd.read_csv(StringIO(content))
    google_file.Delete()
    return df

#spotify = '1spihvvV_nFnrbqtw7LPpVbR6iKLgDfnN'
spotify = '1IyUGxeqg5kEQseu1Eiko2I_CLvyvY2Y7'

df = read_file(spotify)
print(df)
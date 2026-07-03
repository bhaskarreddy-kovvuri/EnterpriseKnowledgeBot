import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

class GmailAuthenticator:
    TOKEN_FILE = "auth/token.json"
    CREDENTIALS = "credentials.json"

    def authenticate(self):
        creds = None
        if os.path.exists(self.TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(
                self.TOKEN_FILE,
                SCOPES
            )

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CREDENTIALS,
                    SCOPES
                )
                creds = flow.run_local_server(port=0)

            os.makedirs("auth", exist_ok=True)
            with open(self.TOKEN_FILE, "w") as token:
                token.write(creds.to_json())
        return creds
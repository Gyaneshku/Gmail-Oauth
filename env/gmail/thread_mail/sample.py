from django.shortcuts import render
import requests
from requests.auth import HTTPBasicAuth

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

token = {
  "access_token": "ya29.a0AeTM1idEmyNbUB-D66qFePUbeNoDZGJSgyz5E81Kgr64QytV37Q5VvWh1JBX8WrcrEMJZxNd6Tk5dGok8udHgU6LBn9sJYDW3QbvumaVJ0n5Fjj9uCLCpGV-VJ1R0L7SxppuILyYQqdFGJGI80TuBJV-VDLSaCgYKAUASARASFQHWtWOmbbnwEAkzBinQeaJrzI1v1g0163", 
  "scope": "https://www.googleapis.com/auth/gmail.addons.current.message.action https://www.googleapis.com/auth/gmail.insert https://www.googleapis.com/auth/gmail.addons.current.message.readonly https://www.googleapis.com/auth/gmail.compose https://www.googleapis.com/auth/gmail.send https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.metadata https://www.googleapis.com/auth/gmail.addons.current.action.compose https://mail.google.com/ https://www.googleapis.com/auth/gmail.labels", 
  "token_type": "Bearer", 
  "client_id": "991060010699-0i8bh18bu5t94ou4b241bd4vch5n5dui.apps.googleusercontent.com",
  "client_secret": "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",
  "expires_in": 3599, 
  "refresh_token": "1//04UuloMKVEuHLCgYIARAAGAQSNwF-L9IrqD7hqm-MReF8eoDAP87ITcbH5zoKAheg2p6qa0K_5amTv8bZLfQ1VMCKC4CD3mVYiME"
}
  
try:
    creds = Credentials.from_authorized_user_info(token, SCOPES)
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().threads().list(userId='it.developer01@nodbearings.net', q='RFI 5463ISQ').execute()
    # print(results)
    resp = results.get('threads')
    print(resp)
    thread_id = resp[0].get('id')
    print(thread_id, '---final thread id of mail ----')
except HttpError as error:
    print("Error hai")

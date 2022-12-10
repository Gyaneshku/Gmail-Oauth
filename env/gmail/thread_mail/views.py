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


def mail():
    token = {
    "access_token": "ya29.a0AeTM1iflJjZMA1ESScTmcjJi8ZVt6d0vZUoS40-eSrIFSY5gaPLoc6S3Fqsw3RUJ1tCaq_3kG5n8KXspTOXvTc3SFSHPNEIvY0ZFv8i57722MuWI6RuMijNVA3VGbdL8qiyiAYt2tEiA-qAVwWGPmrEPVhSHaCgYKAd8SARASFQHWtWOm7s1VljfDfHnuoZ_3TKbzrg0163",
    "scope": "https://www.googleapis.com/auth/gmail.readonly",
    "token_type": "Bearer",
    "expires_in": 3599,
    "client_id":"991060010699-0i8bh18bu5t94ou4b241bd4vch5n5dui.apps.googleusercontent.com",
    "client_secret": "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",
    "refresh_token": "1//04zAnAkGIhrOlCgYIARAAGAQSNwF-L9IrCEz9cyzfw0q5akXbiipcVWIgQfN-OKts3MK_QXL6_MSUbYZVaRXLwsxECG-w3Xyrm14"
  
  }
  

    try:
        creds = Credentials.from_authorized_user_info(token, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        for label in labels:
            print(label, "----test----")
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
# def gmail_thread(request):
#     if request.method == 'GET':
#         value = mail()
#     print(value[0])
#     return render(request, 'index.html',{"data":str(value[0])})

def crm_test(request):
    #Calling CRM DEals api folder
    url = "https://nethunt.com/api/v1/zapier/actions/create-record/621b6ad6eb35455b10a2e6ce"
    headers = {"Content-Type":"application/json"}
    auth = HTTPBasicAuth('it.developer01@nodbearings.net','8a202acb-fae1-4607-a974-e516e6f0507f')
    data = {
            "timeZone": "Europe/London",
            "fields": {
                'Name':'Gyanesh_test','Brand':'zwz',
                'Stage':'Customer Support (Sales) - RFI/RFQ','Source': 'Webstore',
                }
    }
    response = requests.post( url= url,headers= headers,auth = auth, json = data)
    print(response,'-----CRM Deals folder Check----')
    resp_data = response.json()
    record_id = resp_data.get('recordId')
    print(resp_data)
    # Calling Gmail Function
    value = mail()
    thread= str(value[0]) # Getting Thread from gmail api with the particular RFI Number
   # Calling CRM for Mail integration
    g_url = 'https://nethunt.com/api/v1/zapier/actions/link-gmail-thread/'+record_id
    print(g_url,"---final url call check-----")
    g_data = {
        "gmailThreadId":thread
    }
    print(g_data,'-----CRM Gmail Thread check----')
    m_response = requests.post(url =g_url,headers= headers,auth = auth,json = g_data )
    print(m_response.json(),'--------- testing gmail thread CRM ----')
    return render (request, 'test.html')




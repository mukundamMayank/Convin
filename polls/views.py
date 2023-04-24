


from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from django.shortcuts import redirect

from django.shortcuts import HttpResponse
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import json

def GoogleCalendarInitView(request):
    flow = InstalledAppFlow.from_client_secrets_file(
        '/home/mayank/Desktop/placement/convin/mysite/polls/client_secret_1052611409115-3maref8c47trunr8foe7lrvhkp0dh642.apps.googleusercontent.com.json',
        scopes=['https://www.googleapis.com/auth/calendar.readonly'],
        redirect_uri='http://localhost:8000'
    )
    auth_url, _ = flow.authorization_url(prompt='consent')
    print("auth_url is =  ", auth_url)
    return redirect(auth_url)





def GoogleCalendarRedirectView(request):
	print('hello world')
	if 'error' in request.GET:
		return HttpResponse('Authorization failed: %s' % request.GET['error'])
	if 'code' not in request.GET:
		return HttpResponse('Authorization failed: invalid state')

	print('code is = ', request.GET['code'])
	flow = InstalledAppFlow.from_client_secrets_file('/home/mayank/Desktop/placement/convin/mysite/polls/client_secret_1052611409115-3maref8c47trunr8foe7lrvhkp0dh642.apps.googleusercontent.com.json',scopes=['https://www.googleapis.com/auth/calendar.readonly'],redirect_uri = 'http://localhost:8000')
	access_token = flow.fetch_token(code=request.GET['code'])
	print("access_token is ", access_token)
	credentials = flow.credentials
	print("credentials is ", credentials)
	if not credentials.valid:
		if credentials.expired and credentials.refresh_token:
			credentials.refresh(Request())
	service = build('calendar', 'v3', credentials=credentials)
	events_result = service.events().list(calendarId='primary', timeMin=datetime.datetime.utcnow().isoformat() + 'Z', maxResults=10, singleEvents=True, orderBy='startTime').execute()
	events = events_result.get('items', [])
	res = []
	for i in events:
		x = {
			"kind":i['kind'],
			"id":i['id'],
			"title":i['summary'],
			"start_time":i['start']['dateTime'],
			"end_time":i['end']['dateTime']
		}

		res.append(x)

	return HttpResponse(json.dumps(res))
    


	


- To initiate the login screen, navigate to "https://localhost:8000/rest/v1/calendar/init/" and use the Gmail account you wish to sign in with. Follow the steps as they appear, and you will receive a request URL with code and state query parameters.
- For the other API "rest/v1/calendar/redirect," use the code and state query parameters, and you will receive an access_token along with its expiry time and refresh token. The refresh token is to be used once the token expires. Hit the URL that has been created, and you will receive a list of events marked in your calendar.


**Note for reviewers**
- Although I'm obtaining more data from the Google API than displayed, I have only shown certain information on the screen. I have also sent an email regarding how the display should be, but I have not received a response yet.

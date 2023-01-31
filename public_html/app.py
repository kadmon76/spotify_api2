
import os
import json
import requests
import hashlib
import base64
from refresh import refresh
CURRENT_DIR    = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE    = CURRENT_DIR + "/../files/spotibot_comf.json"
def getConfig():
    try:
        f = open(CONFIG_FILE)
        data = json.load(f)
        return data
    except(Exception) as err:
        print(err)
        
CONFIG        = getConfig()
AUTH_URL      = CONFIG.get('AUTH_URL')
CLIENT_ID     = CONFIG.get('CLIENT_ID')
CLIENT_SECRET = CONFIG.get('CLIENT_SECRET')  
USER_ID       = CONFIG.get('USER_ID')
REDIRECT_URI  = CONFIG.get('REDIRECT_URI')   
BASE_API_URL  ='https://api.spotify.com/v1'
# Create a state token to prevent request forgery.
STATE = hashlib.sha256(os.urandom(1024)).hexdigest()


class SpotifyApi:
    def __init__(self):
        self.user_id = USER_ID
        self.spotify_token = ''
    def get_access_token(self):
        refreshCaller = refresh()
        self.spotify_token = refreshCaller.refresh()
        print('refreshing token')
        return self.spotify_token
    def creat_playlist(self, playlist_name):
        print('creating playlist')
        endpoint = f'/users/{USER_ID}/playlists'
        headers = {
        'Authorization': f'Bearer {self.spotify_token}',
        'Content-Type' : 'application/json'      
        }   
        print(headers) 
        payload = {'name' : playlist_name}
        r = requests.post(BASE_API_URL+endpoint, headers=headers, json =payload)
        r_json = r.json()
        

        
        
        
a = SpotifyApi()
a.get_access_token()
a.creat_playlist('test')















# request_url = 'https://accounts.spotify.com/authorize?'
# payload = {'client_id': CLIENT_ID,
#         'response_type' : 'code',
#         'redirect_uri' : REDIRECT_URI,
#         'state':STATE,
#         'scope' : SCOPE }
# r= requests.get(request_url , params=payload )
# print(r.status_code)




# code = 'AQCP1fDKW0wWz8inpikp3Ov_-Vf6u6yWoiz02CtKN-Px8YYYuXxpIAnsHmte4F9Wa1Ms8-mWs5ZQUC6eb0ITCUjjrCSIjN3DwhSMf-mm6WtLHceWR25aGc08VGGnKUK_Rbq3a9kL3ipiiuedJFsakwN7myg8jJwMZ8pfmHdRNVD_oFawSbUh2em0iTKtEjrI4MNaDgfaMmLGE2fap6z-G_50rDXoDi8Q1Ajg'
# b = base64.b64encode(bytes(CLIENT_ID+":"+CLIENT_SECRET, 'utf-8'))
# base64_str = b.decode('utf-8')
# print(base64_str)
# headers = {'Authorization' : f'Basic YzM3OWFiOGU0ZjlkNDhjMWE1NGRlMmMwMGE1YTBhYjM6ZThlZDA0MzQzYWI2NGM5OWFiNmY3ODVjZTYxMGE5MjQ=',
#            'Content-Type' : 'application/x-www-form-urlencoded'}
# payload = {'grant_type' : 'authorization_code',
#            'code' : code,
#            'redirect_uri' : REDIRECT_URI}


# r = requests.post(url ='https://accounts.spotify.com/api/token',headers=headers , params=payload)
# print(r.status_code)
# print(r.text)


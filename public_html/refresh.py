"""
     automate get access token from spotify api using a refresh_token.
     only will work if has a valid refresh_token that we will exchange for a new access toekn and a new refresh_token. 

    Returns:
        _type_: _description_
    """


import os
import json
import base64
import hashlib
import requests

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
REDIRECT_URI  = CONFIG.get('REDIRECT_URI')   
SCOPE         = CONFIG.get('SCOPE')
REFRESH_TOKEN = CONFIG.get('REFRESH_TOKEN')
# Create a state token to prevent request forgery.
STATE = hashlib.sha256(os.urandom(1024)).hexdigest()

b = base64.b64encode(bytes(CLIENT_ID+":"+CLIENT_SECRET, 'utf-8'))
base64_str = b.decode('utf-8')




class refresh : 
    def __init__(self) -> None:
        self.refresh_token = REFRESH_TOKEN
        self.auth_base64 = base64_str
        
    def refresh(self):
        payload = {'grant_type' : 'refresh_token',
                   'refresh_token' : self.refresh_token
        }
        headers = {'Authorization' : 'Basic '+self.auth_base64,
                   'Content-Type' : 'application/x-www-form-urlencoded'}
        
        r = requests.post(url=AUTH_URL ,headers=headers, params=payload )
        r_json = r.json()
        access_token = r_json['access_token']
        return access_token

        
a = refresh()
a.refresh()




# https://accounts.spotify.com/authorize?client_id=c379ab8e4f9d48c1a54de2c00a5a0ab3&response_type=code&redirect_uri=https%3A%2F%2Ftry.yaronl.com&scope=playlist-modify-public%20playlist-modify-private

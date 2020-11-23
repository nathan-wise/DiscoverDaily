import requests, json
import keys

user_id = keys.user_id
auth = keys.oauth_token

class BuildPlaylist():
    
    def __init__(self):
        self.user_id = user_id
        self.auth = auth

    def createPlaylist(self):

        request_body = json.dump({
                "name": "Discord Playlist",
                "description": "Playlist related to discord chat",
                "public": False
        })
        
        query = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {auth}"
            }
        )
        response_json = response.json()

        return response_json["id"] 
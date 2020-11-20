import requests, json
import keys

clientId = keys.client_id
clientSecret = keys.client_secret

class BuildPlaylist():
    
    def __init__(self):
        self.clientId = clientId

    def createPlaylist(self):

        request_body = json.dump({
                "name": "Discord Playlist",
                "description": "Playlist related to discord chat",
                "public": False
        })

        query = f"https://api.spotify.com/v1/users/{clientId}/playlists"
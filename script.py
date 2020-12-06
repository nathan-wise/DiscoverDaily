import requests, json
import keys

user_id = keys.user_id
auth = keys.oauth_token

class BuildPlaylist():
    
    def __init__(self):
        self.user_id = user_id
        self.auth = auth

    """
    Leave this commented for now do not want to run up uses of auth
    """
    # def create_playlist(self):

    #     request_body = json.dump({
    #             "name": "Discord Playlist",
    #             "description": "Playlist related to discord chat",
    #             "public": False
    #     })
        
    #     query = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    #     response = requests.post(
    #         query,
    #         data=request_body,
    #         headers={
    #             "Content-Type":"application/json",
    #             "Authorization":f"Bearer {auth}"
    #         }
    #     )
    #     response_json = response.json()

    #     return response_json["id"] 
    
    def get_song(self, track, artist):
        #  Spotify calls songs -> tracks (tracks can be sung or instrumental/songs have to have singing)

        query = f"https://api.spotify.com/v1/search?q={track}%2C{artist}&type=track%2Cartist&market=US&limit=5&offset=0"

        response = requests.get(
            query,
            headers={
                "Content-Type":"application/json",
                "Authorization":f"Bearer {auth}"
            }
        )
        response_json = response.json()

        # pulls up the list of tracks
        songs = response_json["tracks"]["items"]
        # returns the first track
        uri = songs[0]["uri"]
        return uri

build = BuildPlaylist()
print(build.get_song("Shadow", "Kesha"))
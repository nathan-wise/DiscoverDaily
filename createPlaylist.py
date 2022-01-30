import json, requests
from secrets import user_id, spotify_token

class CreatePlaylist:

    def __init__(self) -> None:
        self.user_id = user_id
        self.spotify_token = spotify_token

    def checkPlaylists(self):
        check_query = "https://api.spotify.com/v1/users/{self.user_id}/playlists"

        # request_body = json.dumps {
            
        # }

        response = requests.get(
            check_query,
            # data=request_body,
            headers={
                "Authorization" : "Bearer {self.spotify_token}",
                "Content-Type": "application/json"
            }
        )

        response_json = response.json()
        print(response_json)

    def createPlayList(self):
        pass

test = CreatePlaylist()
test.checkPlaylists()
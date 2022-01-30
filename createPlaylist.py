from asyncio.windows_events import NULL
import json, requests
from secrets import user_id, spotify_token

class CreatePlaylist:
    """
    create a playlist with new songs everyday

    checkPlaylists: checks to see if there is a playlist by the name "Discover Daily"
    createPlaylist: creates a playlist if there no existing playlist
    updatePlaylist: updates the playlist
    """

    def __init__(self) -> None:
        self.user_id = user_id
        self.spotify_token = spotify_token

    #check to see if there is already a playlist with this title
    def checkPlaylists(self):
        check_query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        response = requests.get(
            check_query,
            headers={
                "Authorization": f"Bearer {self.spotify_token}",
                "Content-Type": "application/json"
            }
        )

        response_json = response.json()
        items = response_json['items']

        playlistID = NULL

        # this range is created from the auto limit of 20
        for num in range(20):
            if items[num]['name'] == 'Discover Daily':
                playlistID = items[num]['id']
        
        if playlistID is not NULL:
            self.updatePlaylist(playlistID)
        else:
            self.createNewPlaylist()

    # if there is not a playlist with the title then create one
    def createNewPlaylist(self):
        create_query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        request_body = json.dumps({
            "name": "Discover Daily",
            "description": "Will Describe more in future",
            "public": False
        })

        response = requests.post(
            create_query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_token}"
            }
        )

        response_json = response.json()
        playlistID = response_json["id"]
        self.updatePlaylist(playlistID)

    #if there is a playlist with that title then update it
    def updatePlaylist(self, playlistID):
        print(playlistID)


test = CreatePlaylist()
check = test.checkPlaylists()
print(check)
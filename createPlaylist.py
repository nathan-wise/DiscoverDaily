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
        tracks = 0

        # this range is created from the auto limit of 20
        for num in range(20):
            if items[num]['name'] == 'Discover Daily':
                # id of the playlist
                playlistID = items[num]['id']

                #number of tracks in the playlist
                tracks = items[num]["tracks"]["total"]


        if playlistID is not NULL:
            self.updatePlaylist(playlistID, tracks)
        else:
            self.createNewPlaylist()

    # if there is not a playlist with the title then create one
    def createNewPlaylist(self):
        create_query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        # the information to create the playlist
        request_body = json.dumps({
            "name": "Discover Daily",
            "description": "Will Describe more in future",
            "public": False
        })

        # sending off the post request
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

        # number of tracks in the playlist
        tracks = response_json["tracks"]["total"]

        self.updatePlaylist(playlistID, tracks)

    # if there is a playlist with that title then update it
    def updatePlaylist(self, playlistID, tracks):
        if tracks > 0:
            self.removeFromPlaylist(playlistID, tracks)

    # remove tracks from the playlist
    def removeFromPlaylist(self, playlistID, tracks):
        get_query = f"https://api.spotify.com/v1/playlists/{playlistID}"
        delete_query = f"https://api.spotify.com/v1/playlists/{playlistID}/tracks"

        response = requests.get(
            get_query,
            headers={
                "Authorization": f"Bearer {self.spotify_token}",
                "Content-Type": "application/json"
            }
        )

        response_json = response.json()

        # this will get the track id
        for num in range(tracks):
            track_id = response_json['tracks']['items'][num]['track']['id']
            print(track_id)
            delete_body = json.dumps({
                "tracks":[
                    {
                        "uri":f"spotify:track:{track_id}"
                    }
                ]
            })

            deletes = requests.delete(
                delete_query,
                data=delete_body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.spotify_token}"
                }
            )



        # have to know the track's id to remove it
        pass


test = CreatePlaylist()
check = test.checkPlaylists()
print(check)
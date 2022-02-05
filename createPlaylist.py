from asyncio.windows_events import NULL
import json, requests

from randomGenerator import RandomGenerator
from secrets import user_id, spotify_token

# user_id is the users name like "thraac"
# spotify_token is the oauth token

class CreatePlaylist:
    """
    create a playlist with new songs everyday

    checkPlaylists: checks to see if there is a playlist by the name "Discover Daily"
    createNewPlaylist: creates a playlist if there no existing playlist
    getSong: finds random songs on Spotify
    updatePlaylist: updates the playlist
    removeFromPlaylist: removes all existing songs from the playlist
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

        playlist_id = NULL
        tracks = 0

        # this range is created from the auto limit of 20
        for num in range(20):
            if items[num]['name'] == 'Discover Daily':
                # id of the playlist
                playlist_id = items[num]['id']

                #number of tracks in the playlist
                tracks = items[num]["tracks"]["total"]


        if playlist_id is not NULL:
            self.updatePlaylist(playlist_id, tracks)
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
        playlist_id = response_json["id"]

        # number of tracks in the playlist
        tracks = response_json["tracks"]["total"]

        self.updatePlaylist(playlist_id, tracks)

    def getSong(self):
        rand = RandomGenerator()

        randomChar = rand.getRandomCharacter()
        randomOff = rand.getRandomOffset()
        randomTrack = rand.getRandomTrack()

        search_query = f"https://api.spotify.com/v1/search?q={randomChar}%25&type=track&offset={randomOff}"

        search_response = requests.get(
            search_query,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.spotify_token}"
            }
        )

        search_json = search_response.json()
        return search_json["tracks"]["items"][randomTrack]['id']

    # if there is a playlist with that title then update it
    def updatePlaylist(self, playlist_id, tracks):
        if tracks > 0:
            self.removeFromPlaylist(playlist_id, tracks)

        add_query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        five = 5

        # change the 5 to any number this is the number of songs that will be gotten
        while five > 0:
            songToAdd = self.getSong()
            add_body = json.dumps({
                "uris":[
                        f"spotify:track:{songToAdd}"
                ]
            })

            add_response = requests.post(
                add_query,
                data=add_body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.spotify_token}"
                }
            )

            five -= 1

    # remove tracks from the playlist
    def removeFromPlaylist(self, playlist_id, tracks):
        get_query = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        delete_query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

        # this is to get the track in the playlist which is used later for track_id
        response = requests.get(
            get_query,
            headers={
                "Authorization": f"Bearer {self.spotify_token}",
                "Content-Type": "application/json"
            }
        )
        response_json = response.json()
       
        for num in range(tracks):
            # this will get the track id
            track_id = response_json['tracks']['items'][num]['track']['id']

            # the code to delete the track
            delete_body = json.dumps({
                "tracks":[
                    {
                        "uri":f"spotify:track:{track_id}"
                    }
                ]
            })

            # the request to delete the track
            deletes = requests.delete(
                delete_query,
                data=delete_body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.spotify_token}"
                }
            )



test = CreatePlaylist()
check = test.checkPlaylists()
print(check)
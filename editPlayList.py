import requests, json
import keys

user_id = keys.user_id
auth = keys.oauth_token

class EditPlayist():
    """
    This will add a song to a play list
    This may need to be broken into two pieces later one piece editing the playlist
    And the other piece getting either the current playing song or a specific song
    """
    # base set up
    def __init__(self):
        self.user_id = user_id
        self.auth = auth
    
    # get playlist to add song to
    
    # get a specific song
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
    
    # add song to playlist


build = BuildPlaylist()
print(build.get_song("Shadow", "Kesha"))
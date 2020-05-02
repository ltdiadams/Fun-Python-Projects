# Script making use of Spotipy Lib for Spotify to find the top song of the week
# in the 'Hot Hits Canada' playlist and text me with the Name, Artist and Release Date
# for a recommendation! Maybe randomize and schedule it to text daily with a new song?
# Much to think about...

from twilio.rest import Client
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import schedule

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_SECRET'

account_sid = 'YOUR_SID'
auth_token = 'YOUR_TOKEN'

client = Client(account_sid, auth_token)
sender = 'TWILIO_NUM'
reciever = 'MY_NUM'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('Spotify', '37i9dQZF1DWXT8uSSn6PRy') # Hot Hits Canada Playlist

def getTrack(id):
  meta = sp.track(id)

  name = meta['name']
  # album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']

  track = [name, artist, release_date]
  return track

# get top track, functionality to do more in the future though...
track = getTrack(ids[0])

text = "Check out Canada's top hit: " + track[0] + " by " + track[1] + "!! Released: " + track[2]
client.messages.create(to=reciever, from_=sender, body=text)
# print(text)

# create dataset
# df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity'])
# df.to_csv("spotify.csv", sep = ',')

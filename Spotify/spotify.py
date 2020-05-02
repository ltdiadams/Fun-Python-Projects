# Script making use of Spotipy Lib for Spotify to get a random song from the 'Today's Top Hits' playlist
# and text me with the Name, Artist, Release Date, Song Link and Album Art
# for a recommendation! Maybe schedule it to text daily with a new song?
# Much to think about...

from twilio.rest import Client
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import schedule
from random import randrange

# credentials for spotify dev account
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_SECRET'

# credentials for your twilio number
account_sid = 'YOUR_SID'
auth_token = 'YOUR_TOKEN'

client = Client(account_sid, auth_token)
sender = 'YOUR_TWILIO_NUM'
reciever = 'YOUR_RECIPIENT'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

# get access to playlist
ids = getTrackIDs('Spotify', '37i9dQZF1DXcBWIGoYBM5M') # Today's Top Hits Playlist

# get track information
def getTrack(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  name = meta['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']

  uri = features[0]['uri'] # uri is a special link to a track but needs to be hyperlink
  url = "https://open.spotify.com/track/" + uri[14:] # turns uri for a track into https
  art = meta['album']['images'][0]['url'] # gets album art

  track = [name, artist, release_date, url, art]
  return track

# get random track in playlist of 50 songs
track = getTrack(ids[randrange(50)])

# compose text message complete with song link and album cover
text = "Check out today's top hits: " + track[0] + " by " + track[1] + "!! Released: " + track[2] + " " + track[3]
client.messages.create(to=reciever, from_=sender, body=text, media_url=track[4])

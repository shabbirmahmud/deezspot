import sys
import os

# Add the local deezloader directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from deezloader.spotloader import SpoLogin

# Adjust the path to the credentials.json file
credentials_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'credentials.json'))
spo = SpoLogin(credentials_path=credentials_path)

# Example usage of SpoLogin to download a track with high quality
track_id = 'https://open.spotify.com/track/4tCtwWceOPWzenK2HAIJSb?si=O-Z88HlnSnu4vRLbwTOd4A'
tracks= spo.download_track(track_id, output_dir='./downloads/tracks', quality_download='NORMAL')
print(tracks.song_path)


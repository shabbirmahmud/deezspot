import sys
import os

# Add the local deezloader directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from deezloader.spotloader import SpoLogin

# Adjust the path to the credentials.json file
credentials_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'credentials.json'))
spo = SpoLogin(credentials_path=credentials_path)

# Example usage of SpotLoader to download a track with normal quality
try:
    track = spo.download_track("https://open.spotify.com/track/4tCtwWceOPWzenK2HAIJSb?si=O-Z88HlnSnu4vRLbwTOd4A", 
                             output_dir='./downloads/tracks', 
                             quality_download='NORMAL')
    print(f"Successfully downloaded: {track.song_path}")
except Exception as e:
    print(f"Error downloading track: {str(e)}")

# Example usage of SpotLoader to download an album with high quality
try:
    album = spo.download_album("https://open.spotify.com/album/6n4YU8iRm07O7lR1zQZypN?si=bx3Xdxn7QV2B69MfQvDURQ", 
                             output_dir='./downloads/albums', 
                             quality_download='HIGH')
    print(f"Successfully downloaded: {album.album_name}")
except Exception as e:
    print(f"Error downloading album: {str(e)}")

# Example usage of SpotLoader to download a playlist with normal quality
try:
    playlist = spo.download_playlist("https://open.spotify.com/playlist/1ZyEi4bBTYGTIlY23U1kwG?si=56bQ2HShRXC1iGIwzkPYMw", 
                             output_dir='./downloads/playlists', 
                             quality_download='NORMAL')
    print(f"Successfully downloaded: {playlist.playlist_name}")
except Exception as e:
    print(f"Error downloading playlist: {str(e)}")
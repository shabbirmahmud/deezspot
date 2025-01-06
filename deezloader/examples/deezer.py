
import sys
import os

# Add the local deezloader directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from deezloader.deezloader import DeeLogin
import traceback
# Login
dl = DeeLogin(
            arl='Your arl',
            email='email',
            password='password',
)

# Download single track with MP3 320kbp
try:
    down = dl.download_episode(
                link_episode='https://www.deezer.com/en/episode/698290121',
                output_dir='./downloads/track',
                quality_download='MP3_320',
                recursive_quality=False,
                recursive_download=False,
                not_interface=False,
                method_save=1,
    )
except Exception as e:
    traceback.print_exc()

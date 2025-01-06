
import sys
import os

# Add the local deezloader directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from deezloader.deezloader import DeeLogin
import traceback
# Login
dl = DeeLogin(
            arl='42dfada98821e9ba118c2f72029221533f0cff61fdb2b7bf8cce757b6b34507630817003a0d0f57eb599022f18491d7d0597d9a7d03ebd4725cf8230ad13f77f90c676822e78b7b36a218a1903a810af9f8a04eea6f8eb68288438f63124f69d',
            email='farihmuhammad75@gmail.com',
            password='Farih2009@',
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
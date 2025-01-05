# Deezloadclone UNDER DEVELOPMENT
A clone from [deezloader](https://pypi.org/project/deezloader) with fix some bugs and giving some error handling :D


# Disclaimer

- I am not responsible for the usage of this program by other people.
- I do not recommend you doing this illegally or against Deezer's terms of service.

* ### PYTHON VERSION SUPPORTED ###
	![Python >= 3.9](https://img.shields.io/badge/python-v%3E=3.9-blue)

* ### OS Supported ###
	![Linux Support](https://img.shields.io/badge/Linux-Support-brightgreen.svg)
	![macOS Support](https://img.shields.io/badge/macOS-Support-brightgreen.svg)
	![Windows Support](https://img.shields.io/badge/Windows-Support-brightgreen.svg)

# Install?
first install it using pip
```
pip3 install git+https://github.com/farihdzkyy/deezloadclone
```
# Configure
You need to login for using this package.
**Deezer**
```
from deezloadclone.deezloader import DeeLogin 
downloa = DeeLogin(
            arl='your arl token',
            email='email login deezer',
            password='password',
)
```
**Spotify**
```
from deezloadclone.deezloader import SpoLogin

spodown = SpoLogin(
    email='your spotify email',
    pwd='your spotify account password'
)
```

Enjoy to use!


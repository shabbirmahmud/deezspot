from setuptools import setup

README = open("README.md", "r")
readmed = README.read()
README.close()

setup(
	name = "deezloaderclone",
	version = "2024.04.04",
	description = "Downloads songs, albums or playlists from deezer and spotify (cloned from https://github.com/An0nimia/deezloader)",
	long_description = readmed,
	long_description_content_type = "text/markdown",
	license = "GNU Affero General Public License v3",
	python_requires = ">=3.10",
	author = "farihdzaky",
	author_email = "farihdzakyy@gmail.com",
	url = "https://github.com/farihdzkyy/deezloadclone",

	packages = [
		"deezloader",
		"deezloader/models", "deezloader/spotloader",
		"deezloader/deezloader", "deezloader/libutils"
	],

	install_requires = [
		"mutagen", "pycryptodome", "requests",
		"spotipy", "tqdm", "fastapi",
		"uvicorn[standard]", "git+https://github.com/kokarare1212/librespot-python"
	],

	scripts = [
		"deezloader/bin/deez-dw.py",
		"deezloader/bin/deez-web.py"
	]
)

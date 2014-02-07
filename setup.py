from distutils.core import setup
PACKAGE = "lazyopt"
NAME = "lazyopt"
DESCRIPTION = "the lazy coder's option parser"
AUTHOR = "mark neyer"
AUTHOR_EMAIL = "mneyer@gmail.com"
URL = "https://github.com/neyer/lazyopt"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=[PACKAGE]
)

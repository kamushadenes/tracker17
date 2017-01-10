import os
from distutils.core import setup

long_description = 'This small tool can be used to track mail packages from about anywhere on the world thanks to 17track.net service.'

if os.path.exists('README.md'):
    long_description = open('README.md', 'r').read()


setup(
  name = '17tracker',
  packages = ['17tracker'], # this must be the same as the name above
  version = '0.1',
  description = '17Track.net Python API (Unnoficial)'
  long_description = long_description,
  author = 'Kamus Hadenes',
  author_email = 'kamushadenes@hyadesinc.com',
  url = 'https://github.com/kamushadenes/17tracker', # use the URL to the github repo
  download_url = 'https://github.com/kamushadenes/17tracker/tarball/0.1', # I'll explain this in a second
  keywords = ['tracking', 'mail', 'api'], # arbitrary keywords
)


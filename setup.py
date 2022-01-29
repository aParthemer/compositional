from distutils.core import setup

import setuptools

setup(
  name = 'MidiCompose',
  version = '0.3',
  license='MIT',
  description = 'Library for programatically composing music using midi.',
  author = 'Alex Parthemer',
  author_email = 'alexparthemer@gmail.com',
  url = 'https://github.com/aParthemer/MidiCompose',
  download_url = 'https://github.com/aParthemer/MidiCompose/archive/refs/tags/v_02.tar.gz',
  keywords = ["midi","python","music"],
  install_requires=[
    'numpy',
    'mido',
    'icecream'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  packages=setuptools.find_packages(where="."),
  python_requires=">=3.6"
)
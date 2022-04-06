from distutils.core import setup

import setuptools

setup(
    name='compositional',
    version='0.0.5',
    license='MIT',
    description='Library for programatically composing music using midi.',
    author='Alex Parthemer',
    author_email='alexparthemer@gmail.com',
    url='https://github.com/aParthemer/compositional',
    download_url='https://github.com/aParthemer/compositional/archive/refs/tags/v_04.tar.gz',
    keywords=["midi", "python", "music"],
    install_requires=[
        'numpy',
        'mido',
        'icecream',
        'typing-extensions'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=setuptools.find_packages(
        where=".",
        exclude=("*rendering.*", "*rendering", "*tests.*", "*tests")
    ),
    python_requires=">=3.6"
)

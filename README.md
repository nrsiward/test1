## ufo2ttf.py

Convert a UFO into a ttf file without OpenType tables using minimal processing (compared to fontmake).

Compared to the below it does not decompose glyphs or remove overlaps and curve conversion seems to happen in a different way.


## ufo2ttf_fontmake.py

This script should be functionally equivalent to how fontmake converts a UFO to a ttf file except that it excludes
the compilation of fea and the renaming of glyphs to production names.

## Installation

The easiest way to install all the needed libraries is to install fontmake. (A smith vm may already have fontmake 
installed -- see below.) Either of the below should work:

`sudo pip install fontmake`

or

`pip install --user fontmake`

If you want to isolate all eleven of the libraries fontmake needs, you can install fontmake in a virtual environment
and run the scripts there. Please note that a virtual environment won't work simply with smith.

If your smith vm already has fontmake installed, try running ufo2ttf.py. If it produces errors concerning modules 
that cannot be found, you may need to use Python 2 and update the fontmake dependencies:

`sudo -H python2 -m pip install fontmake`

`sudo -H python2 -m pip install --upgrade fontmake`

`python2 ufo2fea.py`

## Adding OpenType support
FWIW, OpenType support can be added using fonttools after running either ufo2ttf script. features.fea can be compiled using the command line:

`fonttools feaLib [-h] [-o <fn>] [-v] <fea fn> <ttf fn>`

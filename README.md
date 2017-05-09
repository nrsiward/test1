## ufo2ttf.py

Convert a UFO into a ttf file without OpenType tables using minimal processing (compared to fontmake)


## ufo2ttf_fontmake.py

This script should be functionally equivalent to how fontmake converts a UFO to a ttf file except that it excludes
the compilation of fea and the renaming of glyphs to production names

## Installation

The easiest way to install all the needed libraries is to install fontmake.

[sudo] pip install [--user] fontmake

If you want to isolate all the libraries fontmake needs, you can install it in a virtual environment
and run this script there
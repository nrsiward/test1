# Convert a UFO into a ttf file without OpenType tables
# using minimal processing (compared to fontmake)

# The easiest way to install all the needed libraries is to install fontmake.
#   [sudo] pip install fontmake
# If you want to isolate all the libraries fontmake needs,
# you can install it in a virtual environment and run this script there

from __future__ import print_function
import sys
import defcon, ufo2ft.outlineCompiler, ufo2ft.preProcessor

try:
    ufo_fn = sys.argv[1]
    ttf_fn = sys.argv[2]
except:
    print("ufo2ttf <ufo> <output ttf>")
    sys.exit()

PUBLIC_PREFIX = 'public.'

ufo = defcon.Font(ufo_fn)

# print('Converting UFO to ttf and compiling fea')
# font = ufo2ft.compileTTF(ufo,
#     glyphOrder = ufo.lib.get(PUBLIC_PREFIX + 'glyphOrder'),
#     useProductionNames = False)

print('Converting UFO to ttf without OT')
#the named arg values are the same as the default values
preProcessor = ufo2ft.preProcessor.TTFPreProcessor(ufo, removeOverlaps=False, convertCubics=True)
glyphSet = preProcessor.process()

outlineCompiler = ufo2ft.outlineCompiler.OutlineTTFCompiler(ufo, glyphSet=glyphSet,
    glyphOrder=ufo.lib.get(PUBLIC_PREFIX + 'glyphOrder'))
font = outlineCompiler.compile()

print('Saving ttf file')
font.save(ttf_fn)

print('Done')

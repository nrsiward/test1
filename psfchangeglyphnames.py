# Rename the glpyhs in a ttf file based on production names in a UFO
#  using same technique as fontmake

# The easiest way to install all the needed libraries is to install fontmake.
#   [sudo] pip install fontmake
# If you want to isolate all the libraries fontmake needs,
# you can install it in a python virtual environment and run this script there

import sys
import defcon
import fontTools.ttLib
import ufo2ft

try:
    ufo_fn = sys.argv[1]
    in_ttf_fn = sys.argv[2]
    out_ttf_fn = sys.argv[3]
except:
    print("psfchangeglyphnames <ufo> <input ttf> <output ttf>")
    sys.exit()

ufo = defcon.Font(ufo_fn)
ttf = fontTools.ttLib.TTFont(in_ttf_fn)
postProcessor = ufo2ft.PostProcessor(ttf, ufo)
ttf = postProcessor.process(useProductionNames=True, optimizeCFF=False)
ttf.save(out_ttf_fn)

# This script should be functionally equivalent to how fontmake
# converts a UFO to a ttf file except that it excludes 
# the compilation of fea and the renaming of glyphs to production names

# The easiest way to install all the needed libraries is to install fontmake.
#   [sudo] pip install [--user] fontmake
# If you want to isolate all the libraries fontmake needs,
# you can install it in a virtual environment and run this script there


from __future__ import print_function
import sys
import defcon, booleanOperations, cu2qu, cu2qu.ufo, ufo2ft, ufo2ft.outlineCompiler, fontTools

try:
    ufo_fn = sys.argv[1]
    ttf_fn = sys.argv[2]
except:
    print("ufo2ttf_fontmake <ufo> <output ttf>")
    sys.exit()

font_nm = None
PUBLIC_PREFIX = 'public.'

def _font_name(ufo):
    """Generate a postscript-style font name."""
    return '%s-%s' % (ufo.info.familyName.replace(' ', ''),
                      ufo.info.styleName.replace(' ', ''))

def remove_overlaps(ufo):
    for glyph in ufo:
        contours = list(glyph)
        glyph.clearContours()
        try:
            booleanOperations.union(contours, glyph.getPointPen())
        except BooleanOperationsError:
            print("Failed to remove overlaps for %s: %r", font_name, glyph.name)
            raise

def decompose_glyphs(ufo):
    """Move components of UFOs' glyphs to their outlines."""
    for glyph in ufo:
        if not glyph.components:
            continue
        _deep_copy_contours(ufo, glyph, glyph, fontTools.misc.transform.Transform())
        glyph.clearComponents()

def _deep_copy_contours(ufo, parent, component, transformation):
    """Copy contours from component to parent, including nested components."""

    for nested in component.components:
        _deep_copy_contours(
            ufo, parent, ufo[nested.baseGlyph],
            transformation.transform(nested.transformation))

    if component != parent:
        pen = fontTools.pens.transformPen.TransformPen(parent.getPen(), transformation)

        # if the transformation has a negative determinant, it will reverse
        # the contour direction of the component
        xx, xy, yx, yy = transformation[:4]
        if xx*yy - xy*yx < 0:
            pen = cu2qu.pens.ReverseContourPen(pen)

        component.draw(pen)


ufo = defcon.Font(ufo_fn)
font_nm = _font_name(ufo)

print('Decomposing glyphs')
decompose_glyphs(ufo)

print("Removing overlaps in UFOs' glyphs' contours")
remove_overlaps(ufo)

print('Converting curves')
cu2qu.ufo.fonts_to_quadratic([ufo], reverse_direction=True)

# print('Converting UFO to ttf and compiling fea
# font = ufo2ft.compileTTF(ufo,
    # glyphOrder = ufo.lib.get(PUBLIC_PREFIX + 'glyphOrder'), 
    # useProductionNames = False)

print('Converting UFO to ttf without OT')
outlineCompiler = ufo2ft.outlineCompiler.OutlineTTFCompiler(ufo,
    glyphOrder = ufo.lib.get(PUBLIC_PREFIX + 'glyphOrder'), 
    convertCubics = False)
font = outlineCompiler.compile()
    
print('Saving ttf file')
font.save(ttf_fn)

print('Done')

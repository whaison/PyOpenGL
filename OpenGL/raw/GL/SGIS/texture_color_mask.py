'''OpenGL extension SGIS.texture_color_mask

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_texture_color_mask'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_texture_color_mask',False)
_p.unpack_constants( """GL_TEXTURE_COLOR_WRITEMASK_SGIS 0x81EF""", globals())
@_f
@_p.types(None,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glTextureColorMaskSGIS( red,green,blue,alpha ):pass


def glInitTextureColorMaskSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

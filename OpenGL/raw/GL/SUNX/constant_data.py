'''OpenGL extension SUNX.constant_data

Overview (from the spec)
    
    This extension allows the pixel data specified by the
    application to be used internally without making a second copy.
    This extension affects how the pixel data in client memory is
    interpreted and therefore affects DrawPixels, Bitmap,
    PolygonStipple, TexImage1D, TexImage2D, TexImage3DEXT,
    ColorTableSGI.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SUNX/constant_data.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SUNX_constant_data'
_DEPRECATED = False
GL_UNPACK_CONSTANT_DATA_SUNX = constant.Constant( 'GL_UNPACK_CONSTANT_DATA_SUNX', 0x81D5 )
GL_TEXTURE_CONSTANT_DATA_SUNX = constant.Constant( 'GL_TEXTURE_CONSTANT_DATA_SUNX', 0x81D6 )
glFinishTextureSUNX = platform.createExtensionFunction( 
'glFinishTextureSUNX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glFinishTextureSUNX() -> None',
argNames=(),
deprecated=_DEPRECATED,
)


def glInitConstantDataSUNX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
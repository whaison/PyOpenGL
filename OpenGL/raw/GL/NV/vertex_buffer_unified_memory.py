'''OpenGL extension NV.vertex_buffer_unified_memory

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/NV/vertex_buffer_unified_memory.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_vertex_buffer_unified_memory'
_DEPRECATED = False
GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV', 0x8F1E )
GL_ELEMENT_ARRAY_UNIFIED_NV = constant.Constant( 'GL_ELEMENT_ARRAY_UNIFIED_NV', 0x8F1F )
GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV', 0x8F20 )
GL_VERTEX_ARRAY_ADDRESS_NV = constant.Constant( 'GL_VERTEX_ARRAY_ADDRESS_NV', 0x8F21 )
GL_NORMAL_ARRAY_ADDRESS_NV = constant.Constant( 'GL_NORMAL_ARRAY_ADDRESS_NV', 0x8F22 )
GL_COLOR_ARRAY_ADDRESS_NV = constant.Constant( 'GL_COLOR_ARRAY_ADDRESS_NV', 0x8F23 )
GL_INDEX_ARRAY_ADDRESS_NV = constant.Constant( 'GL_INDEX_ARRAY_ADDRESS_NV', 0x8F24 )
GL_TEXTURE_COORD_ARRAY_ADDRESS_NV = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_ADDRESS_NV', 0x8F25 )
GL_EDGE_FLAG_ARRAY_ADDRESS_NV = constant.Constant( 'GL_EDGE_FLAG_ARRAY_ADDRESS_NV', 0x8F26 )
GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV', 0x8F27 )
GL_FOG_COORD_ARRAY_ADDRESS_NV = constant.Constant( 'GL_FOG_COORD_ARRAY_ADDRESS_NV', 0x8F28 )
GL_ELEMENT_ARRAY_ADDRESS_NV = constant.Constant( 'GL_ELEMENT_ARRAY_ADDRESS_NV', 0x8F29 )
GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV', 0x8F2A )
GL_VERTEX_ARRAY_LENGTH_NV = constant.Constant( 'GL_VERTEX_ARRAY_LENGTH_NV', 0x8F2B )
GL_NORMAL_ARRAY_LENGTH_NV = constant.Constant( 'GL_NORMAL_ARRAY_LENGTH_NV', 0x8F2C )
GL_COLOR_ARRAY_LENGTH_NV = constant.Constant( 'GL_COLOR_ARRAY_LENGTH_NV', 0x8F2D )
GL_INDEX_ARRAY_LENGTH_NV = constant.Constant( 'GL_INDEX_ARRAY_LENGTH_NV', 0x8F2E )
GL_TEXTURE_COORD_ARRAY_LENGTH_NV = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_LENGTH_NV', 0x8F2F )
GL_EDGE_FLAG_ARRAY_LENGTH_NV = constant.Constant( 'GL_EDGE_FLAG_ARRAY_LENGTH_NV', 0x8F30 )
GL_SECONDARY_COLOR_ARRAY_LENGTH_NV = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_LENGTH_NV', 0x8F31 )
GL_FOG_COORD_ARRAY_LENGTH_NV = constant.Constant( 'GL_FOG_COORD_ARRAY_LENGTH_NV', 0x8F32 )
GL_ELEMENT_ARRAY_LENGTH_NV = constant.Constant( 'GL_ELEMENT_ARRAY_LENGTH_NV', 0x8F33 )
glBufferAddressRangeNV = platform.createExtensionFunction( 
'glBufferAddressRangeNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint64EXT,constants.GLsizeiptr,),
doc='glBufferAddressRangeNV(GLenum(pname), GLuint(index), GLuint64EXT(address), GLsizeiptr(length)) -> None',
argNames=('pname','index','address','length',),
deprecated=_DEPRECATED,
)

glVertexFormatNV = platform.createExtensionFunction( 
'glVertexFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLsizei,),
doc='glVertexFormatNV(GLint(size), GLenum(type), GLsizei(stride)) -> None',
argNames=('size','type','stride',),
deprecated=_DEPRECATED,
)

glNormalFormatNV = platform.createExtensionFunction( 
'glNormalFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,),
doc='glNormalFormatNV(GLenum(type), GLsizei(stride)) -> None',
argNames=('type','stride',),
deprecated=_DEPRECATED,
)

glColorFormatNV = platform.createExtensionFunction( 
'glColorFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLsizei,),
doc='glColorFormatNV(GLint(size), GLenum(type), GLsizei(stride)) -> None',
argNames=('size','type','stride',),
deprecated=_DEPRECATED,
)

glIndexFormatNV = platform.createExtensionFunction( 
'glIndexFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,),
doc='glIndexFormatNV(GLenum(type), GLsizei(stride)) -> None',
argNames=('type','stride',),
deprecated=_DEPRECATED,
)

glTexCoordFormatNV = platform.createExtensionFunction( 
'glTexCoordFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLsizei,),
doc='glTexCoordFormatNV(GLint(size), GLenum(type), GLsizei(stride)) -> None',
argNames=('size','type','stride',),
deprecated=_DEPRECATED,
)

glEdgeFlagFormatNV = platform.createExtensionFunction( 
'glEdgeFlagFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,),
doc='glEdgeFlagFormatNV(GLsizei(stride)) -> None',
argNames=('stride',),
deprecated=_DEPRECATED,
)

glSecondaryColorFormatNV = platform.createExtensionFunction( 
'glSecondaryColorFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLsizei,),
doc='glSecondaryColorFormatNV(GLint(size), GLenum(type), GLsizei(stride)) -> None',
argNames=('size','type','stride',),
deprecated=_DEPRECATED,
)

glFogCoordFormatNV = platform.createExtensionFunction( 
'glFogCoordFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,),
doc='glFogCoordFormatNV(GLenum(type), GLsizei(stride)) -> None',
argNames=('type','stride',),
deprecated=_DEPRECATED,
)

glVertexAttribFormatNV = platform.createExtensionFunction( 
'glVertexAttribFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLenum,constants.GLboolean,constants.GLsizei,),
doc='glVertexAttribFormatNV(GLuint(index), GLint(size), GLenum(type), GLboolean(normalized), GLsizei(stride)) -> None',
argNames=('index','size','type','normalized','stride',),
deprecated=_DEPRECATED,
)

glVertexAttribIFormatNV = platform.createExtensionFunction( 
'glVertexAttribIFormatNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLenum,constants.GLsizei,),
doc='glVertexAttribIFormatNV(GLuint(index), GLint(size), GLenum(type), GLsizei(stride)) -> None',
argNames=('index','size','type','stride',),
deprecated=_DEPRECATED,
)

glGetIntegerui64i_vNV = platform.createExtensionFunction( 
'glGetIntegerui64i_vNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,ctypes.POINTER(constants.GLuint64EXT),),
doc='glGetIntegerui64i_vNV(GLenum(value), GLuint(index), POINTER(constants.GLuint64EXT)(result)) -> None',
argNames=('value','index','result',),
deprecated=_DEPRECATED,
)


def glInitVertexBufferUnifiedMemoryNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

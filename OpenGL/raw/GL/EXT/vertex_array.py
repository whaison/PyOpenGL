'''OpenGL extension EXT.vertex_array

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_vertex_array'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_vertex_array',False)
_p.unpack_constants( """GL_VERTEX_ARRAY_EXT 0x8074
GL_NORMAL_ARRAY_EXT 0x8075
GL_COLOR_ARRAY_EXT 0x8076
GL_INDEX_ARRAY_EXT 0x8077
GL_TEXTURE_COORD_ARRAY_EXT 0x8078
GL_EDGE_FLAG_ARRAY_EXT 0x8079
GL_VERTEX_ARRAY_SIZE_EXT 0x807A
GL_VERTEX_ARRAY_TYPE_EXT 0x807B
GL_VERTEX_ARRAY_STRIDE_EXT 0x807C
GL_VERTEX_ARRAY_COUNT_EXT 0x807D
GL_NORMAL_ARRAY_TYPE_EXT 0x807E
GL_NORMAL_ARRAY_STRIDE_EXT 0x807F
GL_NORMAL_ARRAY_COUNT_EXT 0x8080
GL_COLOR_ARRAY_SIZE_EXT 0x8081
GL_COLOR_ARRAY_TYPE_EXT 0x8082
GL_COLOR_ARRAY_STRIDE_EXT 0x8083
GL_COLOR_ARRAY_COUNT_EXT 0x8084
GL_INDEX_ARRAY_TYPE_EXT 0x8085
GL_INDEX_ARRAY_STRIDE_EXT 0x8086
GL_INDEX_ARRAY_COUNT_EXT 0x8087
GL_TEXTURE_COORD_ARRAY_SIZE_EXT 0x8088
GL_TEXTURE_COORD_ARRAY_TYPE_EXT 0x8089
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT 0x808A
GL_TEXTURE_COORD_ARRAY_COUNT_EXT 0x808B
GL_EDGE_FLAG_ARRAY_STRIDE_EXT 0x808C
GL_EDGE_FLAG_ARRAY_COUNT_EXT 0x808D
GL_VERTEX_ARRAY_POINTER_EXT 0x808E
GL_NORMAL_ARRAY_POINTER_EXT 0x808F
GL_COLOR_ARRAY_POINTER_EXT 0x8090
GL_INDEX_ARRAY_POINTER_EXT 0x8091
GL_TEXTURE_COORD_ARRAY_POINTER_EXT 0x8092
GL_EDGE_FLAG_ARRAY_POINTER_EXT 0x8093""", globals())
glget.addGLGetConstant( GL_VERTEX_ARRAY_EXT, (1,) )
glget.addGLGetConstant( GL_NORMAL_ARRAY_EXT, (1,) )
glget.addGLGetConstant( GL_INDEX_ARRAY_EXT, (1,) )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_EXT, (1,) )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_ARRAY_SIZE_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_ARRAY_TYPE_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_ARRAY_STRIDE_EXT, (1,) )
glget.addGLGetConstant( GL_VERTEX_ARRAY_COUNT_EXT, (1,) )
glget.addGLGetConstant( GL_NORMAL_ARRAY_TYPE_EXT, (1,) )
glget.addGLGetConstant( GL_NORMAL_ARRAY_STRIDE_EXT, (1,) )
glget.addGLGetConstant( GL_NORMAL_ARRAY_COUNT_EXT, (1,) )
glget.addGLGetConstant( GL_COLOR_ARRAY_SIZE_EXT, (1,) )
glget.addGLGetConstant( GL_COLOR_ARRAY_TYPE_EXT, (1,) )
glget.addGLGetConstant( GL_COLOR_ARRAY_STRIDE_EXT, (1,) )
glget.addGLGetConstant( GL_COLOR_ARRAY_COUNT_EXT, (1,) )
glget.addGLGetConstant( GL_INDEX_ARRAY_TYPE_EXT, (1,) )
glget.addGLGetConstant( GL_INDEX_ARRAY_STRIDE_EXT, (1,) )
glget.addGLGetConstant( GL_INDEX_ARRAY_COUNT_EXT, (1,) )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_SIZE_EXT, (1,) )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_TYPE_EXT, (1,) )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_STRIDE_EXT, (1,) )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_COUNT_EXT, (1,) )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_STRIDE_EXT, (1,) )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_COUNT_EXT, (1,) )
@_f
@_p.types(None,_cs.GLint)
def glArrayElementEXT( i ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glColorPointerEXT( size,type,stride,count,pointer ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei)
def glDrawArraysEXT( mode,first,count ):pass
@_f
@_p.types(None,_cs.GLsizei,_cs.GLsizei,arrays.GLbooleanArray)
def glEdgeFlagPointerEXT( stride,count,pointer ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLvoidpArray)
def glGetPointervEXT( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glIndexPointerEXT( type,stride,count,pointer ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glNormalPointerEXT( type,stride,count,pointer ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glTexCoordPointerEXT( size,type,stride,count,pointer ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,ctypes.c_void_p)
def glVertexPointerEXT( size,type,stride,count,pointer ):pass


def glInitVertexArrayEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

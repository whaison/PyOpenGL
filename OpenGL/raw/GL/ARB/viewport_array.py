'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_viewport_array'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_viewport_array',False)
_p.unpack_constants( """GL_MAX_VIEWPORTS 0x825B
GL_VIEWPORT_SUBPIXEL_BITS 0x825C
GL_VIEWPORT_BOUNDS_RANGE 0x825D
GL_LAYER_PROVOKING_VERTEX 0x825E
GL_VIEWPORT_INDEX_PROVOKING_VERTEX 0x825F
GL_UNDEFINED_VERTEX 0x8260""", globals())
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glViewportArrayv(first,count,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glViewportIndexedf(index,x,y,w,h):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glViewportIndexedfv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLintArray)
def glScissorArrayv(first,count,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glScissorIndexed(index,left,bottom,width,height):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glScissorIndexedv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLdoubleArray)
def glDepthRangeArrayv(first,count,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble)
def glDepthRangeIndexed(index,n,f):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLfloatArray)
def glGetFloati_v(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLdoubleArray)
def glGetDoublei_v(target,index,data):pass


def glInitViewportArrayARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

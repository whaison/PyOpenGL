'''OpenGL extension VERSION.GL_1_4_DEPRECATED

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_4'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_1_4',True)
_p.unpack_constants( """GL_POINT_SIZE_MIN 0x8126
GL_POINT_SIZE_MAX 0x8127
GL_POINT_DISTANCE_ATTENUATION 0x8129
GL_GENERATE_MIPMAP 0x8191
GL_GENERATE_MIPMAP_HINT 0x8192
GL_FOG_COORDINATE_SOURCE 0x8450
GL_FOG_COORDINATE 0x8451
GL_FRAGMENT_DEPTH 0x8452
GL_CURRENT_FOG_COORDINATE 0x8453
GL_FOG_COORDINATE_ARRAY_TYPE 0x8454
GL_FOG_COORDINATE_ARRAY_STRIDE 0x8455
GL_FOG_COORDINATE_ARRAY_POINTER 0x8456
GL_FOG_COORDINATE_ARRAY 0x8457
GL_COLOR_SUM 0x8458
GL_CURRENT_SECONDARY_COLOR 0x8459
GL_SECONDARY_COLOR_ARRAY_SIZE 0x845A
GL_SECONDARY_COLOR_ARRAY_TYPE 0x845B
GL_SECONDARY_COLOR_ARRAY_STRIDE 0x845C
GL_SECONDARY_COLOR_ARRAY_POINTER 0x845D
GL_SECONDARY_COLOR_ARRAY 0x845E
GL_TEXTURE_FILTER_CONTROL 0x8500
GL_DEPTH_TEXTURE_MODE 0x884B
GL_COMPARE_R_TO_TEXTURE 0x884E""", globals())
@_f
@_p.types(None,_cs.GLfloat)
def glFogCoordf( coord ):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glFogCoordfv( coord ):pass
@_f
@_p.types(None,_cs.GLdouble)
def glFogCoordd( coord ):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glFogCoorddv( coord ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glFogCoordPointer( type,stride,pointer ):pass
@_f
@_p.types(None,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glSecondaryColor3b( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLbyteArray)
def glSecondaryColor3bv( v ):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glSecondaryColor3d( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glSecondaryColor3dv( v ):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glSecondaryColor3f( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glSecondaryColor3fv( v ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glSecondaryColor3i( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLintArray)
def glSecondaryColor3iv( v ):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glSecondaryColor3s( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glSecondaryColor3sv( v ):pass
@_f
@_p.types(None,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte)
def glSecondaryColor3ub( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLubyteArray)
def glSecondaryColor3ubv( v ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glSecondaryColor3ui( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLuintArray)
def glSecondaryColor3uiv( v ):pass
@_f
@_p.types(None,_cs.GLushort,_cs.GLushort,_cs.GLushort)
def glSecondaryColor3us( red,green,blue ):pass
@_f
@_p.types(None,arrays.GLushortArray)
def glSecondaryColor3usv( v ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glSecondaryColorPointer( size,type,stride,pointer ):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glWindowPos2d( x,y ):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glWindowPos2dv( v ):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glWindowPos2f( x,y ):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glWindowPos2fv( v ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glWindowPos2i( x,y ):pass
@_f
@_p.types(None,arrays.GLintArray)
def glWindowPos2iv( v ):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort)
def glWindowPos2s( x,y ):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glWindowPos2sv( v ):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glWindowPos3d( x,y,z ):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glWindowPos3dv( v ):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glWindowPos3f( x,y,z ):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glWindowPos3fv( v ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glWindowPos3i( x,y,z ):pass
@_f
@_p.types(None,arrays.GLintArray)
def glWindowPos3iv( v ):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glWindowPos3s( x,y,z ):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glWindowPos3sv( v ):pass


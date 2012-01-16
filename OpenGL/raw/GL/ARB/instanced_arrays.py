'''OpenGL extension ARB.instanced_arrays

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_instanced_arrays'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_instanced_arrays',False)
_p.unpack_constants( """GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB 0x88FE""", globals())
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribDivisorARB( index,divisor ):pass


def glInitInstancedArraysARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

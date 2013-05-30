'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_IBM_multimode_draw_arrays'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_IBM_multimode_draw_arrays',False)

@_f
@_p.types(None,arrays.GLuintArray,arrays.GLintArray,arrays.GLsizeiArray,_cs.GLsizei,_cs.GLint)
def glMultiModeDrawArraysIBM(mode,first,count,primcount,modestride):pass
@_f
@_p.types(None,arrays.GLuintArray,arrays.GLsizeiArray,_cs.GLenum,arrays.GLvoidpArray,_cs.GLsizei,_cs.GLint)
def glMultiModeDrawElementsIBM(mode,count,type,indices,primcount,modestride):pass


def glInitMultimodeDrawArraysIBM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

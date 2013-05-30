'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_copy_buffer'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_copy_buffer',False)
_p.unpack_constants( """GL_COPY_READ_BUFFER_BINDING 0x8F36
GL_COPY_READ_BUFFER 0x8F36
GL_COPY_WRITE_BUFFER_BINDING 0x8F37
GL_COPY_WRITE_BUFFER 0x8F37""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr)
def glCopyBufferSubData(readTarget,writeTarget,readOffset,writeOffset,size):pass


def glInitCopyBufferARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

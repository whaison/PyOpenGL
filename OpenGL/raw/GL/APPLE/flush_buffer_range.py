'''OpenGL extension APPLE.flush_buffer_range

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_APPLE_flush_buffer_range'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_APPLE_flush_buffer_range',False)
_p.unpack_constants( """GL_BUFFER_SERIALIZED_MODIFY_APPLE 0x8A12
GL_BUFFER_FLUSHING_UNMAP_APPLE 0x8A13""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glBufferParameteriAPPLE( target,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr)
def glFlushMappedBufferRangeAPPLE( target,offset,size ):pass


def glInitFlushBufferRangeAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

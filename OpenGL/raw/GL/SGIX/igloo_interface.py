'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_igloo_interface'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_igloo_interface',False)

@_f
@_p.types(None,_cs.GLenum,ctypes.c_void_p)
def glIglooInterfaceSGIX(pname,params):pass


def glInitIglooInterfaceSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

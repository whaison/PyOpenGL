'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_framebuffer_no_attachments'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_framebuffer_no_attachments',False)
_p.unpack_constants( """GL_FRAMEBUFFER_DEFAULT_WIDTH 0x9310
GL_FRAMEBUFFER_DEFAULT_HEIGHT 0x9311
GL_FRAMEBUFFER_DEFAULT_LAYERS 0x9312
GL_FRAMEBUFFER_DEFAULT_SAMPLES 0x9313
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS 0x9314
GL_MAX_FRAMEBUFFER_WIDTH 0x9315
GL_MAX_FRAMEBUFFER_HEIGHT 0x9316
GL_MAX_FRAMEBUFFER_LAYERS 0x9317
GL_MAX_FRAMEBUFFER_SAMPLES 0x9318""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glFramebufferParameteri(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glNamedFramebufferParameteriEXT(framebuffer,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetNamedFramebufferParameterivEXT(framebuffer,pname,params):pass


def glInitFramebufferNoAttachmentsARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

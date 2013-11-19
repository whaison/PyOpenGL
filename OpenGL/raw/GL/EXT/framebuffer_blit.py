'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_framebuffer_blit'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_framebuffer_blit')
GL_DRAW_FRAMEBUFFER_BINDING_EXT=_C('GL_DRAW_FRAMEBUFFER_BINDING_EXT',0x8CA6)
GL_DRAW_FRAMEBUFFER_EXT=_C('GL_DRAW_FRAMEBUFFER_EXT',0x8CA9)
GL_READ_FRAMEBUFFER_BINDING_EXT=_C('GL_READ_FRAMEBUFFER_BINDING_EXT',0x8CAA)
GL_READ_FRAMEBUFFER_EXT=_C('GL_READ_FRAMEBUFFER_EXT',0x8CA8)
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLbitfield,_cs.GLenum)
def glBlitFramebufferEXT(srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter):pass

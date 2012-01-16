'''OpenGL extension VERSION.GL_3_1

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_3_1'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_3_1',False)
_p.unpack_constants( """GL_SAMPLER_2D_RECT 0x8B63
GL_SAMPLER_2D_RECT_SHADOW 0x8B64
GL_SAMPLER_BUFFER 0x8DC2
GL_INT_SAMPLER_2D_RECT 0x8DCD
GL_INT_SAMPLER_BUFFER 0x8DD0
GL_UNSIGNED_INT_SAMPLER_2D_RECT 0x8DD5
GL_UNSIGNED_INT_SAMPLER_BUFFER 0x8DD8
GL_TEXTURE_BUFFER 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE 0x8C2B
GL_TEXTURE_BINDING_BUFFER 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING 0x8C2D
GL_TEXTURE_BUFFER_FORMAT 0x8C2E
GL_TEXTURE_RECTANGLE 0x84F5
GL_TEXTURE_BINDING_RECTANGLE 0x84F6
GL_PROXY_TEXTURE_RECTANGLE 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE 0x84F8
GL_RED_SNORM 0x8F90
GL_RG_SNORM 0x8F91
GL_RGB_SNORM 0x8F92
GL_RGBA_SNORM 0x8F93
GL_R8_SNORM 0x8F94
GL_RG8_SNORM 0x8F95
GL_RGB8_SNORM 0x8F96
GL_RGBA8_SNORM 0x8F97
GL_R16_SNORM 0x8F98
GL_RG16_SNORM 0x8F99
GL_RGB16_SNORM 0x8F9A
GL_RGBA16_SNORM 0x8F9B
GL_SIGNED_NORMALIZED 0x8F9C
GL_PRIMITIVE_RESTART 0x8F9D
GL_PRIMITIVE_RESTART_INDEX 0x8F9E""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawArraysInstanced( mode,first,count,primcount ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glDrawElementsInstanced( mode,count,type,indices,primcount ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glTexBuffer( target,internalformat,buffer ):pass
@_f
@_p.types(None,_cs.GLuint)
def glPrimitiveRestartIndex( index ):pass


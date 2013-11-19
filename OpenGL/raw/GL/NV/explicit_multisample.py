'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_explicit_multisample'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_explicit_multisample')
GL_INT_SAMPLER_RENDERBUFFER_NV=_C('GL_INT_SAMPLER_RENDERBUFFER_NV',0x8E57)
GL_MAX_SAMPLE_MASK_WORDS_NV=_C('GL_MAX_SAMPLE_MASK_WORDS_NV',0x8E59)
GL_SAMPLER_RENDERBUFFER_NV=_C('GL_SAMPLER_RENDERBUFFER_NV',0x8E56)
GL_SAMPLE_MASK_NV=_C('GL_SAMPLE_MASK_NV',0x8E51)
GL_SAMPLE_MASK_VALUE_NV=_C('GL_SAMPLE_MASK_VALUE_NV',0x8E52)
GL_SAMPLE_POSITION_NV=_C('GL_SAMPLE_POSITION_NV',0x8E50)
GL_TEXTURE_BINDING_RENDERBUFFER_NV=_C('GL_TEXTURE_BINDING_RENDERBUFFER_NV',0x8E53)
GL_TEXTURE_RENDERBUFFER_DATA_STORE_BINDING_NV=_C('GL_TEXTURE_RENDERBUFFER_DATA_STORE_BINDING_NV',0x8E54)
GL_TEXTURE_RENDERBUFFER_NV=_C('GL_TEXTURE_RENDERBUFFER_NV',0x8E55)
GL_UNSIGNED_INT_SAMPLER_RENDERBUFFER_NV=_C('GL_UNSIGNED_INT_SAMPLER_RENDERBUFFER_NV',0x8E58)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLfloatArray)
def glGetMultisamplefvNV(pname,index,val):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLbitfield)
def glSampleMaskIndexedNV(index,mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glTexRenderbufferNV(target,renderbuffer):pass

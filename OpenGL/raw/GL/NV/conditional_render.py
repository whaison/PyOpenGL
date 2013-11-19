'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_conditional_render'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_conditional_render')
GL_QUERY_BY_REGION_NO_WAIT_NV=_C('GL_QUERY_BY_REGION_NO_WAIT_NV',0x8E16)
GL_QUERY_BY_REGION_WAIT_NV=_C('GL_QUERY_BY_REGION_WAIT_NV',0x8E15)
GL_QUERY_NO_WAIT_NV=_C('GL_QUERY_NO_WAIT_NV',0x8E14)
GL_QUERY_WAIT_NV=_C('GL_QUERY_WAIT_NV',0x8E13)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBeginConditionalRenderNV(id,mode):pass
@_f
@_p.types(None,)
def glEndConditionalRenderNV():pass

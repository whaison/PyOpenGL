'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_stencil_two_side'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_stencil_two_side')
GL_ACTIVE_STENCIL_FACE_EXT=_C('GL_ACTIVE_STENCIL_FACE_EXT',0x8911)
GL_STENCIL_TEST_TWO_SIDE_EXT=_C('GL_STENCIL_TEST_TWO_SIDE_EXT',0x8910)
@_f
@_p.types(None,_cs.GLenum)
def glActiveStencilFaceEXT(face):pass

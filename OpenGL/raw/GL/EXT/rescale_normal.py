'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_rescale_normal'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_rescale_normal')
GL_RESCALE_NORMAL_EXT=_C('GL_RESCALE_NORMAL_EXT',0x803A)


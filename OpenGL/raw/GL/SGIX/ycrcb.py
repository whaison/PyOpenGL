'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIX_ycrcb'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_ycrcb')
GL_YCRCB_422_SGIX=_C('GL_YCRCB_422_SGIX',0x81BB)
GL_YCRCB_444_SGIX=_C('GL_YCRCB_444_SGIX',0x81BC)


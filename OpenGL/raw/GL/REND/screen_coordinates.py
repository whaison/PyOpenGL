'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_REND_screen_coordinates'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_REND_screen_coordinates')
GL_INVERTED_SCREEN_W_REND=_C('GL_INVERTED_SCREEN_W_REND',0x8491)
GL_SCREEN_COORDINATES_REND=_C('GL_SCREEN_COORDINATES_REND',0x8490)


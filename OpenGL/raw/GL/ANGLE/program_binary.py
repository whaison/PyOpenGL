'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ANGLE_program_binary'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ANGLE_program_binary')
GL_PROGRAM_BINARY_ANGLE=_C('GL_PROGRAM_BINARY_ANGLE',0x93A6)


'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ATI_text_fragment_shader'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_text_fragment_shader')
GL_TEXT_FRAGMENT_SHADER_ATI=_C('GL_TEXT_FRAGMENT_SHADER_ATI',0x8200)


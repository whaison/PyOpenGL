'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_texture_compression_latc'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_texture_compression_latc')
GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT=_C('GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT',0x8C72)
GL_COMPRESSED_LUMINANCE_LATC1_EXT=_C('GL_COMPRESSED_LUMINANCE_LATC1_EXT',0x8C70)
GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT=_C('GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT',0x8C73)
GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT=_C('GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT',0x8C71)


'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_S3_s3tc'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_S3_s3tc')
GL_RGB4_S3TC=_C('GL_RGB4_S3TC',0x83A1)
GL_RGBA4_DXT5_S3TC=_C('GL_RGBA4_DXT5_S3TC',0x83A5)
GL_RGBA4_S3TC=_C('GL_RGBA4_S3TC',0x83A3)
GL_RGBA_DXT5_S3TC=_C('GL_RGBA_DXT5_S3TC',0x83A4)
GL_RGBA_S3TC=_C('GL_RGBA_S3TC',0x83A2)
GL_RGB_S3TC=_C('GL_RGB_S3TC',0x83A0)


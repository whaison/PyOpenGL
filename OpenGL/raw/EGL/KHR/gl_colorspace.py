'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_KHR_gl_colorspace'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_gl_colorspace')
EGL_GL_COLORSPACE_KHR=_C('EGL_GL_COLORSPACE_KHR',0x309D)
EGL_GL_COLORSPACE_LINEAR_KHR=_C('EGL_GL_COLORSPACE_LINEAR_KHR',0x308A)
EGL_GL_COLORSPACE_SRGB_KHR=_C('EGL_GL_COLORSPACE_SRGB_KHR',0x3089)


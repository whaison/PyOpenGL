'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIS_pixel_texture'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIS_pixel_texture')
GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS=_C('GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS',0x8355)
GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS=_C('GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS',0x8354)
GL_PIXEL_GROUP_COLOR_SGIS=_C('GL_PIXEL_GROUP_COLOR_SGIS',0x8356)
GL_PIXEL_TEXTURE_SGIS=_C('GL_PIXEL_TEXTURE_SGIS',0x8353)
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetPixelTexGenParameterfvSGIS(pname,params):pass
# Calculate length of params from pname:PixelTexGenParameterNameSGIS
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glGetPixelTexGenParameterivSGIS(pname,params):pass
# Calculate length of params from pname:PixelTexGenParameterNameSGIS
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPixelTexGenParameterfSGIS(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPixelTexGenParameterfvSGIS(pname,params):pass
# Calculate length of params from pname:PixelTexGenParameterNameSGIS
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPixelTexGenParameteriSGIS(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glPixelTexGenParameterivSGIS(pname,params):pass
# Calculate length of params from pname:PixelTexGenParameterNameSGIS

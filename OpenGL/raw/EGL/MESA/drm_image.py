'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.EGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_MESA_drm_image'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_MESA_drm_image')
EGL_DRM_BUFFER_FORMAT_ARGB32_MESA=_C('EGL_DRM_BUFFER_FORMAT_ARGB32_MESA',0x31D2)
EGL_DRM_BUFFER_FORMAT_MESA=_C('EGL_DRM_BUFFER_FORMAT_MESA',0x31D0)
EGL_DRM_BUFFER_MESA=_C('EGL_DRM_BUFFER_MESA',0x31D3)
EGL_DRM_BUFFER_STRIDE_MESA=_C('EGL_DRM_BUFFER_STRIDE_MESA',0x31D4)
EGL_DRM_BUFFER_USE_MESA=_C('EGL_DRM_BUFFER_USE_MESA',0x31D1)
EGL_DRM_BUFFER_USE_SCANOUT_MESA=_C('EGL_DRM_BUFFER_USE_SCANOUT_MESA',0x00000001)
EGL_DRM_BUFFER_USE_SHARE_MESA=_C('EGL_DRM_BUFFER_USE_SHARE_MESA',0x00000002)
@_f
@_p.types(_cs.EGLImageKHR,_cs.EGLDisplay,arrays.GLintArray)
def eglCreateDRMImageMESA(dpy,attrib_list):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLImageKHR,arrays.GLintArray,arrays.GLintArray,arrays.GLintArray)
def eglExportDRMImageMESA(dpy,image,name,handle,stride):pass

'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.EGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_KHR_cl_event'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_cl_event')
EGL_CL_EVENT_HANDLE_KHR=_C('EGL_CL_EVENT_HANDLE_KHR',0x309C)
EGL_SYNC_CL_EVENT_COMPLETE_KHR=_C('EGL_SYNC_CL_EVENT_COMPLETE_KHR',0x30FF)
EGL_SYNC_CL_EVENT_KHR=_C('EGL_SYNC_CL_EVENT_KHR',0x30FE)


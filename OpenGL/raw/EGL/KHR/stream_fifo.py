'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.EGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_KHR_stream_fifo'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_stream_fifo')
EGL_STREAM_FIFO_LENGTH_KHR=_C('EGL_STREAM_FIFO_LENGTH_KHR',0x31FC)
EGL_STREAM_TIME_CONSUMER_KHR=_C('EGL_STREAM_TIME_CONSUMER_KHR',0x31FE)
EGL_STREAM_TIME_NOW_KHR=_C('EGL_STREAM_TIME_NOW_KHR',0x31FD)
EGL_STREAM_TIME_PRODUCER_KHR=_C('EGL_STREAM_TIME_PRODUCER_KHR',0x31FF)
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLStreamKHR,_cs.EGLenum,arrays.GLuint64Array)
def eglQueryStreamTimeKHR(dpy,stream,attribute,value):pass

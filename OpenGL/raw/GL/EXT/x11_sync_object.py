'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_x11_sync_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_x11_sync_object')
GL_SYNC_X11_FENCE_EXT=_C('GL_SYNC_X11_FENCE_EXT',0x90E1)
@_f
@_p.types(_cs.GLsync,_cs.GLenum,_cs.GLintptr,_cs.GLbitfield)
def glImportSyncEXT(external_sync_type,external_sync,flags):pass

'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GLX import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLX_SGIX_swap_group'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_SGIX_swap_group')

@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXDrawable,_cs.GLXDrawable)
def glXJoinSwapGroupSGIX(dpy,drawable,member):pass

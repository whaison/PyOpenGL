'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_EXT_pixel_format'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_pixel_format')
WGL_ACCELERATION_EXT=_C('WGL_ACCELERATION_EXT',0x2003)
WGL_ACCUM_ALPHA_BITS_EXT=_C('WGL_ACCUM_ALPHA_BITS_EXT',0x2021)
WGL_ACCUM_BITS_EXT=_C('WGL_ACCUM_BITS_EXT',0x201D)
WGL_ACCUM_BLUE_BITS_EXT=_C('WGL_ACCUM_BLUE_BITS_EXT',0x2020)
WGL_ACCUM_GREEN_BITS_EXT=_C('WGL_ACCUM_GREEN_BITS_EXT',0x201F)
WGL_ACCUM_RED_BITS_EXT=_C('WGL_ACCUM_RED_BITS_EXT',0x201E)
WGL_ALPHA_BITS_EXT=_C('WGL_ALPHA_BITS_EXT',0x201B)
WGL_ALPHA_SHIFT_EXT=_C('WGL_ALPHA_SHIFT_EXT',0x201C)
WGL_AUX_BUFFERS_EXT=_C('WGL_AUX_BUFFERS_EXT',0x2024)
WGL_BLUE_BITS_EXT=_C('WGL_BLUE_BITS_EXT',0x2019)
WGL_BLUE_SHIFT_EXT=_C('WGL_BLUE_SHIFT_EXT',0x201A)
WGL_COLOR_BITS_EXT=_C('WGL_COLOR_BITS_EXT',0x2014)
WGL_DEPTH_BITS_EXT=_C('WGL_DEPTH_BITS_EXT',0x2022)
WGL_DOUBLE_BUFFER_EXT=_C('WGL_DOUBLE_BUFFER_EXT',0x2011)
WGL_DRAW_TO_BITMAP_EXT=_C('WGL_DRAW_TO_BITMAP_EXT',0x2002)
WGL_DRAW_TO_WINDOW_EXT=_C('WGL_DRAW_TO_WINDOW_EXT',0x2001)
WGL_FULL_ACCELERATION_EXT=_C('WGL_FULL_ACCELERATION_EXT',0x2027)
WGL_GENERIC_ACCELERATION_EXT=_C('WGL_GENERIC_ACCELERATION_EXT',0x2026)
WGL_GREEN_BITS_EXT=_C('WGL_GREEN_BITS_EXT',0x2017)
WGL_GREEN_SHIFT_EXT=_C('WGL_GREEN_SHIFT_EXT',0x2018)
WGL_NEED_PALETTE_EXT=_C('WGL_NEED_PALETTE_EXT',0x2004)
WGL_NEED_SYSTEM_PALETTE_EXT=_C('WGL_NEED_SYSTEM_PALETTE_EXT',0x2005)
WGL_NO_ACCELERATION_EXT=_C('WGL_NO_ACCELERATION_EXT',0x2025)
WGL_NUMBER_OVERLAYS_EXT=_C('WGL_NUMBER_OVERLAYS_EXT',0x2008)
WGL_NUMBER_PIXEL_FORMATS_EXT=_C('WGL_NUMBER_PIXEL_FORMATS_EXT',0x2000)
WGL_NUMBER_UNDERLAYS_EXT=_C('WGL_NUMBER_UNDERLAYS_EXT',0x2009)
WGL_PIXEL_TYPE_EXT=_C('WGL_PIXEL_TYPE_EXT',0x2013)
WGL_RED_BITS_EXT=_C('WGL_RED_BITS_EXT',0x2015)
WGL_RED_SHIFT_EXT=_C('WGL_RED_SHIFT_EXT',0x2016)
WGL_SHARE_ACCUM_EXT=_C('WGL_SHARE_ACCUM_EXT',0x200E)
WGL_SHARE_DEPTH_EXT=_C('WGL_SHARE_DEPTH_EXT',0x200C)
WGL_SHARE_STENCIL_EXT=_C('WGL_SHARE_STENCIL_EXT',0x200D)
WGL_STENCIL_BITS_EXT=_C('WGL_STENCIL_BITS_EXT',0x2023)
WGL_STEREO_EXT=_C('WGL_STEREO_EXT',0x2012)
WGL_SUPPORT_GDI_EXT=_C('WGL_SUPPORT_GDI_EXT',0x200F)
WGL_SUPPORT_OPENGL_EXT=_C('WGL_SUPPORT_OPENGL_EXT',0x2010)
WGL_SWAP_COPY_EXT=_C('WGL_SWAP_COPY_EXT',0x2029)
WGL_SWAP_EXCHANGE_EXT=_C('WGL_SWAP_EXCHANGE_EXT',0x2028)
WGL_SWAP_LAYER_BUFFERS_EXT=_C('WGL_SWAP_LAYER_BUFFERS_EXT',0x2006)
WGL_SWAP_METHOD_EXT=_C('WGL_SWAP_METHOD_EXT',0x2007)
WGL_SWAP_UNDEFINED_EXT=_C('WGL_SWAP_UNDEFINED_EXT',0x202A)
WGL_TRANSPARENT_EXT=_C('WGL_TRANSPARENT_EXT',0x200A)
WGL_TRANSPARENT_VALUE_EXT=_C('WGL_TRANSPARENT_VALUE_EXT',0x200B)
WGL_TYPE_COLORINDEX_EXT=_C('WGL_TYPE_COLORINDEX_EXT',0x202C)
WGL_TYPE_RGBA_EXT=_C('WGL_TYPE_RGBA_EXT',0x202B)
@_f
@_p.types(_cs.BOOL,_cs.HDC,ctypes.POINTER(_cs.c_int),ctypes.POINTER(_cs.FLOAT),_cs.UINT,ctypes.POINTER(_cs.c_int),ctypes.POINTER(_cs.UINT))
def wglChoosePixelFormatEXT(hdc,piAttribIList,pfAttribFList,nMaxFormats,piFormats,nNumFormats):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.c_int,_cs.c_int,_cs.UINT,ctypes.POINTER(_cs.c_int),ctypes.POINTER(_cs.FLOAT))
def wglGetPixelFormatAttribfvEXT(hdc,iPixelFormat,iLayerPlane,nAttributes,piAttributes,pfValues):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.c_int,_cs.c_int,_cs.UINT,ctypes.POINTER(_cs.c_int),ctypes.POINTER(_cs.c_int))
def wglGetPixelFormatAttribivEXT(hdc,iPixelFormat,iLayerPlane,nAttributes,piAttributes,piValues):pass

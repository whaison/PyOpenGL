'''OpenGL extension ATI.pixel_format_float

This module customises the behaviour of the 
OpenGL.raw.WGL.ATI.pixel_format_float to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds pixel formats with floating-point RGBA color
	components.
	
	The size of each float components is specified using the same
	WGL_RED_BITS_ARB, WGL_GREEN_BITS_ARB, WGL_BLUE_BITS_ARB and
	WGL_ALPHA_BITS_ARB pixel format attributes that are used for
	defining the size of fixed-point components.  32 bit floating-
	point components are in the standard IEEE float format.  16 bit
	floating-point components have 1 sign bit, 5 exponent bits,
	and 10 mantissa bits. 
	
	In standard OpenGL RGBA color components are normally clamped to
	the range [0,1].  The color components of a float buffer are
	clamped to the limits of the range representable by their format.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ATI/pixel_format_float.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.ATI.pixel_format_float import *
from OpenGL.raw.WGL.ATI.pixel_format_float import _EXTENSION_NAME

def glInitPixelFormatFloatATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
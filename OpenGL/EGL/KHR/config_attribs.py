'''OpenGL extension KHR.config_attribs

This module customises the behaviour of the 
OpenGL.raw.EGL.KHR.config_attribs to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/config_attribs.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.EGL.KHR.config_attribs import *

def glInitConfigAttribsKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
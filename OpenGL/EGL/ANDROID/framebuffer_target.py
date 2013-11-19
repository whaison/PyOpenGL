'''OpenGL extension ANDROID.framebuffer_target

This module customises the behaviour of the 
OpenGL.raw.EGL.ANDROID.framebuffer_target to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANDROID/framebuffer_target.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.EGL.ANDROID.framebuffer_target import *

def glInitFramebufferTargetANDROID():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
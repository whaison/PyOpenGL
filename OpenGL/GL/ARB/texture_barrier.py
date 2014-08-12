'''OpenGL extension ARB.texture_barrier

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_barrier to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_barrier.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.texture_barrier import *
from OpenGL.raw.GL.ARB.texture_barrier import _EXTENSION_NAME

def glInitTextureBarrierARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
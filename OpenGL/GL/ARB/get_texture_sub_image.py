'''OpenGL extension ARB.get_texture_sub_image

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.get_texture_sub_image to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/get_texture_sub_image.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.get_texture_sub_image import *
from OpenGL.raw.GL.ARB.get_texture_sub_image import _EXTENSION_NAME

def glInitGetTextureSubImageARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
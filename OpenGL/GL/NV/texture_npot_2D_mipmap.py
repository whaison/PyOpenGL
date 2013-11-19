'''OpenGL extension NV.texture_npot_2D_mipmap

This module customises the behaviour of the 
OpenGL.raw.GL.NV.texture_npot_2D_mipmap to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/texture_npot_2D_mipmap.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.texture_npot_2D_mipmap import *

def glInitTextureNpot2DMipmapNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
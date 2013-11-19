'''OpenGL extension OES.texture_cube_map

This module customises the behaviour of the 
OpenGL.raw.GL.OES.texture_cube_map to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/texture_cube_map.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.OES.texture_cube_map import *

def glInitTextureCubeMapOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
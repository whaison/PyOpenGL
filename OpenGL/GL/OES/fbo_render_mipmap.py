'''OpenGL extension OES.fbo_render_mipmap

This module customises the behaviour of the 
OpenGL.raw.GL.OES.fbo_render_mipmap to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/fbo_render_mipmap.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.OES.fbo_render_mipmap import *

def glInitFboRenderMipmapOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
'''OpenGL extension I3D.swap_frame_lock

This module customises the behaviour of the 
OpenGL.raw.WGL.I3D.swap_frame_lock to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/I3D/swap_frame_lock.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.WGL.I3D.swap_frame_lock import *

def glInitSwapFrameLockI3D():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
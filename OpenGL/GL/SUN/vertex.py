'''OpenGL extension SUN.vertex

This module customises the behaviour of the 
OpenGL.raw.GL.SUN.vertex to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides new GL commands to specify vertex data such as 
	color and normal along with the vertex in one single GL command in order to
	minimize the overhead in making GL commands for each set of vertex data.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SUN/vertex.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SUN.vertex import *

def glInitVertexSUN():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
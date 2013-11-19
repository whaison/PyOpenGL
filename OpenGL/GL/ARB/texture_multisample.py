'''OpenGL extension ARB.texture_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides support for two new types of "multisample
	textures" - two-dimensional and two-dimensional array - as well as
	mechanisms to fetch a specific sample from such a texture in a shader,
	and to attach such textures to FBOs for rendering.
	
	This extension also includes the following functionality, first described
	in NV_explicit_multisample:
	
	 * A query in the API to query the location of samples within the pixel
	
	 * An explicit control for the multisample sample mask to augment the
	   control provided by SampleCoverage

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_multisample.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.texture_multisample import *

def glInitTextureMultisampleARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
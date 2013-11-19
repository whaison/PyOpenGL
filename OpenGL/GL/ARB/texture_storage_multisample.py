'''OpenGL extension ARB.texture_storage_multisample

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_storage_multisample to provide a more 
Python-friendly API

Overview (from the spec)
	
	The ARB_texture_storage extension and OpenGL 4.2 introduced the concept
	of immutable texture objects. With these objects, once their data store
	has been sized and allocated, it could not be resized for the lifetime
	of the objects (although its content could be updated). OpenGL
	implementations may be able to take advantage of the knowledge that the
	underlying data store of certain objects cannot be deleted or otherwise
	reallocated without destruction of the whole object (normally, a much
	heavier weight and less frequent operation). Immutable storage
	for all types of textures besides multisample and buffer textures was
	introduced by ARB_texture_storage. For completeness, this extension
	introduces immutable storage for multisampled textures.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_storage_multisample.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.texture_storage_multisample import *

def glInitTextureStorageMultisampleARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
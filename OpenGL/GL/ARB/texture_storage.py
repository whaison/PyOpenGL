'''OpenGL extension ARB.texture_storage

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_storage to provide a more 
Python-friendly API

Overview (from the spec)
	
	The texture image specification commands in OpenGL allow each level
	to be separately specified with different sizes, formats, types and
	so on, and only imposes consistency checks at draw time. This adds
	overhead for implementations.
	
	This extension provides a mechanism for specifying the entire
	structure of a texture in a single call, allowing certain
	consistency checks and memory allocations to be done up front. Once
	specified, the format and dimensions of the image array become
	immutable, to simplify completeness checks in the implementation.
	
	When using this extension, it is no longer possible to supply texture
	data using TexImage*. Instead, data can be uploaded using TexSubImage*,
	or produced by other means (such as render-to-texture, mipmap generation,
	or rendering to a sibling EGLImage).
	
	This extension has complicated interactions with other extensions.
	The goal of most of these interactions is to ensure that a texture
	is always mipmap complete (and cube complete for cubemap textures).

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_storage.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.texture_storage import *

def glInitTextureStorageARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
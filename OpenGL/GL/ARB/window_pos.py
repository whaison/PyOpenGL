'''OpenGL extension ARB.window_pos

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.window_pos to provide a more 
Python-friendly API

Overview (from the spec)
	
	In order to set the current raster position to a specific window
	coordinate with the RasterPos command, the modelview matrix, projection
	matrix and viewport must be set very carefully.  Furthermore, if the
	desired window coordinate is outside of the window's bounds one must rely
	on a subtle side-effect of the Bitmap command in order to avoid frustum
	clipping.
	
	This extension provides a set of functions to directly set the current
	raster position in window coordinates, bypassing the modelview matrix, the
	projection matrix and the viewport-to-window mapping.  Furthermore, clip
	testing is not performed, so that the current raster position is always
	valid.
	
	This greatly simplifies the process of setting the current raster position
	to a specific window coordinate prior to calling DrawPixels, CopyPixels or
	Bitmap.  Many matrix operations can be avoided when mixing 2D and 3D
	rendering.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/window_pos.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.window_pos import *

def glInitWindowPosARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
glWindowPos2dvARB = arrays.setInputArraySizeType(
    glWindowPos2dvARB,
    2,
    arrays.GLdoubleArray,
    'v',
)
glWindowPos2fvARB = arrays.setInputArraySizeType(
    glWindowPos2fvARB,
    2,
    arrays.GLfloatArray,
    'v',
)
glWindowPos2ivARB = arrays.setInputArraySizeType(
    glWindowPos2ivARB,
    2,
    arrays.GLintArray,
    'v',
)
glWindowPos2svARB = arrays.setInputArraySizeType(
    glWindowPos2svARB,
    2,
    arrays.GLshortArray,
    'v',
)
glWindowPos3dvARB = arrays.setInputArraySizeType(
    glWindowPos3dvARB,
    3,
    arrays.GLdoubleArray,
    'v',
)
glWindowPos3fvARB = arrays.setInputArraySizeType(
    glWindowPos3fvARB,
    3,
    arrays.GLfloatArray,
    'v',
)
glWindowPos3ivARB = arrays.setInputArraySizeType(
    glWindowPos3ivARB,
    3,
    arrays.GLintArray,
    'v',
)
glWindowPos3svARB = arrays.setInputArraySizeType(
    glWindowPos3svARB,
    3,
    arrays.GLshortArray,
    'v',
)
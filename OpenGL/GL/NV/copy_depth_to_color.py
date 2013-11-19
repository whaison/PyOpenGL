'''OpenGL extension NV.copy_depth_to_color

This module customises the behaviour of the 
OpenGL.raw.GL.NV.copy_depth_to_color to provide a more 
Python-friendly API

Overview (from the spec)
	
	Some applications, especially systems for distributed OpenGL
	rendering, would like to have a fast way of copying their depth
	buffer into a color buffer; for example, this allows the depth buffer
	to be scanned out, allowing downstream compositing operations.
	
	To do this operation in unextended OpenGL, the app must use
	glReadPixels of GL_DEPTH_COMPONENT data, followed by glDrawPixels of
	RGBA data.  However, this typically will not provide adequate
	performance.
	
	This extension provides a way to copy the depth data directly into
	the color buffer, by adding two new options for the "type" parameter
	of glCopyPixels: GL_DEPTH_STENCIL_TO_RGBA_NV and
	GL_DEPTH_STENCIL_TO_BGRA_NV.
	
	Typically, OpenGL implementations support many more bits of depth
	precision than color precision per channel.  On many PC platforms, it
	is common, for example, to have 24 bits of depth, 8 bits of stencil,
	and 8 bits of red, green, blue, and alpha.
	
	In such a framebuffer configuration, the most effective way to copy
	the data without this extension would be to perform a glReadPixels of
	GL_UNSIGNED_INT_24_8_NV/GL_DEPTH_STENCIL_NV (using the existing
	NV_packed_depth_stencil extension), followed by a glDrawPixels of
	GL_UNSIGNED_INT_8_8_8_8/GL_RGBA or GL_BGRA data.  This places the
	depth data in the color channels and the stencil data in the alpha
	channel.
	
	This extension's new operations concatenates these two operations,
	providing a CopyPixels command that does both of these steps in one.
	This provides a large performance speedup, since no pixel data must
	be transfered across the bus.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/copy_depth_to_color.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.copy_depth_to_color import *

def glInitCopyDepthToColorNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
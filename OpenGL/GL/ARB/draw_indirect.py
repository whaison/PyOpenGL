'''OpenGL extension ARB.draw_indirect

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.draw_indirect to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism for supplying the arguments to a 
	DrawArraysInstanced or DrawElementsInstancedBaseVertex from buffer object
	memory. This is not particularly useful for applications where the CPU 
	knows the values of the arguments beforehand, but is helpful when the 
	values will be generated on the GPU through any mechanism that can write
	to a buffer object including image stores, atomic counters, or compute
	interop. This allows the GPU to consume these arguments without a round-
	trip to the CPU or the expensive synchronization that would involve. This
	is similar to the DrawTransformFeedbackEXT command from 
	EXT_transform_feedback2, but offers much more flexibility in both 
	generating the arguments and in the type of Draws that can be accomplished.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/draw_indirect.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.draw_indirect import *

def glInitDrawIndirectARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
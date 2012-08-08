'''OpenGL extension ARB.ES3_compatibility

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.ES3_compatibility to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds support for features of OpenGL ES 3.0 that are
	missing from OpenGL 3.x. Enabling these features will ease the process
	of porting applications from OpenGL ES 3.0 to OpenGL. These features
	include conservative boolean occlusion queries, primitive restart with a
	fixed index, the OpenGL ES Shading Language 3.00 specification, and the
	dependencies stated above.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/ES3_compatibility.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.ES3_compatibility import *
### END AUTOGENERATED SECTION
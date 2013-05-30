'''OpenGL extension OES.compressed_paletted_texture

This module customises the behaviour of the 
OpenGL.raw.GL.OES.compressed_paletted_texture to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/compressed_paletted_texture.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.OES.compressed_paletted_texture import *
### END AUTOGENERATED SECTION
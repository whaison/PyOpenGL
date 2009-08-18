'''OpenGL extension ARB.draw_elements_base_vertex

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.draw_elements_base_vertex to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.draw_elements_base_vertex import *
### END AUTOGENERATED SECTION
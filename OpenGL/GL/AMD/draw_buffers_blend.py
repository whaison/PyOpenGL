'''OpenGL extension AMD.draw_buffers_blend

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.draw_buffers_blend to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.draw_buffers_blend import *
### END AUTOGENERATED SECTION
'''OpenGL extension SGI.depth_pass_instrument

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGI/depth_pass_instrument.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGI_depth_pass_instrument'
_DEPRECATED = False
GL_DEPTH_PASS_INSTRUMENT_SGIX = constant.Constant( 'GL_DEPTH_PASS_INSTRUMENT_SGIX', 0x8310 )
GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX = constant.Constant( 'GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX', 0x8311 )
GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX = constant.Constant( 'GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX', 0x8312 )


def glInitDepthPassInstrumentSGI():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
'''OpenGL extension SGIX.flush_raster

Overview (from the spec)
    
    This extensions provides a way to ensure that all raster operations 
    currently in the pipeline will be completed before the next 
    raster operation begins. We define a raster operation as an operation
    that involves the rasterization stage of the OpenGL pipeline.
    The implementation is free to decide what consitutes flushing the
    raster subsystem.
    
    The motivation is to allow accurate instrumentation by 
    including this call before stopping rasterization measurements.
    There are cases where Finish() is used, but a FlushRaster()
    would suffice, so this extension is deliberately kept independent 
    of the instruments extension.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/flush_raster.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_flush_raster'
_DEPRECATED = False

glFlushRasterSGIX = platform.createExtensionFunction( 
'glFlushRasterSGIX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glFlushRasterSGIX() -> None',
argNames=(),
deprecated=_DEPRECATED,
)


def glInitFlushRasterSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
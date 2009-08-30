'''OpenGL extension NV.light_max_exponent

Overview (from the spec)
    
    Default OpenGL does not permit a shininess or spot exponent over
    128.0.  This extension permits implementations to support and
    advertise a maximum shininess and spot exponent beyond 128.0.
    
    Note that extremely high exponents for shininess and/or spot light
    cutoff will require sufficiently high tessellation for acceptable
    lighting results.
    
    Paul Deifenbach's thesis suggests that higher exponents are
    necessary to approximate BRDFs with per-vertex ligthing and
    multiple passes.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/NV/light_max_exponent.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_light_max_exponent'
_DEPRECATED = False
GL_MAX_SHININESS_NV = constant.Constant( 'GL_MAX_SHININESS_NV', 0x8504 )
glget.addGLGetConstant( GL_MAX_SHININESS_NV, (1,) )
GL_MAX_SPOT_EXPONENT_NV = constant.Constant( 'GL_MAX_SPOT_EXPONENT_NV', 0x8505 )
glget.addGLGetConstant( GL_MAX_SPOT_EXPONENT_NV, (1,) )


def glInitLightMaxExponentNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
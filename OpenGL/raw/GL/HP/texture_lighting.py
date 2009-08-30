'''OpenGL extension HP.texture_lighting

Overview (from the spec)
    
    This extension defines a mechanism for applications to request
    that color originating from specular lighting be added to
    the fragment color _after_ texture application.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/HP/texture_lighting.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_HP_texture_lighting'
_DEPRECATED = False
GL_TEXTURE_LIGHTING_MODE_HP = constant.Constant( 'GL_TEXTURE_LIGHTING_MODE_HP', 0x8167 )
GL_TEXTURE_POST_SPECULAR_HP = constant.Constant( 'GL_TEXTURE_POST_SPECULAR_HP', 0x8168 )
GL_TEXTURE_PRE_SPECULAR_HP = constant.Constant( 'GL_TEXTURE_PRE_SPECULAR_HP', 0x8169 )


def glInitTextureLightingHP():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
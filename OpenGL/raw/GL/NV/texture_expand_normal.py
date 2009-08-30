'''OpenGL extension NV.texture_expand_normal

Overview (from the spec)
    
    This extension provides a remapping mode where unsigned texture
    components (in the range [0,1]) can be treated as though they
    contained signed data (in the range [-1,+1]).  This allows
    applications to easily encode signed data into unsigned texture
    formats.
    
    The functionality of this extension is nearly identical to the
    EXPAND_NORMAL_NV remapping mode provided in the NV_register_combiners
    extension, although it applies even if register combiners are used.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_expand_normal.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_texture_expand_normal'
_DEPRECATED = False
GL_TEXTURE_UNSIGNED_REMAP_MODE_NV = constant.Constant( 'GL_TEXTURE_UNSIGNED_REMAP_MODE_NV', 0x888F )


def glInitTextureExpandNormalNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
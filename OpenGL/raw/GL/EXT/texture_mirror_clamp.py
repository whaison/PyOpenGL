'''OpenGL extension EXT.texture_mirror_clamp

Overview (from the spec)
	
	EXT_texture_mirror_clamp extends the set of texture wrap modes to
	include three modes (GL_MIRROR_CLAMP_EXT, GL_MIRROR_CLAMP_TO_EDGE_EXT,
	GL_MIRROR_CLAMP_TO_BORDER_EXT) that effectively use a texture map
	twice as large as the original image in which the additional half
	of the new image is a mirror image of the original image.
	
	This new mode relaxes the need to generate images whose opposite
	edges match by using the original image to generate a matching
	"mirror image".  This mode allows the texture to be mirrored only
	once in the negative s, t, and r directions.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_mirror_clamp.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_mirror_clamp'
_DEPRECATED = False
GL_MIRROR_CLAMP_EXT = constant.Constant( 'GL_MIRROR_CLAMP_EXT', 0x8742 )
GL_MIRROR_CLAMP_TO_EDGE_EXT = constant.Constant( 'GL_MIRROR_CLAMP_TO_EDGE_EXT', 0x8743 )
GL_MIRROR_CLAMP_TO_BORDER_EXT = constant.Constant( 'GL_MIRROR_CLAMP_TO_BORDER_EXT', 0x8912 )


def glInitTextureMirrorClampEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

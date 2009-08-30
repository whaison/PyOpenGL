'''OpenGL extension EXT.texture_compression_s3tc

Overview (from the spec)
    
    This extension provides additional texture compression functionality
    specific to S3's S3TC format (called DXTC in Microsoft's DirectX API),
    subject to all the requirements and limitations described by the extension
    GL_ARB_texture_compression.
    
    This extension supports DXT1, DXT3, and DXT5 texture compression formats.
    For the DXT1 image format, this specification supports an RGB-only mode
    and a special RGBA mode with single-bit "transparent" alpha.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_compression_s3tc.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_compression_s3tc'
_DEPRECATED = False
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = constant.Constant( 'GL_COMPRESSED_RGB_S3TC_DXT1_EXT', 0x83F0 )
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = constant.Constant( 'GL_COMPRESSED_RGBA_S3TC_DXT1_EXT', 0x83F1 )
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = constant.Constant( 'GL_COMPRESSED_RGBA_S3TC_DXT3_EXT', 0x83F2 )
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = constant.Constant( 'GL_COMPRESSED_RGBA_S3TC_DXT5_EXT', 0x83F3 )


def glInitTextureCompressionS3TcEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
'''OpenGL extension ARB.texture_compression_bptc

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_ARB_texture_compression_bptc'
_p.unpack_constants( """GL_COMPRESSED_RGBA_BPTC_UNORM_ARB 0x8E8C
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB 0x8E8D
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB 0x8E8E
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB 0x8E8F""", globals())


def glInitTextureCompressionBptcARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

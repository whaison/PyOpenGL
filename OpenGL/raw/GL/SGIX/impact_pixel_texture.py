'''OpenGL extension SGIX.impact_pixel_texture

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_SGIX_impact_pixel_texture'
_p.unpack_constants( """GL_PIXEL_TEX_GEN_Q_CEILING_SGIX 0x8184
GL_PIXEL_TEX_GEN_Q_ROUND_SGIX 0x8185
GL_PIXEL_TEX_GEN_Q_FLOOR_SGIX 0x8186
GL_PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX 0x8187
GL_PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX 0x8188
GL_PIXEL_TEX_GEN_ALPHA_LS_SGIX 0x8189
GL_PIXEL_TEX_GEN_ALPHA_MS_SGIX 0x818A""", globals())


def glInitImpactPixelTextureSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

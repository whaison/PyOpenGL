'''OpenGL extension EXT.framebuffer_multisample_blit_scaled

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_EXT_framebuffer_multisample_blit_scaled'
_p.unpack_constants( """GL_SCALED_RESOLVE_FASTEST_EXT 0x90BA
GL_SCALED_RESOLVE_NICEST_EXT 0x90BB""", globals())


def glInitFramebufferMultisampleBlitScaledEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

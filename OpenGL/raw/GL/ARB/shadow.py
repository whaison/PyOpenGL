'''OpenGL extension ARB.shadow

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_ARB_shadow'
_p.unpack_constants( """GL_TEXTURE_COMPARE_MODE_ARB 0x884C
GL_TEXTURE_COMPARE_FUNC_ARB 0x884D
GL_COMPARE_R_TO_TEXTURE_ARB 0x884E""", globals())


def glInitShadowARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

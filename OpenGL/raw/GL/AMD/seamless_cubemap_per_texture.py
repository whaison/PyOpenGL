'''OpenGL extension AMD.seamless_cubemap_per_texture

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_AMD_seamless_cubemap_per_texture'



def glInitSeamlessCubemapPerTextureAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

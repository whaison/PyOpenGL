'''OpenGL extension AMD.conservative_depth

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_AMD_conservative_depth'



def glInitConservativeDepthAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

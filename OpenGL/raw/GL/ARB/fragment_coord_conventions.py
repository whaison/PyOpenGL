'''OpenGL extension ARB.fragment_coord_conventions

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_ARB_fragment_coord_conventions'



def glInitFragmentCoordConventionsARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

'''OpenGL extension NV.copy_depth_to_color

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_NV_copy_depth_to_color'
_p.unpack_constants( """GL_DEPTH_STENCIL_TO_RGBA_NV 0x886E
GL_DEPTH_STENCIL_TO_BGRA_NV 0x886F""", globals())


def glInitCopyDepthToColorNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

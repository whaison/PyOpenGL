'''OpenGL extension AMD.transform_feedback3_lines_triangles

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p
EXTENSION_NAME = 'GL_AMD_transform_feedback3_lines_triangles'



def glInitTransformFeedback3LinesTrianglesAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

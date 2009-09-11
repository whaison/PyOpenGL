'''OpenGL extension S3.s3tc

Overview (from the spec)
	
	This extension allows specifying texture data in compressed S3TC
	format.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/S3/s3tc.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_S3_s3tc'
_DEPRECATED = False
GL_RGB_S3TC = constant.Constant( 'GL_RGB_S3TC', 0x83A0 )
GL_RGB4_S3TC = constant.Constant( 'GL_RGB4_S3TC', 0x83A1 )
GL_RGBA_S3TC = constant.Constant( 'GL_RGBA_S3TC', 0x83A2 )
GL_RGBA4_S3TC = constant.Constant( 'GL_RGBA4_S3TC', 0x83A3 )


def glInitS3TcS3():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

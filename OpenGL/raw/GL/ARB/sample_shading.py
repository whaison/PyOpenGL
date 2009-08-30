'''OpenGL extension ARB.sample_shading

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/sample_shading.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_sample_shading'
_DEPRECATED = False
GL_SAMPLE_SHADING = constant.Constant( 'GL_SAMPLE_SHADING', 0x8C36 )
GL_MIN_SAMPLE_SHADING_VALUE = constant.Constant( 'GL_MIN_SAMPLE_SHADING_VALUE', 0x8C37 )
glMinSampleShading = platform.createExtensionFunction( 
'glMinSampleShading',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLclampf,),
doc='glMinSampleShading(GLclampf(value)) -> None',
argNames=('value',),
deprecated=_DEPRECATED,
)


def glInitSampleShadingARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
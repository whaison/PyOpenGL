'''OpenGL extension ARB.sampler_objects

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_sampler_objects'
_DEPRECATED = False
GL_SAMPLER_BINDING = constant.Constant( 'GL_SAMPLER_BINDING', 0x8919 )
glGenSamplers = platform.createExtensionFunction( 
'glGenSamplers',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glGenSamplers(GLsizei(count), GLuintArray(samplers)) -> None',
argNames=('count','samplers',),
deprecated=_DEPRECATED,
)

glDeleteSamplers = platform.createExtensionFunction( 
'glDeleteSamplers',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glDeleteSamplers(GLsizei(count), GLuintArray(samplers)) -> None',
argNames=('count','samplers',),
deprecated=_DEPRECATED,
)

glIsSampler = platform.createExtensionFunction( 
'glIsSampler',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLuint,),
doc='glIsSampler(GLuint(sampler)) -> constants.GLboolean',
argNames=('sampler',),
deprecated=_DEPRECATED,
)

glBindSampler = platform.createExtensionFunction( 
'glBindSampler',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,),
doc='glBindSampler(GLuint(unit), GLuint(sampler)) -> None',
argNames=('unit','sampler',),
deprecated=_DEPRECATED,
)

glSamplerParameteri = platform.createExtensionFunction( 
'glSamplerParameteri',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLint,),
doc='glSamplerParameteri(GLuint(sampler), GLenum(pname), GLint(param)) -> None',
argNames=('sampler','pname','param',),
deprecated=_DEPRECATED,
)

glSamplerParameteriv = platform.createExtensionFunction( 
'glSamplerParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glSamplerParameteriv(GLuint(sampler), GLenum(pname), GLintArray(param)) -> None',
argNames=('sampler','pname','param',),
deprecated=_DEPRECATED,
)

glSamplerParameterf = platform.createExtensionFunction( 
'glSamplerParameterf',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLfloat,),
doc='glSamplerParameterf(GLuint(sampler), GLenum(pname), GLfloat(param)) -> None',
argNames=('sampler','pname','param',),
deprecated=_DEPRECATED,
)

glSamplerParameterfv = platform.createExtensionFunction( 
'glSamplerParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLfloatArray,),
doc='glSamplerParameterfv(GLuint(sampler), GLenum(pname), GLfloatArray(param)) -> None',
argNames=('sampler','pname','param',),
deprecated=_DEPRECATED,
)

glSamplerParameterIiv = platform.createExtensionFunction( 
'glSamplerParameterIiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glSamplerParameterIiv(GLuint(sampler), GLenum(pname), GLintArray(param)) -> None',
argNames=('sampler','pname','param',),
deprecated=_DEPRECATED,
)

glSamplerParameterIuiv = platform.createExtensionFunction( 
'glSamplerParameterIuiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLuintArray,),
doc='glSamplerParameterIuiv(GLuint(sampler), GLenum(pname), GLuintArray(param)) -> None',
argNames=('sampler','pname','param',),
deprecated=_DEPRECATED,
)

glGetSamplerParameteriv = platform.createExtensionFunction( 
'glGetSamplerParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glGetSamplerParameteriv(GLuint(sampler), GLenum(pname), GLintArray(params)) -> None',
argNames=('sampler','pname','params',),
deprecated=_DEPRECATED,
)

glGetSamplerParameterIiv = platform.createExtensionFunction( 
'glGetSamplerParameterIiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glGetSamplerParameterIiv(GLuint(sampler), GLenum(pname), GLintArray(params)) -> None',
argNames=('sampler','pname','params',),
deprecated=_DEPRECATED,
)

glGetSamplerParameterfv = platform.createExtensionFunction( 
'glGetSamplerParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLfloatArray,),
doc='glGetSamplerParameterfv(GLuint(sampler), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('sampler','pname','params',),
deprecated=_DEPRECATED,
)

glGetSamplerParameterIfv = platform.createExtensionFunction( 
'glGetSamplerParameterIfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLfloatArray,),
doc='glGetSamplerParameterIfv(GLuint(sampler), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('sampler','pname','params',),
deprecated=_DEPRECATED,
)


def glInitSamplerObjectsARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

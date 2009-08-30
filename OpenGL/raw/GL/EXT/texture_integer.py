'''OpenGL extension EXT.texture_integer

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_integer.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_integer'
_DEPRECATED = False
GL_RGBA32UI_EXT = constant.Constant( 'GL_RGBA32UI_EXT', 0x8D70 )
GL_RGB32UI_EXT = constant.Constant( 'GL_RGB32UI_EXT', 0x8D71 )
GL_ALPHA32UI_EXT = constant.Constant( 'GL_ALPHA32UI_EXT', 0x8D72 )
GL_INTENSITY32UI_EXT = constant.Constant( 'GL_INTENSITY32UI_EXT', 0x8D73 )
GL_LUMINANCE32UI_EXT = constant.Constant( 'GL_LUMINANCE32UI_EXT', 0x8D74 )
GL_LUMINANCE_ALPHA32UI_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA32UI_EXT', 0x8D75 )
GL_RGBA16UI_EXT = constant.Constant( 'GL_RGBA16UI_EXT', 0x8D76 )
GL_RGB16UI_EXT = constant.Constant( 'GL_RGB16UI_EXT', 0x8D77 )
GL_ALPHA16UI_EXT = constant.Constant( 'GL_ALPHA16UI_EXT', 0x8D78 )
GL_INTENSITY16UI_EXT = constant.Constant( 'GL_INTENSITY16UI_EXT', 0x8D79 )
GL_LUMINANCE16UI_EXT = constant.Constant( 'GL_LUMINANCE16UI_EXT', 0x8D7A )
GL_LUMINANCE_ALPHA16UI_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA16UI_EXT', 0x8D7B )
GL_RGBA8UI_EXT = constant.Constant( 'GL_RGBA8UI_EXT', 0x8D7C )
GL_RGB8UI_EXT = constant.Constant( 'GL_RGB8UI_EXT', 0x8D7D )
GL_ALPHA8UI_EXT = constant.Constant( 'GL_ALPHA8UI_EXT', 0x8D7E )
GL_INTENSITY8UI_EXT = constant.Constant( 'GL_INTENSITY8UI_EXT', 0x8D7F )
GL_LUMINANCE8UI_EXT = constant.Constant( 'GL_LUMINANCE8UI_EXT', 0x8D80 )
GL_LUMINANCE_ALPHA8UI_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA8UI_EXT', 0x8D81 )
GL_RGBA32I_EXT = constant.Constant( 'GL_RGBA32I_EXT', 0x8D82 )
GL_RGB32I_EXT = constant.Constant( 'GL_RGB32I_EXT', 0x8D83 )
GL_ALPHA32I_EXT = constant.Constant( 'GL_ALPHA32I_EXT', 0x8D84 )
GL_INTENSITY32I_EXT = constant.Constant( 'GL_INTENSITY32I_EXT', 0x8D85 )
GL_LUMINANCE32I_EXT = constant.Constant( 'GL_LUMINANCE32I_EXT', 0x8D86 )
GL_LUMINANCE_ALPHA32I_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA32I_EXT', 0x8D87 )
GL_RGBA16I_EXT = constant.Constant( 'GL_RGBA16I_EXT', 0x8D88 )
GL_RGB16I_EXT = constant.Constant( 'GL_RGB16I_EXT', 0x8D89 )
GL_ALPHA16I_EXT = constant.Constant( 'GL_ALPHA16I_EXT', 0x8D8A )
GL_INTENSITY16I_EXT = constant.Constant( 'GL_INTENSITY16I_EXT', 0x8D8B )
GL_LUMINANCE16I_EXT = constant.Constant( 'GL_LUMINANCE16I_EXT', 0x8D8C )
GL_LUMINANCE_ALPHA16I_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA16I_EXT', 0x8D8D )
GL_RGBA8I_EXT = constant.Constant( 'GL_RGBA8I_EXT', 0x8D8E )
GL_RGB8I_EXT = constant.Constant( 'GL_RGB8I_EXT', 0x8D8F )
GL_ALPHA8I_EXT = constant.Constant( 'GL_ALPHA8I_EXT', 0x8D90 )
GL_INTENSITY8I_EXT = constant.Constant( 'GL_INTENSITY8I_EXT', 0x8D91 )
GL_LUMINANCE8I_EXT = constant.Constant( 'GL_LUMINANCE8I_EXT', 0x8D92 )
GL_LUMINANCE_ALPHA8I_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA8I_EXT', 0x8D93 )
GL_RED_INTEGER_EXT = constant.Constant( 'GL_RED_INTEGER_EXT', 0x8D94 )
GL_GREEN_INTEGER_EXT = constant.Constant( 'GL_GREEN_INTEGER_EXT', 0x8D95 )
GL_BLUE_INTEGER_EXT = constant.Constant( 'GL_BLUE_INTEGER_EXT', 0x8D96 )
GL_ALPHA_INTEGER_EXT = constant.Constant( 'GL_ALPHA_INTEGER_EXT', 0x8D97 )
GL_RGB_INTEGER_EXT = constant.Constant( 'GL_RGB_INTEGER_EXT', 0x8D98 )
GL_RGBA_INTEGER_EXT = constant.Constant( 'GL_RGBA_INTEGER_EXT', 0x8D99 )
GL_BGR_INTEGER_EXT = constant.Constant( 'GL_BGR_INTEGER_EXT', 0x8D9A )
GL_BGRA_INTEGER_EXT = constant.Constant( 'GL_BGRA_INTEGER_EXT', 0x8D9B )
GL_LUMINANCE_INTEGER_EXT = constant.Constant( 'GL_LUMINANCE_INTEGER_EXT', 0x8D9C )
GL_LUMINANCE_ALPHA_INTEGER_EXT = constant.Constant( 'GL_LUMINANCE_ALPHA_INTEGER_EXT', 0x8D9D )
GL_RGBA_INTEGER_MODE_EXT = constant.Constant( 'GL_RGBA_INTEGER_MODE_EXT', 0x8D9E )
glTexParameterIivEXT = platform.createExtensionFunction( 
'glTexParameterIivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glTexParameterIivEXT(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glTexParameterIuivEXT = platform.createExtensionFunction( 
'glTexParameterIuivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLuintArray,),
doc='glTexParameterIuivEXT(GLenum(target), GLenum(pname), GLuintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetTexParameterIivEXT = platform.createExtensionFunction( 
'glGetTexParameterIivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetTexParameterIivEXT(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetTexParameterIuivEXT = platform.createExtensionFunction( 
'glGetTexParameterIuivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLuintArray,),
doc='glGetTexParameterIuivEXT(GLenum(target), GLenum(pname), GLuintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glClearColorIiEXT = platform.createExtensionFunction( 
'glClearColorIiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLint,constants.GLint,constants.GLint,),
doc='glClearColorIiEXT(GLint(red), GLint(green), GLint(blue), GLint(alpha)) -> None',
argNames=('red','green','blue','alpha',),
deprecated=_DEPRECATED,
)

glClearColorIuiEXT = platform.createExtensionFunction( 
'glClearColorIuiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glClearColorIuiEXT(GLuint(red), GLuint(green), GLuint(blue), GLuint(alpha)) -> None',
argNames=('red','green','blue','alpha',),
deprecated=_DEPRECATED,
)


def glInitTextureIntegerEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
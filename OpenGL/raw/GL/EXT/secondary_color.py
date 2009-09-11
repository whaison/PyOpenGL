'''OpenGL extension EXT.secondary_color

Overview (from the spec)
	
	This extension allows specifying the RGB components of the secondary
	color used in the Color Sum stage, instead of using the default
	(0,0,0,0) color. It applies only in RGBA mode and when LIGHTING is
	disabled.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/secondary_color.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_secondary_color'
_DEPRECATED = False
GL_COLOR_SUM_EXT = constant.Constant( 'GL_COLOR_SUM_EXT', 0x8458 )
glget.addGLGetConstant( GL_COLOR_SUM_EXT, (1,) )
GL_CURRENT_SECONDARY_COLOR_EXT = constant.Constant( 'GL_CURRENT_SECONDARY_COLOR_EXT', 0x8459 )
glget.addGLGetConstant( GL_CURRENT_SECONDARY_COLOR_EXT, (1,) )
GL_SECONDARY_COLOR_ARRAY_SIZE_EXT = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_SIZE_EXT', 0x845A )
glget.addGLGetConstant( GL_SECONDARY_COLOR_ARRAY_SIZE_EXT, (1,) )
GL_SECONDARY_COLOR_ARRAY_TYPE_EXT = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_TYPE_EXT', 0x845B )
glget.addGLGetConstant( GL_SECONDARY_COLOR_ARRAY_TYPE_EXT, (1,) )
GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT', 0x845C )
glget.addGLGetConstant( GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT, (1,) )
GL_SECONDARY_COLOR_ARRAY_POINTER_EXT = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_POINTER_EXT', 0x845D )
GL_SECONDARY_COLOR_ARRAY_EXT = constant.Constant( 'GL_SECONDARY_COLOR_ARRAY_EXT', 0x845E )
glSecondaryColor3bEXT = platform.createExtensionFunction( 
'glSecondaryColor3bEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLbyte,constants.GLbyte,constants.GLbyte,),
doc='glSecondaryColor3bEXT(GLbyte(red), GLbyte(green), GLbyte(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3bvEXT = platform.createExtensionFunction( 
'glSecondaryColor3bvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLbyteArray,),
doc='glSecondaryColor3bvEXT(GLbyteArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3dEXT = platform.createExtensionFunction( 
'glSecondaryColor3dEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glSecondaryColor3dEXT(GLdouble(red), GLdouble(green), GLdouble(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3dvEXT = platform.createExtensionFunction( 
'glSecondaryColor3dvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLdoubleArray,),
doc='glSecondaryColor3dvEXT(GLdoubleArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3fEXT = platform.createExtensionFunction( 
'glSecondaryColor3fEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLfloat,constants.GLfloat,constants.GLfloat,),
doc='glSecondaryColor3fEXT(GLfloat(red), GLfloat(green), GLfloat(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3fvEXT = platform.createExtensionFunction( 
'glSecondaryColor3fvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLfloatArray,),
doc='glSecondaryColor3fvEXT(GLfloatArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3iEXT = platform.createExtensionFunction( 
'glSecondaryColor3iEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLint,constants.GLint,),
doc='glSecondaryColor3iEXT(GLint(red), GLint(green), GLint(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3ivEXT = platform.createExtensionFunction( 
'glSecondaryColor3ivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLintArray,),
doc='glSecondaryColor3ivEXT(GLintArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3sEXT = platform.createExtensionFunction( 
'glSecondaryColor3sEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLshort,constants.GLshort,constants.GLshort,),
doc='glSecondaryColor3sEXT(GLshort(red), GLshort(green), GLshort(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3svEXT = platform.createExtensionFunction( 
'glSecondaryColor3svEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLshortArray,),
doc='glSecondaryColor3svEXT(GLshortArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3ubEXT = platform.createExtensionFunction( 
'glSecondaryColor3ubEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLubyte,constants.GLubyte,constants.GLubyte,),
doc='glSecondaryColor3ubEXT(GLubyte(red), GLubyte(green), GLubyte(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3ubvEXT = platform.createExtensionFunction( 
'glSecondaryColor3ubvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLubyteArray,),
doc='glSecondaryColor3ubvEXT(GLubyteArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3uiEXT = platform.createExtensionFunction( 
'glSecondaryColor3uiEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glSecondaryColor3uiEXT(GLuint(red), GLuint(green), GLuint(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3uivEXT = platform.createExtensionFunction( 
'glSecondaryColor3uivEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLuintArray,),
doc='glSecondaryColor3uivEXT(GLuintArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColor3usEXT = platform.createExtensionFunction( 
'glSecondaryColor3usEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLushort,constants.GLushort,constants.GLushort,),
doc='glSecondaryColor3usEXT(GLushort(red), GLushort(green), GLushort(blue)) -> None',
argNames=('red','green','blue',),
deprecated=_DEPRECATED,
)

glSecondaryColor3usvEXT = platform.createExtensionFunction( 
'glSecondaryColor3usvEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLushortArray,),
doc='glSecondaryColor3usvEXT(GLushortArray(v)) -> None',
argNames=('v',),
deprecated=_DEPRECATED,
)

glSecondaryColorPointerEXT = platform.createExtensionFunction( 
'glSecondaryColorPointerEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLenum,constants.GLsizei,ctypes.c_void_p,),
doc='glSecondaryColorPointerEXT(GLint(size), GLenum(type), GLsizei(stride), c_void_p(pointer)) -> None',
argNames=('size','type','stride','pointer',),
deprecated=_DEPRECATED,
)


def glInitSecondaryColorEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

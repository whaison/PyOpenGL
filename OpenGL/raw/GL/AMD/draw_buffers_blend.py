'''OpenGL extension AMD.draw_buffers_blend

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/AMD/draw_buffers_blend.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_AMD_draw_buffers_blend'

glBlendFuncIndexedAMD = platform.createExtensionFunction( 
	'glBlendFuncIndexedAMD', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, constants.GLenum,),
	doc = 'glBlendFuncIndexedAMD( GLuint(buf), GLenum(src), GLenum(dst) ) -> None',
	argNames = ('buf', 'src', 'dst',),
)

glBlendFuncSeparateIndexedAMD = platform.createExtensionFunction( 
	'glBlendFuncSeparateIndexedAMD', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, constants.GLenum, constants.GLenum, constants.GLenum,),
	doc = 'glBlendFuncSeparateIndexedAMD( GLuint(buf), GLenum(srcRGB), GLenum(dstRGB), GLenum(srcAlpha), GLenum(dstAlpha) ) -> None',
	argNames = ('buf', 'srcRGB', 'dstRGB', 'srcAlpha', 'dstAlpha',),
)

glBlendEquationIndexedAMD = platform.createExtensionFunction( 
	'glBlendEquationIndexedAMD', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum,),
	doc = 'glBlendEquationIndexedAMD( GLuint(buf), GLenum(mode) ) -> None',
	argNames = ('buf', 'mode',),
)

glBlendEquationSeparateIndexedAMD = platform.createExtensionFunction( 
	'glBlendEquationSeparateIndexedAMD', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, constants.GLenum,),
	doc = 'glBlendEquationSeparateIndexedAMD( GLuint(buf), GLenum(modeRGB), GLenum(modeAlpha) ) -> None',
	argNames = ('buf', 'modeRGB', 'modeAlpha',),
)


def glInitDrawBuffersBlendAMD():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )

'''OpenGL extension NV.fragment_program

Overview (from the spec)
	
	OpenGL mandates a certain set of configurable per-fragment computations
	defining texture lookup, texture environment, color sum, and fog
	operations.  Each of these areas provide a useful but limited set of fixed
	operations.  For example, unextended OpenGL 1.2.1 provides only four
	texture environment modes, color sum, and three fog modes.  Many OpenGL
	extensions have either improved existing functionality or introduced new
	configurable fragment operations.  While these extensions have enabled new
	and interesting rendering effects, the set of effects is limited by the
	set of special modes introduced by the extension.  This lack of
	flexibility is in contrast to the high-level of programmability of
	general-purpose CPUs and other (frequently software-based) shading
	languages.  The purpose of this extension is to expose to the OpenGL
	application writer an unprecedented degree of programmability in the
	computation of final fragment colors and depth values.
	
	This extension provides a mechanism for defining fragment program
	instruction sequences for application-defined fragment programs.  When in
	fragment program mode, a program is executed each time a fragment is
	produced by rasterization.  The inputs for the program are the attributes
	(position, colors, texture coordinates) associated with the fragment and a
	set of constant registers.  A fragment program can perform mathematical
	computations and texture lookups using arbitrary texture coordinates.  The
	results of a fragment program are new color and depth values for the
	fragment.
	
	This extension defines a programming model including a 4-component vector
	instruction set, 16- and 32-bit floating-point data types, and a
	relatively large set of temporary registers.  The programming model also
	includes a condition code vector which can be used to mask register writes
	at run-time or kill fragments altogether.  The syntax, program
	instructions, and general semantics are similar to those in the
	NV_vertex_program and NV_vertex_program2 extensions, which provide for the
	execution of an arbitrary program each time the GL receives a vertex.
	
	The fragment program execution environment is designed for efficient
	hardware implementation and to support a wide variety of programs.  By
	design, the entire set of existing fragment programs defined by existing
	OpenGL per-fragment computation extensions can be implemented using the
	extension's programming model.
	
	The fragment program execution environment accesses textures via
	arbitrarily computed texture coordinates.  As such, there is no necessary
	correspondence between the texture coordinates and texture maps previously
	lumped into a single "texture unit".  This extension separates the notion
	of "texture coordinate sets" and "texture image units" (texture maps and
	associated parameters), allowing implementations with a different number
	of each.  The initial implementation of this extension will support 8
	texture coordinate sets and 16 texture image units.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/NV/fragment_program.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_fragment_program'
_DEPRECATED = False
GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV = constant.Constant( 'GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV', 0x8868 )
glget.addGLGetConstant( GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV, (1,) )
GL_FRAGMENT_PROGRAM_NV = constant.Constant( 'GL_FRAGMENT_PROGRAM_NV', 0x8870 )
glget.addGLGetConstant( GL_FRAGMENT_PROGRAM_NV, (1,) )
GL_MAX_TEXTURE_COORDS_NV = constant.Constant( 'GL_MAX_TEXTURE_COORDS_NV', 0x8871 )
glget.addGLGetConstant( GL_MAX_TEXTURE_COORDS_NV, (1,) )
GL_MAX_TEXTURE_IMAGE_UNITS_NV = constant.Constant( 'GL_MAX_TEXTURE_IMAGE_UNITS_NV', 0x8872 )
glget.addGLGetConstant( GL_MAX_TEXTURE_IMAGE_UNITS_NV, (1,) )
GL_FRAGMENT_PROGRAM_BINDING_NV = constant.Constant( 'GL_FRAGMENT_PROGRAM_BINDING_NV', 0x8873 )
glget.addGLGetConstant( GL_FRAGMENT_PROGRAM_BINDING_NV, (1,) )
GL_PROGRAM_ERROR_STRING_NV = constant.Constant( 'GL_PROGRAM_ERROR_STRING_NV', 0x8874 )
glProgramNamedParameter4fNV = platform.createExtensionFunction( 
'glProgramNamedParameter4fNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLubyteArray,constants.GLfloat,constants.GLfloat,constants.GLfloat,constants.GLfloat,),
doc='glProgramNamedParameter4fNV(GLuint(id), GLsizei(len), GLubyteArray(name), GLfloat(x), GLfloat(y), GLfloat(z), GLfloat(w)) -> None',
argNames=('id','len','name','x','y','z','w',),
deprecated=_DEPRECATED,
)

glProgramNamedParameter4dNV = platform.createExtensionFunction( 
'glProgramNamedParameter4dNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLubyteArray,constants.GLdouble,constants.GLdouble,constants.GLdouble,constants.GLdouble,),
doc='glProgramNamedParameter4dNV(GLuint(id), GLsizei(len), GLubyteArray(name), GLdouble(x), GLdouble(y), GLdouble(z), GLdouble(w)) -> None',
argNames=('id','len','name','x','y','z','w',),
deprecated=_DEPRECATED,
)

glProgramNamedParameter4fvNV = platform.createExtensionFunction( 
'glProgramNamedParameter4fvNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLubyteArray,arrays.GLfloatArray,),
doc='glProgramNamedParameter4fvNV(GLuint(id), GLsizei(len), GLubyteArray(name), GLfloatArray(v)) -> None',
argNames=('id','len','name','v',),
deprecated=_DEPRECATED,
)

glProgramNamedParameter4dvNV = platform.createExtensionFunction( 
'glProgramNamedParameter4dvNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLubyteArray,arrays.GLdoubleArray,),
doc='glProgramNamedParameter4dvNV(GLuint(id), GLsizei(len), GLubyteArray(name), GLdoubleArray(v)) -> None',
argNames=('id','len','name','v',),
deprecated=_DEPRECATED,
)

glGetProgramNamedParameterfvNV = platform.createExtensionFunction( 
'glGetProgramNamedParameterfvNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLubyteArray,arrays.GLfloatArray,),
doc='glGetProgramNamedParameterfvNV(GLuint(id), GLsizei(len), GLubyteArray(name), GLfloatArray(params)) -> None',
argNames=('id','len','name','params',),
deprecated=_DEPRECATED,
)

glGetProgramNamedParameterdvNV = platform.createExtensionFunction( 
'glGetProgramNamedParameterdvNV',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLubyteArray,arrays.GLdoubleArray,),
doc='glGetProgramNamedParameterdvNV(GLuint(id), GLsizei(len), GLubyteArray(name), GLdoubleArray(params)) -> None',
argNames=('id','len','name','params',),
deprecated=_DEPRECATED,
)


def glInitFragmentProgramNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

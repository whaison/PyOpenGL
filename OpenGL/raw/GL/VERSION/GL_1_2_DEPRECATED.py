'''OpenGL extension VERSION.GL_1_2_DEPRECATED

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/VERSION/GL_1_2_DEPRECATED.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_1_2'
_DEPRECATED = True
GL_RESCALE_NORMAL = constant.Constant( 'GL_RESCALE_NORMAL', 0x803A )
GL_LIGHT_MODEL_COLOR_CONTROL = constant.Constant( 'GL_LIGHT_MODEL_COLOR_CONTROL', 0x81F8 )
GL_SINGLE_COLOR = constant.Constant( 'GL_SINGLE_COLOR', 0x81F9 )
GL_SEPARATE_SPECULAR_COLOR = constant.Constant( 'GL_SEPARATE_SPECULAR_COLOR', 0x81FA )
GL_ALIASED_POINT_SIZE_RANGE = constant.Constant( 'GL_ALIASED_POINT_SIZE_RANGE', 0x846D )
glColorTable = platform.createExtensionFunction( 
'glColorTable',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLsizei,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glColorTable(GLenum(target), GLenum(internalformat), GLsizei(width), GLenum(format), GLenum(type), c_void_p(table)) -> None',
argNames=('target','internalformat','width','format','type','table',),
deprecated=_DEPRECATED,
)

glColorTableParameterfv = platform.createExtensionFunction( 
'glColorTableParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glColorTableParameterfv(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glColorTableParameteriv = platform.createExtensionFunction( 
'glColorTableParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glColorTableParameteriv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glCopyColorTable = platform.createExtensionFunction( 
'glCopyColorTable',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLint,constants.GLint,constants.GLsizei,),
doc='glCopyColorTable(GLenum(target), GLenum(internalformat), GLint(x), GLint(y), GLsizei(width)) -> None',
argNames=('target','internalformat','x','y','width',),
deprecated=_DEPRECATED,
)

glGetColorTable = platform.createExtensionFunction( 
'glGetColorTable',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glGetColorTable(GLenum(target), GLenum(format), GLenum(type), c_void_p(table)) -> None',
argNames=('target','format','type','table',),
deprecated=_DEPRECATED,
)

glGetColorTableParameterfv = platform.createExtensionFunction( 
'glGetColorTableParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glGetColorTableParameterfv(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetColorTableParameteriv = platform.createExtensionFunction( 
'glGetColorTableParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetColorTableParameteriv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glColorSubTable = platform.createExtensionFunction( 
'glColorSubTable',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glColorSubTable(GLenum(target), GLsizei(start), GLsizei(count), GLenum(format), GLenum(type), c_void_p(data)) -> None',
argNames=('target','start','count','format','type','data',),
deprecated=_DEPRECATED,
)

glCopyColorSubTable = platform.createExtensionFunction( 
'glCopyColorSubTable',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLint,constants.GLint,constants.GLsizei,),
doc='glCopyColorSubTable(GLenum(target), GLsizei(start), GLint(x), GLint(y), GLsizei(width)) -> None',
argNames=('target','start','x','y','width',),
deprecated=_DEPRECATED,
)

glConvolutionFilter1D = platform.createExtensionFunction( 
'glConvolutionFilter1D',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLsizei,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glConvolutionFilter1D(GLenum(target), GLenum(internalformat), GLsizei(width), GLenum(format), GLenum(type), c_void_p(image)) -> None',
argNames=('target','internalformat','width','format','type','image',),
deprecated=_DEPRECATED,
)

glConvolutionFilter2D = platform.createExtensionFunction( 
'glConvolutionFilter2D',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glConvolutionFilter2D(GLenum(target), GLenum(internalformat), GLsizei(width), GLsizei(height), GLenum(format), GLenum(type), c_void_p(image)) -> None',
argNames=('target','internalformat','width','height','format','type','image',),
deprecated=_DEPRECATED,
)

glConvolutionParameterf = platform.createExtensionFunction( 
'glConvolutionParameterf',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLfloat,),
doc='glConvolutionParameterf(GLenum(target), GLenum(pname), GLfloat(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glConvolutionParameterfv = platform.createExtensionFunction( 
'glConvolutionParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glConvolutionParameterfv(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glConvolutionParameteri = platform.createExtensionFunction( 
'glConvolutionParameteri',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLint,),
doc='glConvolutionParameteri(GLenum(target), GLenum(pname), GLint(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glConvolutionParameteriv = platform.createExtensionFunction( 
'glConvolutionParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glConvolutionParameteriv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glCopyConvolutionFilter1D = platform.createExtensionFunction( 
'glCopyConvolutionFilter1D',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLint,constants.GLint,constants.GLsizei,),
doc='glCopyConvolutionFilter1D(GLenum(target), GLenum(internalformat), GLint(x), GLint(y), GLsizei(width)) -> None',
argNames=('target','internalformat','x','y','width',),
deprecated=_DEPRECATED,
)

glCopyConvolutionFilter2D = platform.createExtensionFunction( 
'glCopyConvolutionFilter2D',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLint,constants.GLint,constants.GLsizei,constants.GLsizei,),
doc='glCopyConvolutionFilter2D(GLenum(target), GLenum(internalformat), GLint(x), GLint(y), GLsizei(width), GLsizei(height)) -> None',
argNames=('target','internalformat','x','y','width','height',),
deprecated=_DEPRECATED,
)

glGetConvolutionFilter = platform.createExtensionFunction( 
'glGetConvolutionFilter',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glGetConvolutionFilter(GLenum(target), GLenum(format), GLenum(type), c_void_p(image)) -> None',
argNames=('target','format','type','image',),
deprecated=_DEPRECATED,
)

glGetConvolutionParameterfv = platform.createExtensionFunction( 
'glGetConvolutionParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glGetConvolutionParameterfv(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetConvolutionParameteriv = platform.createExtensionFunction( 
'glGetConvolutionParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetConvolutionParameteriv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetSeparableFilter = platform.createExtensionFunction( 
'glGetSeparableFilter',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLenum,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p,),
doc='glGetSeparableFilter(GLenum(target), GLenum(format), GLenum(type), c_void_p(row), c_void_p(column), c_void_p(span)) -> None',
argNames=('target','format','type','row','column','span',),
deprecated=_DEPRECATED,
)

glSeparableFilter2D = platform.createExtensionFunction( 
'glSeparableFilter2D',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLsizei,constants.GLsizei,constants.GLenum,constants.GLenum,ctypes.c_void_p,ctypes.c_void_p,),
doc='glSeparableFilter2D(GLenum(target), GLenum(internalformat), GLsizei(width), GLsizei(height), GLenum(format), GLenum(type), c_void_p(row), c_void_p(column)) -> None',
argNames=('target','internalformat','width','height','format','type','row','column',),
deprecated=_DEPRECATED,
)

glGetHistogram = platform.createExtensionFunction( 
'glGetHistogram',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLboolean,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glGetHistogram(GLenum(target), GLboolean(reset), GLenum(format), GLenum(type), c_void_p(values)) -> None',
argNames=('target','reset','format','type','values',),
deprecated=_DEPRECATED,
)

glGetHistogramParameterfv = platform.createExtensionFunction( 
'glGetHistogramParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glGetHistogramParameterfv(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetHistogramParameteriv = platform.createExtensionFunction( 
'glGetHistogramParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetHistogramParameteriv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetMinmax = platform.createExtensionFunction( 
'glGetMinmax',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLboolean,constants.GLenum,constants.GLenum,ctypes.c_void_p,),
doc='glGetMinmax(GLenum(target), GLboolean(reset), GLenum(format), GLenum(type), c_void_p(values)) -> None',
argNames=('target','reset','format','type','values',),
deprecated=_DEPRECATED,
)

glGetMinmaxParameterfv = platform.createExtensionFunction( 
'glGetMinmaxParameterfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLfloatArray,),
doc='glGetMinmaxParameterfv(GLenum(target), GLenum(pname), GLfloatArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetMinmaxParameteriv = platform.createExtensionFunction( 
'glGetMinmaxParameteriv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetMinmaxParameteriv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glHistogram = platform.createExtensionFunction( 
'glHistogram',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLsizei,constants.GLenum,constants.GLboolean,),
doc='glHistogram(GLenum(target), GLsizei(width), GLenum(internalformat), GLboolean(sink)) -> None',
argNames=('target','width','internalformat','sink',),
deprecated=_DEPRECATED,
)

glMinmax = platform.createExtensionFunction( 
'glMinmax',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,constants.GLboolean,),
doc='glMinmax(GLenum(target), GLenum(internalformat), GLboolean(sink)) -> None',
argNames=('target','internalformat','sink',),
deprecated=_DEPRECATED,
)

glResetHistogram = platform.createExtensionFunction( 
'glResetHistogram',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,),
doc='glResetHistogram(GLenum(target)) -> None',
argNames=('target',),
deprecated=_DEPRECATED,
)

glResetMinmax = platform.createExtensionFunction( 
'glResetMinmax',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,),
doc='glResetMinmax(GLenum(target)) -> None',
argNames=('target',),
deprecated=_DEPRECATED,
)

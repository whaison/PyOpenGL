'''OpenGL extension AMD.performance_monitor

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_AMD_performance_monitor'
_DEPRECATED = False
GL_COUNTER_TYPE_AMD = constant.Constant( 'GL_COUNTER_TYPE_AMD', 0x8BC0 )
GL_COUNTER_RANGE_AMD = constant.Constant( 'GL_COUNTER_RANGE_AMD', 0x8BC1 )
GL_UNSIGNED_INT64_AMD = constant.Constant( 'GL_UNSIGNED_INT64_AMD', 0x8BC2 )
GL_PERCENTAGE_AMD = constant.Constant( 'GL_PERCENTAGE_AMD', 0x8BC3 )
GL_PERFMON_RESULT_AVAILABLE_AMD = constant.Constant( 'GL_PERFMON_RESULT_AVAILABLE_AMD', 0x8BC4 )
GL_PERFMON_RESULT_SIZE_AMD = constant.Constant( 'GL_PERFMON_RESULT_SIZE_AMD', 0x8BC5 )
GL_PERFMON_RESULT_AMD = constant.Constant( 'GL_PERFMON_RESULT_AMD', 0x8BC6 )
glGetPerfMonitorGroupsAMD = platform.createExtensionFunction( 
'glGetPerfMonitorGroupsAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(arrays.GLintArray,constants.GLsizei,arrays.GLuintArray,),
doc='glGetPerfMonitorGroupsAMD(GLintArray(numGroups), GLsizei(groupsSize), GLuintArray(groups)) -> None',
argNames=('numGroups','groupsSize','groups',),
deprecated=_DEPRECATED,
)

glGetPerfMonitorCountersAMD = platform.createExtensionFunction( 
'glGetPerfMonitorCountersAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLintArray,arrays.GLintArray,constants.GLsizei,arrays.GLuintArray,),
doc='glGetPerfMonitorCountersAMD(GLuint(group), GLintArray(numCounters), GLintArray(maxActiveCounters), GLsizei(counterSize), GLuintArray(counters)) -> None',
argNames=('group','numCounters','maxActiveCounters','counterSize','counters',),
deprecated=_DEPRECATED,
)

glGetPerfMonitorGroupStringAMD = platform.createExtensionFunction( 
'glGetPerfMonitorGroupStringAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray,),
doc='glGetPerfMonitorGroupStringAMD(GLuint(group), GLsizei(bufSize), GLsizeiArray(length), GLcharArray(groupString)) -> None',
argNames=('group','bufSize','length','groupString',),
deprecated=_DEPRECATED,
)

glGetPerfMonitorCounterStringAMD = platform.createExtensionFunction( 
'glGetPerfMonitorCounterStringAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray,),
doc='glGetPerfMonitorCounterStringAMD(GLuint(group), GLuint(counter), GLsizei(bufSize), GLsizeiArray(length), GLcharArray(counterString)) -> None',
argNames=('group','counter','bufSize','length','counterString',),
deprecated=_DEPRECATED,
)

glGetPerfMonitorCounterInfoAMD = platform.createExtensionFunction( 
'glGetPerfMonitorCounterInfoAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLenum,ctypes.c_void_p,),
doc='glGetPerfMonitorCounterInfoAMD(GLuint(group), GLuint(counter), GLenum(pname), c_void_p(data)) -> None',
argNames=('group','counter','pname','data',),
deprecated=_DEPRECATED,
)

glGenPerfMonitorsAMD = platform.createExtensionFunction( 
'glGenPerfMonitorsAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glGenPerfMonitorsAMD(GLsizei(n), GLuintArray(monitors)) -> None',
argNames=('n','monitors',),
deprecated=_DEPRECATED,
)

glDeletePerfMonitorsAMD = platform.createExtensionFunction( 
'glDeletePerfMonitorsAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glDeletePerfMonitorsAMD(GLsizei(n), GLuintArray(monitors)) -> None',
argNames=('n','monitors',),
deprecated=_DEPRECATED,
)

glSelectPerfMonitorCountersAMD = platform.createExtensionFunction( 
'glSelectPerfMonitorCountersAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLboolean,constants.GLuint,constants.GLint,arrays.GLuintArray,),
doc='glSelectPerfMonitorCountersAMD(GLuint(monitor), GLboolean(enable), GLuint(group), GLint(numCounters), GLuintArray(counterList)) -> None',
argNames=('monitor','enable','group','numCounters','counterList',),
deprecated=_DEPRECATED,
)

glBeginPerfMonitorAMD = platform.createExtensionFunction( 
'glBeginPerfMonitorAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glBeginPerfMonitorAMD(GLuint(monitor)) -> None',
argNames=('monitor',),
deprecated=_DEPRECATED,
)

glEndPerfMonitorAMD = platform.createExtensionFunction( 
'glEndPerfMonitorAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,),
doc='glEndPerfMonitorAMD(GLuint(monitor)) -> None',
argNames=('monitor',),
deprecated=_DEPRECATED,
)

glGetPerfMonitorCounterDataAMD = platform.createExtensionFunction( 
'glGetPerfMonitorCounterDataAMD',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLsizei,arrays.GLuintArray,arrays.GLintArray,),
doc='glGetPerfMonitorCounterDataAMD(GLuint(monitor), GLenum(pname), GLsizei(dataSize), GLuintArray(data), GLintArray(bytesWritten)) -> None',
argNames=('monitor','pname','dataSize','data','bytesWritten',),
deprecated=_DEPRECATED,
)


def glInitPerformanceMonitorAMD():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )

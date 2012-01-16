'''OpenGL extension ARB.debug_output

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_debug_output'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_debug_output',False)
_p.unpack_constants( """GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB 0x8243
GL_DEBUG_CALLBACK_FUNCTION_ARB 0x8244
GL_DEBUG_CALLBACK_USER_PARAM_ARB 0x8245
GL_DEBUG_SOURCE_API_ARB 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY_ARB 0x8249
GL_DEBUG_SOURCE_APPLICATION_ARB 0x824A
GL_DEBUG_SOURCE_OTHER_ARB 0x824B
GL_DEBUG_TYPE_ERROR_ARB 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB 0x824E
GL_DEBUG_TYPE_PORTABILITY_ARB 0x824F
GL_DEBUG_TYPE_PERFORMANCE_ARB 0x8250
GL_DEBUG_TYPE_OTHER_ARB 0x8251
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB 0x9144
GL_DEBUG_LOGGED_MESSAGES_ARB 0x9145
GL_DEBUG_SEVERITY_HIGH_ARB 0x9146
GL_DEBUG_SEVERITY_MEDIUM_ARB 0x9147
GL_DEBUG_SEVERITY_LOW_ARB 0x9148""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray,_cs.GLboolean)
def glDebugMessageControlARB( source,type,severity,count,ids,enabled ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLsizei,arrays.GLcharArray)
def glDebugMessageInsertARB( source,type,id,severity,length,buf ):pass
@_f
@_p.types(None,_cs.GLDEBUGPROCARB,ctypes.c_void_p)
def glDebugMessageCallbackARB( callback,userParam ):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,arrays.GLuintArray,arrays.GLuintArray,arrays.GLuintArray,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetDebugMessageLogARB( count,bufsize,sources,types,ids,severities,lengths,messageLog ):pass


def glInitDebugOutputARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

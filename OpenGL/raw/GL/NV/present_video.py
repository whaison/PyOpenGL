'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_present_video'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_present_video',False)
_p.unpack_constants( """GL_FRAME_NV 0x8E26
GL_FIELDS_NV 0x8E27
GL_CURRENT_TIME_NV 0x8E28
GL_NUM_FILL_STREAMS_NV 0x8E29
GL_PRESENT_TIME_NV 0x8E2A
GL_PRESENT_DURATION_NV 0x8E2B""", globals())
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glPresentFrameKeyedNV(video_slot,minPresentTime,beginPresentTimeId,presentDurationId,type,target0,fill0,key0,target1,fill1,key1):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint64EXT,_cs.GLuint,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glPresentFrameDualFillNV(video_slot,minPresentTime,beginPresentTimeId,presentDurationId,type,target0,fill0,target1,fill1,target2,fill2,target3,fill3):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVideoivNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetVideouivNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetVideoi64vNV(video_slot,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetVideoui64vNV(video_slot,pname,params):pass


def glInitPresentVideoNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

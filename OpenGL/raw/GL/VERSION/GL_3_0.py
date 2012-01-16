'''OpenGL extension VERSION.GL_3_0

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_3_0'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_VERSION_GL_3_0',False)
_p.unpack_constants( """GL_COMPARE_REF_TO_TEXTURE 0x884E
GL_CLIP_DISTANCE0 0x3000
GL_CLIP_DISTANCE1 0x3001
GL_CLIP_DISTANCE2 0x3002
GL_CLIP_DISTANCE3 0x3003
GL_CLIP_DISTANCE4 0x3004
GL_CLIP_DISTANCE5 0x3005
GL_CLIP_DISTANCE6 0x3006
GL_CLIP_DISTANCE7 0x3007
GL_MAX_CLIP_DISTANCES 0xD32
GL_MAJOR_VERSION 0x821B
GL_MINOR_VERSION 0x821C
GL_NUM_EXTENSIONS 0x821D
GL_CONTEXT_FLAGS 0x821E
GL_COMPRESSED_RED 0x8225
GL_COMPRESSED_RG 0x8226
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT 0x1
GL_RGBA32F 0x8814
GL_RGB32F 0x8815
GL_RGBA16F 0x881A
GL_RGB16F 0x881B
GL_VERTEX_ATTRIB_ARRAY_INTEGER 0x88FD
GL_MAX_ARRAY_TEXTURE_LAYERS 0x88FF
GL_MIN_PROGRAM_TEXEL_OFFSET 0x8904
GL_MAX_PROGRAM_TEXEL_OFFSET 0x8905
GL_CLAMP_READ_COLOR 0x891C
GL_FIXED_ONLY 0x891D
GL_MAX_VARYING_COMPONENTS 0x8B4B
GL_TEXTURE_1D_ARRAY 0x8C18
GL_PROXY_TEXTURE_1D_ARRAY 0x8C19
GL_TEXTURE_2D_ARRAY 0x8C1A
GL_PROXY_TEXTURE_2D_ARRAY 0x8C1B
GL_TEXTURE_BINDING_1D_ARRAY 0x8C1C
GL_TEXTURE_BINDING_2D_ARRAY 0x8C1D
GL_R11F_G11F_B10F 0x8C3A
GL_UNSIGNED_INT_10F_11F_11F_REV 0x8C3B
GL_RGB9_E5 0x8C3D
GL_UNSIGNED_INT_5_9_9_9_REV 0x8C3E
GL_TEXTURE_SHARED_SIZE 0x8C3F
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH 0x8C76
GL_TRANSFORM_FEEDBACK_BUFFER_MODE 0x8C7F
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS 0x8C80
GL_TRANSFORM_FEEDBACK_VARYINGS 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_START 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE 0x8C85
GL_PRIMITIVES_GENERATED 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN 0x8C88
GL_RASTERIZER_DISCARD 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS 0x8C8B
GL_INTERLEAVED_ATTRIBS 0x8C8C
GL_SEPARATE_ATTRIBS 0x8C8D
GL_TRANSFORM_FEEDBACK_BUFFER 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING 0x8C8F
GL_RGBA32UI 0x8D70
GL_RGB32UI 0x8D71
GL_RGBA16UI 0x8D76
GL_RGB16UI 0x8D77
GL_RGBA8UI 0x8D7C
GL_RGB8UI 0x8D7D
GL_RGBA32I 0x8D82
GL_RGB32I 0x8D83
GL_RGBA16I 0x8D88
GL_RGB16I 0x8D89
GL_RGBA8I 0x8D8E
GL_RGB8I 0x8D8F
GL_RED_INTEGER 0x8D94
GL_GREEN_INTEGER 0x8D95
GL_BLUE_INTEGER 0x8D96
GL_RGB_INTEGER 0x8D98
GL_RGBA_INTEGER 0x8D99
GL_BGR_INTEGER 0x8D9A
GL_BGRA_INTEGER 0x8D9B
GL_SAMPLER_1D_ARRAY 0x8DC0
GL_SAMPLER_2D_ARRAY 0x8DC1
GL_SAMPLER_1D_ARRAY_SHADOW 0x8DC3
GL_SAMPLER_2D_ARRAY_SHADOW 0x8DC4
GL_SAMPLER_CUBE_SHADOW 0x8DC5
GL_UNSIGNED_INT_VEC2 0x8DC6
GL_UNSIGNED_INT_VEC3 0x8DC7
GL_UNSIGNED_INT_VEC4 0x8DC8
GL_INT_SAMPLER_1D 0x8DC9
GL_INT_SAMPLER_2D 0x8DCA
GL_INT_SAMPLER_3D 0x8DCB
GL_INT_SAMPLER_CUBE 0x8DCC
GL_INT_SAMPLER_1D_ARRAY 0x8DCE
GL_INT_SAMPLER_2D_ARRAY 0x8DCF
GL_UNSIGNED_INT_SAMPLER_1D 0x8DD1
GL_UNSIGNED_INT_SAMPLER_2D 0x8DD2
GL_UNSIGNED_INT_SAMPLER_3D 0x8DD3
GL_UNSIGNED_INT_SAMPLER_CUBE 0x8DD4
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY 0x8DD6
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY 0x8DD7
GL_QUERY_WAIT 0x8E13
GL_QUERY_NO_WAIT 0x8E14
GL_QUERY_BY_REGION_WAIT 0x8E15
GL_QUERY_BY_REGION_NO_WAIT 0x8E16
GL_BUFFER_ACCESS_FLAGS 0x911F
GL_BUFFER_MAP_LENGTH 0x9120
GL_BUFFER_MAP_OFFSET 0x9121""", globals())
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMaski( index,r,g,b,a ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLbooleanArray)
def glGetBooleani_v( target,index,data ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetIntegeri_v( target,index,data ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEnablei( target,index ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDisablei( target,index ):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glIsEnabledi( target,index ):pass
@_f
@_p.types(None,_cs.GLenum)
def glBeginTransformFeedback( primitiveMode ):pass
@_f
@_p.types(None,)
def glEndTransformFeedback(  ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glBindBufferRange( target,index,buffer,offset,size ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBindBufferBase( target,index,buffer ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,ctypes.POINTER( ctypes.POINTER( _cs.GLchar )),_cs.GLenum)
def glTransformFeedbackVaryings( program,count,varyings,bufferMode ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetTransformFeedbackVarying( program,index,bufSize,length,size,type,name ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glClampColor( target,clamp ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBeginConditionalRender( id,mode ):pass
@_f
@_p.types(None,)
def glEndConditionalRender(  ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribIPointer( index,size,type,stride,pointer ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribIiv( index,pname,params ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetVertexAttribIuiv( index,pname,params ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint)
def glVertexAttribI1i( index,x ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint)
def glVertexAttribI2i( index,x,y ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI3i( index,x,y,z ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexAttribI4i( index,x,y,z,w ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribI1ui( index,x ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI2ui( index,x,y ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI3ui( index,x,y,z ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glVertexAttribI4ui( index,x,y,z,w ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI1iv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI2iv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI3iv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray)
def glVertexAttribI4iv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI1uiv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI2uiv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI3uiv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLuintArray)
def glVertexAttribI4uiv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLbyteArray)
def glVertexAttribI4bv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLshortArray)
def glVertexAttribI4sv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLubyteArray)
def glVertexAttribI4ubv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLushortArray)
def glVertexAttribI4usv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLuintArray)
def glGetUniformuiv( program,location,params ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,arrays.GLcharArray)
def glBindFragDataLocation( program,color,name ):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetFragDataLocation( program,name ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint)
def glUniform1ui( location,v0 ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint)
def glUniform2ui( location,v0,v1 ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniform3ui( location,v0,v1,v2 ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glUniform4ui( location,v0,v1,v2,v3 ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform1uiv( location,count,value ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform2uiv( location,count,value ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform3uiv( location,count,value ):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glUniform4uiv( location,count,value ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameterIiv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glTexParameterIuiv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameterIiv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetTexParameterIuiv( target,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLintArray)
def glClearBufferiv( buffer,drawbuffer,value ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLuintArray)
def glClearBufferuiv( buffer,drawbuffer,value ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,arrays.GLfloatArray)
def glClearBufferfv( buffer,drawbuffer,value ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLfloat,_cs.GLint)
def glClearBufferfi( buffer,drawbuffer,depth,stencil ):pass
@_f
@_p.types(arrays.GLubyteArray,_cs.GLenum,_cs.GLuint)
def glGetStringi( name,index ):pass
# import deprecated
from OpenGL.raw.GL.VERSION.GL_3_0_DEPRECATED import *

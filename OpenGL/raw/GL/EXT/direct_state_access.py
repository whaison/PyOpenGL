'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_direct_state_access'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_direct_state_access',False)
_p.unpack_constants( """GL_PROGRAM_MATRIX_EXT 0x8E2D
GL_TRANSPOSE_PROGRAM_MATRIX_EXT 0x8E2E
GL_PROGRAM_MATRIX_STACK_DEPTH_EXT 0x8E2F""", globals())
@_f
@_p.types(None,_cs.GLbitfield)
def glClientAttribDefaultEXT(mask):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glPushClientAttribDefaultEXT(mask):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoadfEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixLoaddEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMultfEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixMultdEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixLoadIdentityEXT(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMatrixRotatefEXT(mode,angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixRotatedEXT(mode,angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMatrixScalefEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixScaledEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMatrixTranslatefEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixTranslatedEXT(mode,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixFrustumEXT(mode,left,right,bottom,top,zNear,zFar):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glMatrixOrthoEXT(mode,left,right,bottom,top,zNear,zFar):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixPopEXT(mode):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixPushEXT(mode):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixLoadTransposefEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixLoadTransposedEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glMatrixMultTransposefEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glMatrixMultTransposedEXT(mode,m):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTextureParameterfEXT(texture,target,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTextureParameterfvEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTextureParameteriEXT(texture,target,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTextureParameterivEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureImage1DEXT(texture,target,level,internalformat,width,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureImage2DEXT(texture,target,level,internalformat,width,height,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureSubImage1DEXT(texture,target,level,xoffset,width,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureSubImage2DEXT(texture,target,level,xoffset,yoffset,width,height,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLint)
def glCopyTextureImage1DEXT(texture,target,level,internalformat,x,y,width,border):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLint)
def glCopyTextureImage2DEXT(texture,target,level,internalformat,x,y,width,height,border):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyTextureSubImage1DEXT(texture,target,level,xoffset,x,y,width):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTextureSubImage2DEXT(texture,target,level,xoffset,yoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetTextureImageEXT(texture,target,level,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTextureParameterfvEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTextureParameterivEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,arrays.GLfloatArray)
def glGetTextureLevelParameterfvEXT(texture,target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,arrays.GLintArray)
def glGetTextureLevelParameterivEXT(texture,target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureImage3DEXT(texture,target,level,internalformat,width,height,depth,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTextureSubImage3DEXT(texture,target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTextureSubImage3DEXT(texture,target,level,xoffset,yoffset,zoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glMultiTexParameterfEXT(texunit,target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexParameterfvEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glMultiTexParameteriEXT(texunit,target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glMultiTexParameterivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glMultiTexImage1DEXT(texunit,target,level,internalformat,width,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glMultiTexImage2DEXT(texunit,target,level,internalformat,width,height,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glMultiTexSubImage1DEXT(texunit,target,level,xoffset,width,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glMultiTexSubImage2DEXT(texunit,target,level,xoffset,yoffset,width,height,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLint)
def glCopyMultiTexImage1DEXT(texunit,target,level,internalformat,x,y,width,border):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLint)
def glCopyMultiTexImage2DEXT(texunit,target,level,internalformat,x,y,width,height,border):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei)
def glCopyMultiTexSubImage1DEXT(texunit,target,level,xoffset,x,y,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyMultiTexSubImage2DEXT(texunit,target,level,xoffset,yoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetMultiTexImageEXT(texunit,target,level,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMultiTexParameterfvEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMultiTexParameterivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,arrays.GLfloatArray)
def glGetMultiTexLevelParameterfvEXT(texunit,target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,arrays.GLintArray)
def glGetMultiTexLevelParameterivEXT(texunit,target,level,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glMultiTexImage3DEXT(texunit,target,level,internalformat,width,height,depth,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glMultiTexSubImage3DEXT(texunit,target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyMultiTexSubImage3DEXT(texunit,target,level,xoffset,yoffset,zoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glBindMultiTextureEXT(texunit,target,texture):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEnableClientStateIndexedEXT(array,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDisableClientStateIndexedEXT(array,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glMultiTexCoordPointerEXT(texunit,size,type,stride,pointer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glMultiTexEnvfEXT(texunit,target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexEnvfvEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glMultiTexEnviEXT(texunit,target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glMultiTexEnvivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLdouble)
def glMultiTexGendEXT(texunit,coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLdoubleArray)
def glMultiTexGendvEXT(texunit,coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glMultiTexGenfEXT(texunit,coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glMultiTexGenfvEXT(texunit,coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glMultiTexGeniEXT(texunit,coord,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glMultiTexGenivEXT(texunit,coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMultiTexEnvfvEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMultiTexEnvivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLdoubleArray)
def glGetMultiTexGendvEXT(texunit,coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMultiTexGenfvEXT(texunit,coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMultiTexGenivEXT(texunit,coord,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLfloatArray)
def glGetFloatIndexedvEXT(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLdoubleArray)
def glGetDoubleIndexedvEXT(target,index,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLvoidpArray)
def glGetPointerIndexedvEXT(target,index,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureImage3DEXT(texture,target,level,internalformat,width,height,depth,border,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureImage2DEXT(texture,target,level,internalformat,width,height,border,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureImage1DEXT(texture,target,level,internalformat,width,border,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureSubImage3DEXT(texture,target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureSubImage2DEXT(texture,target,level,xoffset,yoffset,width,height,format,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTextureSubImage1DEXT(texture,target,level,xoffset,width,format,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,ctypes.c_void_p)
def glGetCompressedTextureImageEXT(texture,target,lod,img):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedMultiTexImage3DEXT(texunit,target,level,internalformat,width,height,depth,border,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedMultiTexImage2DEXT(texunit,target,level,internalformat,width,height,border,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedMultiTexImage1DEXT(texunit,target,level,internalformat,width,border,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedMultiTexSubImage3DEXT(texunit,target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedMultiTexSubImage2DEXT(texunit,target,level,xoffset,yoffset,width,height,format,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedMultiTexSubImage1DEXT(texunit,target,level,xoffset,width,format,imageSize,bits):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,ctypes.c_void_p)
def glGetCompressedMultiTexImageEXT(texunit,target,lod,img):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glNamedProgramStringEXT(program,target,format,len,string):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glNamedProgramLocalParameter4dEXT(program,target,index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLdoubleArray)
def glNamedProgramLocalParameter4dvEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glNamedProgramLocalParameter4fEXT(program,target,index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLfloatArray)
def glNamedProgramLocalParameter4fvEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLdoubleArray)
def glGetNamedProgramLocalParameterdvEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLfloatArray)
def glGetNamedProgramLocalParameterfvEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetNamedProgramivEXT(program,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glGetNamedProgramStringEXT(program,target,pname,string):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glNamedProgramLocalParameters4fvEXT(program,target,index,count,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glNamedProgramLocalParameterI4iEXT(program,target,index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glNamedProgramLocalParameterI4ivEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLintArray)
def glNamedProgramLocalParametersI4ivEXT(program,target,index,count,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glNamedProgramLocalParameterI4uiEXT(program,target,index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLuintArray)
def glNamedProgramLocalParameterI4uivEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glNamedProgramLocalParametersI4uivEXT(program,target,index,count,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLintArray)
def glGetNamedProgramLocalParameterIivEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,arrays.GLuintArray)
def glGetNamedProgramLocalParameterIuivEXT(program,target,index,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTextureParameterIivEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glTextureParameterIuivEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTextureParameterIivEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetTextureParameterIuivEXT(texture,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glMultiTexParameterIivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glMultiTexParameterIuivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetMultiTexParameterIivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetMultiTexParameterIuivEXT(texunit,target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLfloat)
def glProgramUniform1fEXT(program,location,v0):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLfloat,_cs.GLfloat)
def glProgramUniform2fEXT(program,location,v0,v1):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glProgramUniform3fEXT(program,location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glProgramUniform4fEXT(program,location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint)
def glProgramUniform1iEXT(program,location,v0):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint)
def glProgramUniform2iEXT(program,location,v0,v1):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glProgramUniform3iEXT(program,location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glProgramUniform4iEXT(program,location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramUniform1fvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramUniform2fvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramUniform3fvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glProgramUniform4fvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glProgramUniform1ivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glProgramUniform2ivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glProgramUniform3ivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glProgramUniform4ivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix2fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix3fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix4fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix2x3fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix3x2fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix2x4fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix4x2fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix3x4fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glProgramUniformMatrix4x3fvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint)
def glProgramUniform1uiEXT(program,location,v0):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint,_cs.GLuint)
def glProgramUniform2uiEXT(program,location,v0,v1):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glProgramUniform3uiEXT(program,location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint,_cs.GLuint,_cs.GLuint,_cs.GLuint)
def glProgramUniform4uiEXT(program,location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glProgramUniform1uivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glProgramUniform2uivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glProgramUniform3uivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glProgramUniform4uivEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLenum)
def glNamedBufferDataEXT(buffer,size,data,usage):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glNamedBufferSubDataEXT(buffer,offset,size,data):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLuint,_cs.GLenum)
def glMapNamedBufferEXT(buffer,access):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glUnmapNamedBufferEXT(buffer):pass
@_f
@_p.types(ctypes.c_void_p,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr,_cs.GLbitfield)
def glMapNamedBufferRangeEXT(buffer,offset,length,access):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glFlushMappedNamedBufferRangeEXT(buffer,offset,length):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr)
def glNamedCopyBufferSubDataEXT(readBuffer,writeBuffer,readOffset,writeOffset,size):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetNamedBufferParameterivEXT(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLvoidpArray)
def glGetNamedBufferPointervEXT(buffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glGetNamedBufferSubDataEXT(buffer,offset,size,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glTextureBufferEXT(texture,target,internalformat,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glMultiTexBufferEXT(texunit,target,internalformat,buffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glNamedRenderbufferStorageEXT(renderbuffer,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetNamedRenderbufferParameterivEXT(renderbuffer,pname,params):pass
@_f
@_p.types(_cs.GLenum,_cs.GLuint,_cs.GLenum)
def glCheckNamedFramebufferStatusEXT(framebuffer,target):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glNamedFramebufferTexture1DEXT(framebuffer,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glNamedFramebufferTexture2DEXT(framebuffer,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glNamedFramebufferTexture3DEXT(framebuffer,attachment,textarget,texture,level,zoffset):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glNamedFramebufferRenderbufferEXT(framebuffer,attachment,renderbuffertarget,renderbuffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetNamedFramebufferAttachmentParameterivEXT(framebuffer,attachment,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glGenerateTextureMipmapEXT(texture,target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glGenerateMultiTexMipmapEXT(texunit,target):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glFramebufferDrawBufferEXT(framebuffer,mode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray)
def glFramebufferDrawBuffersEXT(framebuffer,n,bufs):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glFramebufferReadBufferEXT(framebuffer,mode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferParameterivEXT(framebuffer,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glNamedRenderbufferStorageMultisampleEXT(renderbuffer,samples,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glNamedRenderbufferStorageMultisampleCoverageEXT(renderbuffer,coverageSamples,colorSamples,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glNamedFramebufferTextureEXT(framebuffer,attachment,texture,level):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glNamedFramebufferTextureLayerEXT(framebuffer,attachment,texture,level,layer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLenum)
def glNamedFramebufferTextureFaceEXT(framebuffer,attachment,texture,level,face):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glTextureRenderbufferEXT(texture,target,renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glMultiTexRenderbufferEXT(texunit,target,renderbuffer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLdouble)
def glProgramUniform1dEXT(program,location,x):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLdouble,_cs.GLdouble)
def glProgramUniform2dEXT(program,location,x,y):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glProgramUniform3dEXT(program,location,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glProgramUniform4dEXT(program,location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glProgramUniform1dvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glProgramUniform2dvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glProgramUniform3dvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glProgramUniform4dvEXT(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix2dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix3dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix4dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix2x3dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix2x4dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix3x2dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix3x4dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix4x2dvEXT(program,location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glProgramUniformMatrix4x3dvEXT(program,location,count,transpose,value):pass


def glInitDirectStateAccessEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

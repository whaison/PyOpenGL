'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_HP_image_transform'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_HP_image_transform')
GL_AVERAGE_HP=_C('GL_AVERAGE_HP',0x8160)
GL_CUBIC_HP=_C('GL_CUBIC_HP',0x815F)
GL_IMAGE_CUBIC_WEIGHT_HP=_C('GL_IMAGE_CUBIC_WEIGHT_HP',0x815E)
GL_IMAGE_MAG_FILTER_HP=_C('GL_IMAGE_MAG_FILTER_HP',0x815C)
GL_IMAGE_MIN_FILTER_HP=_C('GL_IMAGE_MIN_FILTER_HP',0x815D)
GL_IMAGE_ROTATE_ANGLE_HP=_C('GL_IMAGE_ROTATE_ANGLE_HP',0x8159)
GL_IMAGE_ROTATE_ORIGIN_X_HP=_C('GL_IMAGE_ROTATE_ORIGIN_X_HP',0x815A)
GL_IMAGE_ROTATE_ORIGIN_Y_HP=_C('GL_IMAGE_ROTATE_ORIGIN_Y_HP',0x815B)
GL_IMAGE_SCALE_X_HP=_C('GL_IMAGE_SCALE_X_HP',0x8155)
GL_IMAGE_SCALE_Y_HP=_C('GL_IMAGE_SCALE_Y_HP',0x8156)
GL_IMAGE_TRANSFORM_2D_HP=_C('GL_IMAGE_TRANSFORM_2D_HP',0x8161)
GL_IMAGE_TRANSLATE_X_HP=_C('GL_IMAGE_TRANSLATE_X_HP',0x8157)
GL_IMAGE_TRANSLATE_Y_HP=_C('GL_IMAGE_TRANSLATE_Y_HP',0x8158)
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP=_C('GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP',0x8162)
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP=_C('GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP',0x8163)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetImageTransformParameterfvHP(target,pname,params):pass
# Calculate length of params from pname:ImageTransformPNameHP
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetImageTransformParameterivHP(target,pname,params):pass
# Calculate length of params from pname:ImageTransformPNameHP
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glImageTransformParameterfHP(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glImageTransformParameterfvHP(target,pname,params):pass
# Calculate length of params from pname:ImageTransformPNameHP
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glImageTransformParameteriHP(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glImageTransformParameterivHP(target,pname,params):pass
# Calculate length of params from pname:ImageTransformPNameHP

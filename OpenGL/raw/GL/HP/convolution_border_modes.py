'''OpenGL extension HP.convolution_border_modes

Overview (from the spec)
    
    This extension provides some additional border modes for the
    EXT_convolution extension.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/HP/convolution_border_modes.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_HP_convolution_border_modes'
_DEPRECATED = False
GL_IGNORE_BORDER_HP = constant.Constant( 'GL_IGNORE_BORDER_HP', 0x8150 )
GL_CONSTANT_BORDER_HP = constant.Constant( 'GL_CONSTANT_BORDER_HP', 0x8151 )
GL_REPLICATE_BORDER_HP = constant.Constant( 'GL_REPLICATE_BORDER_HP', 0x8153 )
GL_CONVOLUTION_BORDER_COLOR_HP = constant.Constant( 'GL_CONVOLUTION_BORDER_COLOR_HP', 0x8154 )


def glInitConvolutionBorderModesHP():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
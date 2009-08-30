'''OpenGL extension ARB.texture_env_combine

Overview (from the spec)
    
    New texture environment function COMBINE_ARB allows programmable
    texture combiner operations, including:
    
        REPLACE                 Arg0
        MODULATE                Arg0 * Arg1
        ADD                     Arg0 + Arg1
        ADD_SIGNED_ARB          Arg0 + Arg1 - 0.5
        SUBTRACT_ARB            Arg0 - Arg1
        INTERPOLATE_ARB         Arg0 * (Arg2) + Arg1 * (1-Arg2)
    
    where Arg0, Arg1 and Arg2 are derived from
    
        PRIMARY_COLOR_ARB       primary color of incoming fragment
        TEXTURE                 texture color of corresponding texture unit
        CONSTANT_ARB            texture environment constant color
        PREVIOUS_ARB            result of previous texture environment; on
                                texture unit 0, this maps to PRIMARY_COLOR_ARB
    
    In addition, the result may be scaled by 1.0, 2.0 or 4.0.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_env_combine.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_env_combine'
_DEPRECATED = False
GL_COMBINE_ARB = constant.Constant( 'GL_COMBINE_ARB', 0x8570 )
GL_COMBINE_RGB_ARB = constant.Constant( 'GL_COMBINE_RGB_ARB', 0x8571 )
GL_COMBINE_ALPHA_ARB = constant.Constant( 'GL_COMBINE_ALPHA_ARB', 0x8572 )
GL_SOURCE0_RGB_ARB = constant.Constant( 'GL_SOURCE0_RGB_ARB', 0x8580 )
GL_SOURCE1_RGB_ARB = constant.Constant( 'GL_SOURCE1_RGB_ARB', 0x8581 )
GL_SOURCE2_RGB_ARB = constant.Constant( 'GL_SOURCE2_RGB_ARB', 0x8582 )
GL_SOURCE0_ALPHA_ARB = constant.Constant( 'GL_SOURCE0_ALPHA_ARB', 0x8588 )
GL_SOURCE1_ALPHA_ARB = constant.Constant( 'GL_SOURCE1_ALPHA_ARB', 0x8589 )
GL_SOURCE2_ALPHA_ARB = constant.Constant( 'GL_SOURCE2_ALPHA_ARB', 0x858A )
GL_OPERAND0_RGB_ARB = constant.Constant( 'GL_OPERAND0_RGB_ARB', 0x8590 )
GL_OPERAND1_RGB_ARB = constant.Constant( 'GL_OPERAND1_RGB_ARB', 0x8591 )
GL_OPERAND2_RGB_ARB = constant.Constant( 'GL_OPERAND2_RGB_ARB', 0x8592 )
GL_OPERAND0_ALPHA_ARB = constant.Constant( 'GL_OPERAND0_ALPHA_ARB', 0x8598 )
GL_OPERAND1_ALPHA_ARB = constant.Constant( 'GL_OPERAND1_ALPHA_ARB', 0x8599 )
GL_OPERAND2_ALPHA_ARB = constant.Constant( 'GL_OPERAND2_ALPHA_ARB', 0x859A )
GL_RGB_SCALE_ARB = constant.Constant( 'GL_RGB_SCALE_ARB', 0x8573 )
GL_ADD_SIGNED_ARB = constant.Constant( 'GL_ADD_SIGNED_ARB', 0x8574 )
GL_INTERPOLATE_ARB = constant.Constant( 'GL_INTERPOLATE_ARB', 0x8575 )
GL_SUBTRACT_ARB = constant.Constant( 'GL_SUBTRACT_ARB', 0x84E7 )
GL_CONSTANT_ARB = constant.Constant( 'GL_CONSTANT_ARB', 0x8576 )
GL_PRIMARY_COLOR_ARB = constant.Constant( 'GL_PRIMARY_COLOR_ARB', 0x8577 )
GL_PREVIOUS_ARB = constant.Constant( 'GL_PREVIOUS_ARB', 0x8578 )


def glInitTextureEnvCombineARB():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
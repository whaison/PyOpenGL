'''OpenGL extension ATI.draw_buffers

Overview (from the spec)
    
    This extension extends ARB_fragment_program to allow multiple output 
    colors, and provides a mechanism for directing those outputs to 
    multiple color buffers.
    

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/ATI/draw_buffers.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_draw_buffers'
_DEPRECATED = False
GL_MAX_DRAW_BUFFERS_ATI = constant.Constant( 'GL_MAX_DRAW_BUFFERS_ATI', 0x8824 )
glget.addGLGetConstant( GL_MAX_DRAW_BUFFERS_ATI, (1,) )
GL_DRAW_BUFFER0_ATI = constant.Constant( 'GL_DRAW_BUFFER0_ATI', 0x8825 )
GL_DRAW_BUFFER1_ATI = constant.Constant( 'GL_DRAW_BUFFER1_ATI', 0x8826 )
GL_DRAW_BUFFER2_ATI = constant.Constant( 'GL_DRAW_BUFFER2_ATI', 0x8827 )
GL_DRAW_BUFFER3_ATI = constant.Constant( 'GL_DRAW_BUFFER3_ATI', 0x8828 )
GL_DRAW_BUFFER4_ATI = constant.Constant( 'GL_DRAW_BUFFER4_ATI', 0x8829 )
GL_DRAW_BUFFER5_ATI = constant.Constant( 'GL_DRAW_BUFFER5_ATI', 0x882A )
GL_DRAW_BUFFER6_ATI = constant.Constant( 'GL_DRAW_BUFFER6_ATI', 0x882B )
GL_DRAW_BUFFER7_ATI = constant.Constant( 'GL_DRAW_BUFFER7_ATI', 0x882C )
GL_DRAW_BUFFER8_ATI = constant.Constant( 'GL_DRAW_BUFFER8_ATI', 0x882D )
GL_DRAW_BUFFER9_ATI = constant.Constant( 'GL_DRAW_BUFFER9_ATI', 0x882E )
GL_DRAW_BUFFER10_ATI = constant.Constant( 'GL_DRAW_BUFFER10_ATI', 0x882F )
GL_DRAW_BUFFER11_ATI = constant.Constant( 'GL_DRAW_BUFFER11_ATI', 0x8830 )
GL_DRAW_BUFFER12_ATI = constant.Constant( 'GL_DRAW_BUFFER12_ATI', 0x8831 )
GL_DRAW_BUFFER13_ATI = constant.Constant( 'GL_DRAW_BUFFER13_ATI', 0x8832 )
GL_DRAW_BUFFER14_ATI = constant.Constant( 'GL_DRAW_BUFFER14_ATI', 0x8833 )
GL_DRAW_BUFFER15_ATI = constant.Constant( 'GL_DRAW_BUFFER15_ATI', 0x8834 )
glDrawBuffersATI = platform.createExtensionFunction( 
'glDrawBuffersATI',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLsizei,arrays.GLuintArray,),
doc='glDrawBuffersATI(GLsizei(n), GLuintArray(bufs)) -> None',
argNames=('n','bufs',),
deprecated=_DEPRECATED,
)


def glInitDrawBuffersATI():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
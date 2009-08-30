'''OpenGL extension EXT.misc_attribute

Overview (from the spec)
    
    EXT_misc_attribute extends the list of attribute groups. It provides
    a miscellaneous group, controlled by the MISC_BIT_EXT bit, that contains
    the attribute state of extensions that don't logically fit in any other
    group. 

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/EXT/misc_attribute.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_misc_attribute'
_DEPRECATED = False



def glInitMiscAttributeEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
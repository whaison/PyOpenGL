'''OpenGL extension OML.subsample

Overview (from the spec)
    
    Many video image formats and compression techniques utilize various
    component subsamplings, so it is necessary to provide a mechanism to
    specify the up- and down-sampling of components as pixel data is
    drawn from and read back to the client. Though subsampled components
    are normally associated with the video color space, YCrCb, use of
    subsampling in OpenGL does not imply a specific color space. Color
    space conversion may be performed using other extensions or core
    capabilities such as the color matrix.
    
    This extension defines two new pixel storage formats representing
    subsampled data on the client. It is loosely based on the
    SGIX_subsample extension, but specifies subsampling with the data
    format parameter rather than pixel packing parameters. It also
    adds support for CYA subsampled data.
    
    When pixel data is received from the client and an unpacking
    upsampling mode other than PIXEL_SUBSAMPLE_NONE_OML is specified,
    upsampling is performed via replication, unless otherwise specified
    by UNPACK_RESAMPLE_OML.
    
    Similarly, when pixel data is read back to the client and a packing
    downsampling mode other than PIXEL_SUBSAMPLE_NONE_OML is specified,
    downsampling is performed via simple component decimation (point
    sampling), unless otherwise specified by PACK_RESAMPLE_OML.

The official definition of this extension is available here:
http://oss.sgi.com/projects/ogl-sample/registry/OML/subsample.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_OML_subsample'
_DEPRECATED = False
GL_FORMAT_SUBSAMPLE_24_24_OML = constant.Constant( 'GL_FORMAT_SUBSAMPLE_24_24_OML', 0x8982 )
GL_FORMAT_SUBSAMPLE_244_244_OML = constant.Constant( 'GL_FORMAT_SUBSAMPLE_244_244_OML', 0x8983 )


def glInitSubsampleOML():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
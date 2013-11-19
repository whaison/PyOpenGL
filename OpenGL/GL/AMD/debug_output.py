'''OpenGL extension AMD.debug_output

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.debug_output to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows the GL to notify applications when various
	debug events occur in contexts that have been created with the debug
	flag, as provided by WGL_ARB_create_context and GLX_ARB_create_context.
	
	These events are represented in the form of enumerable messages with an
	included human-readable translation.  Examples of debug events include
	incorrect use of the GL, warnings of undefined behavior, and performance
	warnings.
	
	A message is uniquely identified by a category and an implementation-
	dependent ID within that category.  Message categories are general and are
	used to organize large groups of similar messages together.  Examples of
	categories include GL errors, performance warnings, and deprecated
	functionality warnings.  Each message is also assigned a severity level
	that denotes roughly how "important" that message is in comparison to
	other messages across all categories.  For example, notification of a GL
	error would have a higher severity than a performance warning due to
	redundant state changes.
	
	Messages are communicated to the application through an application-defined
	callback function that is called by the GL implementation on each debug
	message.  The motivation for the callback routine is to free application
	developers from actively having to query whether any GL error or other
	debuggable event has happened after each call to a GL function.  With a
	callback, developers can keep their code free of debug checks, and only have
	to react to messages as they occur.  In order to support indirect rendering,
	a message log is also provided that stores copies of recent messages until
	they are actively queried.
	
	To control the volume of debug output, messages can be disabled either
	individually by ID, or entire groups of messages can be turned off based
	on category or severity.
	
	The only requirement on the minimum quantity and type of messages that
	implementations of this extension must support is that a message must be
	sent notifying the application whenever any GL error occurs.  Any further
	messages are left to the implementation.  Implementations do not have
	to output messages from all categories listed by this extension
	in order to support this extension, and new categories can be added by
	other extensions.
	
	This extension places no restrictions or requirements on any additional
	functionality provided by the debug context flag through other extensions. 

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/debug_output.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.debug_output import *

def glInitDebugOutputAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
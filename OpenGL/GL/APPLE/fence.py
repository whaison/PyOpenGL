'''OpenGL extension APPLE.fence

This module customises the behaviour of the 
OpenGL.raw.GL.APPLE.fence to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension is provided a finer granularity of synchronizing GL command
	completion than offered by standard OpenGL, which currently offers only two
	mechanisms for synchronization: Flush and Finish. Since Flush merely assures
	the user that the commands complete in a finite (though undetermined) amount
	of time, it is, thus, of only modest utility.  Finish, on the other hand,
	stalls CPU execution until all pending GL commands have completed forcing
	completely synchronous operation, which most often not the desired result.
	This extension offers a middle ground - the ability to "finish" a subset of
	the command stream, and the ability to determine whether a given command has
	completed or not.
	
	This extension introduces the concept of a "fence" to the OpenGL command
	stream with SetFenceAPPLE.  Once the fence is inserted into the command
	stream, it can be tested for its completion with TestFenceAPPLE. Moreover,
	the application may also request a partial Finish up to a particular "fence"
	using the FinishFenceAPPLE command -- that is, all commands prior to the
	fence will be forced to complete until control is returned to the calling
	process.  These new mechanisms allow for synchronization between the host
	CPU and the GPU, which may be accessing the same resources (typically
	memory).
	
	Fences are created and deleted, as are other objects in OpenGL, specifically
	with GenFencesAPPLE and DeleteFencesAPPLE.  The former returns a list of
	unused fence names and the later deletes the provided list of fence names.
	
	In addition to being able to test or finish a fence this extension allows
	testing for other types of completion, including texture objects, vertex
	array objects, and draw pixels. This allows the client to use
	TestObjectAPPLE or FinishObjectAPPLE with FENCE_APPLE, TEXTURE,
	VERTEX_ARRAY, or DRAW_PIXELS_APPLE with the same type of results as
	TestFenceAPPLE and FinishFenceAPPLE.  Specifically, using the FENCE_APPLE
	type is equivalent to calling TestFenceAPPLE or FinishFenceAPPLE with the
	particular fence name.  Using TEXTURE as the object type tests or waits for
	completion of a specific texture, meaning when there are no pending
	rendering commands which use that texture object. Using the VERTEX_ARRAY
	type will test or wait for drawing commands using that particular vertex
	array object name.  Finally, DRAW_PIXELS_APPLE will wait or test for
	completion of all pending DrawPixels commands.  These tests and finishes
	operate with the same limitations and results as test and finish fence.
	
	One use of this extension is in conjunction with APPLE_vertex_array_range to
	determine when graphics hardware has completed accessing vertex data from a
	vertex array range.  Once a fence has been tested TRUE or finished, all
	vertex indices issued before the fence must have completed being accessed.
	This ensures that the vertex data memory corresponding to the issued vertex
	indices can be safely modified (assuming no other outstanding vertex indices
	are issued subsequent to the fence).

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/APPLE/fence.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.APPLE.fence import *

def glInitFenceAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
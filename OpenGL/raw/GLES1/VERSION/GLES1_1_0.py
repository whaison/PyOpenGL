'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GLES1 import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLES1_VERSION_GLES1_1_0'
def _f( function ):
    return _p.createFunction( function,_p.GLES1,'GLES1_VERSION_GLES1_1_0')
GL_ACTIVE_TEXTURE=_C('GL_ACTIVE_TEXTURE',0x84E0)
GL_ADD=_C('GL_ADD',0x0104)
GL_ADD_SIGNED=_C('GL_ADD_SIGNED',0x8574)
GL_ALIASED_LINE_WIDTH_RANGE=_C('GL_ALIASED_LINE_WIDTH_RANGE',0x846E)
GL_ALIASED_POINT_SIZE_RANGE=_C('GL_ALIASED_POINT_SIZE_RANGE',0x846D)
GL_ALPHA=_C('GL_ALPHA',0x1906)
GL_ALPHA_BITS=_C('GL_ALPHA_BITS',0x0D55)
GL_ALPHA_SCALE=_C('GL_ALPHA_SCALE',0x0D1C)
GL_ALPHA_TEST=_C('GL_ALPHA_TEST',0x0BC0)
GL_ALPHA_TEST_FUNC=_C('GL_ALPHA_TEST_FUNC',0x0BC1)
GL_ALPHA_TEST_REF=_C('GL_ALPHA_TEST_REF',0x0BC2)
GL_ALWAYS=_C('GL_ALWAYS',0x0207)
GL_AMBIENT=_C('GL_AMBIENT',0x1200)
GL_AMBIENT_AND_DIFFUSE=_C('GL_AMBIENT_AND_DIFFUSE',0x1602)
GL_AND=_C('GL_AND',0x1501)
GL_AND_INVERTED=_C('GL_AND_INVERTED',0x1504)
GL_AND_REVERSE=_C('GL_AND_REVERSE',0x1502)
GL_ARRAY_BUFFER=_C('GL_ARRAY_BUFFER',0x8892)
GL_ARRAY_BUFFER_BINDING=_C('GL_ARRAY_BUFFER_BINDING',0x8894)
GL_BACK=_C('GL_BACK',0x0405)
GL_BLEND=_C('GL_BLEND',0x0BE2)
GL_BLEND_DST=_C('GL_BLEND_DST',0x0BE0)
GL_BLEND_SRC=_C('GL_BLEND_SRC',0x0BE1)
GL_BLUE_BITS=_C('GL_BLUE_BITS',0x0D54)
GL_BUFFER_SIZE=_C('GL_BUFFER_SIZE',0x8764)
GL_BUFFER_USAGE=_C('GL_BUFFER_USAGE',0x8765)
GL_BYTE=_C('GL_BYTE',0x1400)
GL_CCW=_C('GL_CCW',0x0901)
GL_CLAMP_TO_EDGE=_C('GL_CLAMP_TO_EDGE',0x812F)
GL_CLEAR=_C('GL_CLEAR',0x1500)
GL_CLIENT_ACTIVE_TEXTURE=_C('GL_CLIENT_ACTIVE_TEXTURE',0x84E1)
GL_CLIP_PLANE0=_C('GL_CLIP_PLANE0',0x3000)
GL_CLIP_PLANE1=_C('GL_CLIP_PLANE1',0x3001)
GL_CLIP_PLANE2=_C('GL_CLIP_PLANE2',0x3002)
GL_CLIP_PLANE3=_C('GL_CLIP_PLANE3',0x3003)
GL_CLIP_PLANE4=_C('GL_CLIP_PLANE4',0x3004)
GL_CLIP_PLANE5=_C('GL_CLIP_PLANE5',0x3005)
GL_COLOR_ARRAY=_C('GL_COLOR_ARRAY',0x8076)
GL_COLOR_ARRAY_BUFFER_BINDING=_C('GL_COLOR_ARRAY_BUFFER_BINDING',0x8898)
GL_COLOR_ARRAY_POINTER=_C('GL_COLOR_ARRAY_POINTER',0x8090)
GL_COLOR_ARRAY_SIZE=_C('GL_COLOR_ARRAY_SIZE',0x8081)
GL_COLOR_ARRAY_STRIDE=_C('GL_COLOR_ARRAY_STRIDE',0x8083)
GL_COLOR_ARRAY_TYPE=_C('GL_COLOR_ARRAY_TYPE',0x8082)
GL_COLOR_BUFFER_BIT=_C('GL_COLOR_BUFFER_BIT',0x00004000)
GL_COLOR_CLEAR_VALUE=_C('GL_COLOR_CLEAR_VALUE',0x0C22)
GL_COLOR_LOGIC_OP=_C('GL_COLOR_LOGIC_OP',0x0BF2)
GL_COLOR_MATERIAL=_C('GL_COLOR_MATERIAL',0x0B57)
GL_COLOR_WRITEMASK=_C('GL_COLOR_WRITEMASK',0x0C23)
GL_COMBINE=_C('GL_COMBINE',0x8570)
GL_COMBINE_ALPHA=_C('GL_COMBINE_ALPHA',0x8572)
GL_COMBINE_RGB=_C('GL_COMBINE_RGB',0x8571)
GL_COMPRESSED_TEXTURE_FORMATS=_C('GL_COMPRESSED_TEXTURE_FORMATS',0x86A3)
GL_CONSTANT=_C('GL_CONSTANT',0x8576)
GL_CONSTANT_ATTENUATION=_C('GL_CONSTANT_ATTENUATION',0x1207)
GL_COPY=_C('GL_COPY',0x1503)
GL_COPY_INVERTED=_C('GL_COPY_INVERTED',0x150C)
GL_CULL_FACE=_C('GL_CULL_FACE',0x0B44)
GL_CULL_FACE_MODE=_C('GL_CULL_FACE_MODE',0x0B45)
GL_CURRENT_COLOR=_C('GL_CURRENT_COLOR',0x0B00)
GL_CURRENT_NORMAL=_C('GL_CURRENT_NORMAL',0x0B02)
GL_CURRENT_TEXTURE_COORDS=_C('GL_CURRENT_TEXTURE_COORDS',0x0B03)
GL_CW=_C('GL_CW',0x0900)
GL_DECAL=_C('GL_DECAL',0x2101)
GL_DECR=_C('GL_DECR',0x1E03)
GL_DEPTH_BITS=_C('GL_DEPTH_BITS',0x0D56)
GL_DEPTH_BUFFER_BIT=_C('GL_DEPTH_BUFFER_BIT',0x00000100)
GL_DEPTH_CLEAR_VALUE=_C('GL_DEPTH_CLEAR_VALUE',0x0B73)
GL_DEPTH_FUNC=_C('GL_DEPTH_FUNC',0x0B74)
GL_DEPTH_RANGE=_C('GL_DEPTH_RANGE',0x0B70)
GL_DEPTH_TEST=_C('GL_DEPTH_TEST',0x0B71)
GL_DEPTH_WRITEMASK=_C('GL_DEPTH_WRITEMASK',0x0B72)
GL_DIFFUSE=_C('GL_DIFFUSE',0x1201)
GL_DITHER=_C('GL_DITHER',0x0BD0)
GL_DONT_CARE=_C('GL_DONT_CARE',0x1100)
GL_DOT3_RGB=_C('GL_DOT3_RGB',0x86AE)
GL_DOT3_RGBA=_C('GL_DOT3_RGBA',0x86AF)
GL_DST_ALPHA=_C('GL_DST_ALPHA',0x0304)
GL_DST_COLOR=_C('GL_DST_COLOR',0x0306)
GL_DYNAMIC_DRAW=_C('GL_DYNAMIC_DRAW',0x88E8)
GL_ELEMENT_ARRAY_BUFFER=_C('GL_ELEMENT_ARRAY_BUFFER',0x8893)
GL_ELEMENT_ARRAY_BUFFER_BINDING=_C('GL_ELEMENT_ARRAY_BUFFER_BINDING',0x8895)
GL_EMISSION=_C('GL_EMISSION',0x1600)
GL_EQUAL=_C('GL_EQUAL',0x0202)
GL_EQUIV=_C('GL_EQUIV',0x1509)
GL_EXP=_C('GL_EXP',0x0800)
GL_EXP2=_C('GL_EXP2',0x0801)
GL_EXTENSIONS=_C('GL_EXTENSIONS',0x1F03)
GL_FALSE=_C('GL_FALSE',0)
GL_FASTEST=_C('GL_FASTEST',0x1101)
GL_FIXED=_C('GL_FIXED',0x140C)
GL_FLAT=_C('GL_FLAT',0x1D00)
GL_FLOAT=_C('GL_FLOAT',0x1406)
GL_FOG=_C('GL_FOG',0x0B60)
GL_FOG_COLOR=_C('GL_FOG_COLOR',0x0B66)
GL_FOG_DENSITY=_C('GL_FOG_DENSITY',0x0B62)
GL_FOG_END=_C('GL_FOG_END',0x0B64)
GL_FOG_HINT=_C('GL_FOG_HINT',0x0C54)
GL_FOG_MODE=_C('GL_FOG_MODE',0x0B65)
GL_FOG_START=_C('GL_FOG_START',0x0B63)
GL_FRONT=_C('GL_FRONT',0x0404)
GL_FRONT_AND_BACK=_C('GL_FRONT_AND_BACK',0x0408)
GL_FRONT_FACE=_C('GL_FRONT_FACE',0x0B46)
GL_GENERATE_MIPMAP=_C('GL_GENERATE_MIPMAP',0x8191)
GL_GENERATE_MIPMAP_HINT=_C('GL_GENERATE_MIPMAP_HINT',0x8192)
GL_GEQUAL=_C('GL_GEQUAL',0x0206)
GL_GREATER=_C('GL_GREATER',0x0204)
GL_GREEN_BITS=_C('GL_GREEN_BITS',0x0D53)
GL_INCR=_C('GL_INCR',0x1E02)
GL_INTERPOLATE=_C('GL_INTERPOLATE',0x8575)
GL_INVALID_ENUM=_C('GL_INVALID_ENUM',0x0500)
GL_INVALID_OPERATION=_C('GL_INVALID_OPERATION',0x0502)
GL_INVALID_VALUE=_C('GL_INVALID_VALUE',0x0501)
GL_INVERT=_C('GL_INVERT',0x150A)
GL_KEEP=_C('GL_KEEP',0x1E00)
GL_LEQUAL=_C('GL_LEQUAL',0x0203)
GL_LESS=_C('GL_LESS',0x0201)
GL_LIGHT0=_C('GL_LIGHT0',0x4000)
GL_LIGHT1=_C('GL_LIGHT1',0x4001)
GL_LIGHT2=_C('GL_LIGHT2',0x4002)
GL_LIGHT3=_C('GL_LIGHT3',0x4003)
GL_LIGHT4=_C('GL_LIGHT4',0x4004)
GL_LIGHT5=_C('GL_LIGHT5',0x4005)
GL_LIGHT6=_C('GL_LIGHT6',0x4006)
GL_LIGHT7=_C('GL_LIGHT7',0x4007)
GL_LIGHTING=_C('GL_LIGHTING',0x0B50)
GL_LIGHT_MODEL_AMBIENT=_C('GL_LIGHT_MODEL_AMBIENT',0x0B53)
GL_LIGHT_MODEL_TWO_SIDE=_C('GL_LIGHT_MODEL_TWO_SIDE',0x0B52)
GL_LINEAR=_C('GL_LINEAR',0x2601)
GL_LINEAR_ATTENUATION=_C('GL_LINEAR_ATTENUATION',0x1208)
GL_LINEAR_MIPMAP_LINEAR=_C('GL_LINEAR_MIPMAP_LINEAR',0x2703)
GL_LINEAR_MIPMAP_NEAREST=_C('GL_LINEAR_MIPMAP_NEAREST',0x2701)
GL_LINES=_C('GL_LINES',0x0001)
GL_LINE_LOOP=_C('GL_LINE_LOOP',0x0002)
GL_LINE_SMOOTH=_C('GL_LINE_SMOOTH',0x0B20)
GL_LINE_SMOOTH_HINT=_C('GL_LINE_SMOOTH_HINT',0x0C52)
GL_LINE_STRIP=_C('GL_LINE_STRIP',0x0003)
GL_LINE_WIDTH=_C('GL_LINE_WIDTH',0x0B21)
GL_LOGIC_OP_MODE=_C('GL_LOGIC_OP_MODE',0x0BF0)
GL_LUMINANCE=_C('GL_LUMINANCE',0x1909)
GL_LUMINANCE_ALPHA=_C('GL_LUMINANCE_ALPHA',0x190A)
GL_MATRIX_MODE=_C('GL_MATRIX_MODE',0x0BA0)
GL_MAX_CLIP_PLANES=_C('GL_MAX_CLIP_PLANES',0x0D32)
GL_MAX_LIGHTS=_C('GL_MAX_LIGHTS',0x0D31)
GL_MAX_MODELVIEW_STACK_DEPTH=_C('GL_MAX_MODELVIEW_STACK_DEPTH',0x0D36)
GL_MAX_PROJECTION_STACK_DEPTH=_C('GL_MAX_PROJECTION_STACK_DEPTH',0x0D38)
GL_MAX_TEXTURE_SIZE=_C('GL_MAX_TEXTURE_SIZE',0x0D33)
GL_MAX_TEXTURE_STACK_DEPTH=_C('GL_MAX_TEXTURE_STACK_DEPTH',0x0D39)
GL_MAX_TEXTURE_UNITS=_C('GL_MAX_TEXTURE_UNITS',0x84E2)
GL_MAX_VIEWPORT_DIMS=_C('GL_MAX_VIEWPORT_DIMS',0x0D3A)
GL_MODELVIEW=_C('GL_MODELVIEW',0x1700)
GL_MODELVIEW_MATRIX=_C('GL_MODELVIEW_MATRIX',0x0BA6)
GL_MODELVIEW_STACK_DEPTH=_C('GL_MODELVIEW_STACK_DEPTH',0x0BA3)
GL_MODULATE=_C('GL_MODULATE',0x2100)
GL_MULTISAMPLE=_C('GL_MULTISAMPLE',0x809D)
GL_NAND=_C('GL_NAND',0x150E)
GL_NEAREST=_C('GL_NEAREST',0x2600)
GL_NEAREST_MIPMAP_LINEAR=_C('GL_NEAREST_MIPMAP_LINEAR',0x2702)
GL_NEAREST_MIPMAP_NEAREST=_C('GL_NEAREST_MIPMAP_NEAREST',0x2700)
GL_NEVER=_C('GL_NEVER',0x0200)
GL_NICEST=_C('GL_NICEST',0x1102)
GL_NOOP=_C('GL_NOOP',0x1505)
GL_NOR=_C('GL_NOR',0x1508)
GL_NORMALIZE=_C('GL_NORMALIZE',0x0BA1)
GL_NORMAL_ARRAY=_C('GL_NORMAL_ARRAY',0x8075)
GL_NORMAL_ARRAY_BUFFER_BINDING=_C('GL_NORMAL_ARRAY_BUFFER_BINDING',0x8897)
GL_NORMAL_ARRAY_POINTER=_C('GL_NORMAL_ARRAY_POINTER',0x808F)
GL_NORMAL_ARRAY_STRIDE=_C('GL_NORMAL_ARRAY_STRIDE',0x807F)
GL_NORMAL_ARRAY_TYPE=_C('GL_NORMAL_ARRAY_TYPE',0x807E)
GL_NOTEQUAL=_C('GL_NOTEQUAL',0x0205)
GL_NO_ERROR=_C('GL_NO_ERROR',0)
GL_NUM_COMPRESSED_TEXTURE_FORMATS=_C('GL_NUM_COMPRESSED_TEXTURE_FORMATS',0x86A2)
GL_ONE=_C('GL_ONE',1)
GL_ONE_MINUS_DST_ALPHA=_C('GL_ONE_MINUS_DST_ALPHA',0x0305)
GL_ONE_MINUS_DST_COLOR=_C('GL_ONE_MINUS_DST_COLOR',0x0307)
GL_ONE_MINUS_SRC_ALPHA=_C('GL_ONE_MINUS_SRC_ALPHA',0x0303)
GL_ONE_MINUS_SRC_COLOR=_C('GL_ONE_MINUS_SRC_COLOR',0x0301)
GL_OPERAND0_ALPHA=_C('GL_OPERAND0_ALPHA',0x8598)
GL_OPERAND0_RGB=_C('GL_OPERAND0_RGB',0x8590)
GL_OPERAND1_ALPHA=_C('GL_OPERAND1_ALPHA',0x8599)
GL_OPERAND1_RGB=_C('GL_OPERAND1_RGB',0x8591)
GL_OPERAND2_ALPHA=_C('GL_OPERAND2_ALPHA',0x859A)
GL_OPERAND2_RGB=_C('GL_OPERAND2_RGB',0x8592)
GL_OR=_C('GL_OR',0x1507)
GL_OR_INVERTED=_C('GL_OR_INVERTED',0x150D)
GL_OR_REVERSE=_C('GL_OR_REVERSE',0x150B)
GL_OUT_OF_MEMORY=_C('GL_OUT_OF_MEMORY',0x0505)
GL_PACK_ALIGNMENT=_C('GL_PACK_ALIGNMENT',0x0D05)
GL_PERSPECTIVE_CORRECTION_HINT=_C('GL_PERSPECTIVE_CORRECTION_HINT',0x0C50)
GL_POINTS=_C('GL_POINTS',0x0000)
GL_POINT_DISTANCE_ATTENUATION=_C('GL_POINT_DISTANCE_ATTENUATION',0x8129)
GL_POINT_FADE_THRESHOLD_SIZE=_C('GL_POINT_FADE_THRESHOLD_SIZE',0x8128)
GL_POINT_SIZE=_C('GL_POINT_SIZE',0x0B11)
GL_POINT_SIZE_MAX=_C('GL_POINT_SIZE_MAX',0x8127)
GL_POINT_SIZE_MIN=_C('GL_POINT_SIZE_MIN',0x8126)
GL_POINT_SMOOTH=_C('GL_POINT_SMOOTH',0x0B10)
GL_POINT_SMOOTH_HINT=_C('GL_POINT_SMOOTH_HINT',0x0C51)
GL_POLYGON_OFFSET_FACTOR=_C('GL_POLYGON_OFFSET_FACTOR',0x8038)
GL_POLYGON_OFFSET_FILL=_C('GL_POLYGON_OFFSET_FILL',0x8037)
GL_POLYGON_OFFSET_UNITS=_C('GL_POLYGON_OFFSET_UNITS',0x2A00)
GL_POSITION=_C('GL_POSITION',0x1203)
GL_PREVIOUS=_C('GL_PREVIOUS',0x8578)
GL_PRIMARY_COLOR=_C('GL_PRIMARY_COLOR',0x8577)
GL_PROJECTION=_C('GL_PROJECTION',0x1701)
GL_PROJECTION_MATRIX=_C('GL_PROJECTION_MATRIX',0x0BA7)
GL_PROJECTION_STACK_DEPTH=_C('GL_PROJECTION_STACK_DEPTH',0x0BA4)
GL_QUADRATIC_ATTENUATION=_C('GL_QUADRATIC_ATTENUATION',0x1209)
GL_RED_BITS=_C('GL_RED_BITS',0x0D52)
GL_RENDERER=_C('GL_RENDERER',0x1F01)
GL_REPEAT=_C('GL_REPEAT',0x2901)
GL_REPLACE=_C('GL_REPLACE',0x1E01)
GL_RESCALE_NORMAL=_C('GL_RESCALE_NORMAL',0x803A)
GL_RGB=_C('GL_RGB',0x1907)
GL_RGBA=_C('GL_RGBA',0x1908)
GL_RGB_SCALE=_C('GL_RGB_SCALE',0x8573)
GL_SAMPLES=_C('GL_SAMPLES',0x80A9)
GL_SAMPLE_ALPHA_TO_COVERAGE=_C('GL_SAMPLE_ALPHA_TO_COVERAGE',0x809E)
GL_SAMPLE_ALPHA_TO_ONE=_C('GL_SAMPLE_ALPHA_TO_ONE',0x809F)
GL_SAMPLE_BUFFERS=_C('GL_SAMPLE_BUFFERS',0x80A8)
GL_SAMPLE_COVERAGE=_C('GL_SAMPLE_COVERAGE',0x80A0)
GL_SAMPLE_COVERAGE_INVERT=_C('GL_SAMPLE_COVERAGE_INVERT',0x80AB)
GL_SAMPLE_COVERAGE_VALUE=_C('GL_SAMPLE_COVERAGE_VALUE',0x80AA)
GL_SCISSOR_BOX=_C('GL_SCISSOR_BOX',0x0C10)
GL_SCISSOR_TEST=_C('GL_SCISSOR_TEST',0x0C11)
GL_SET=_C('GL_SET',0x150F)
GL_SHADE_MODEL=_C('GL_SHADE_MODEL',0x0B54)
GL_SHININESS=_C('GL_SHININESS',0x1601)
GL_SHORT=_C('GL_SHORT',0x1402)
GL_SMOOTH=_C('GL_SMOOTH',0x1D01)
GL_SMOOTH_LINE_WIDTH_RANGE=_C('GL_SMOOTH_LINE_WIDTH_RANGE',0x0B22)
GL_SMOOTH_POINT_SIZE_RANGE=_C('GL_SMOOTH_POINT_SIZE_RANGE',0x0B12)
GL_SPECULAR=_C('GL_SPECULAR',0x1202)
GL_SPOT_CUTOFF=_C('GL_SPOT_CUTOFF',0x1206)
GL_SPOT_DIRECTION=_C('GL_SPOT_DIRECTION',0x1204)
GL_SPOT_EXPONENT=_C('GL_SPOT_EXPONENT',0x1205)
GL_SRC0_ALPHA=_C('GL_SRC0_ALPHA',0x8588)
GL_SRC0_RGB=_C('GL_SRC0_RGB',0x8580)
GL_SRC1_ALPHA=_C('GL_SRC1_ALPHA',0x8589)
GL_SRC1_RGB=_C('GL_SRC1_RGB',0x8581)
GL_SRC2_ALPHA=_C('GL_SRC2_ALPHA',0x858A)
GL_SRC2_RGB=_C('GL_SRC2_RGB',0x8582)
GL_SRC_ALPHA=_C('GL_SRC_ALPHA',0x0302)
GL_SRC_ALPHA_SATURATE=_C('GL_SRC_ALPHA_SATURATE',0x0308)
GL_SRC_COLOR=_C('GL_SRC_COLOR',0x0300)
GL_STACK_OVERFLOW=_C('GL_STACK_OVERFLOW',0x0503)
GL_STACK_UNDERFLOW=_C('GL_STACK_UNDERFLOW',0x0504)
GL_STATIC_DRAW=_C('GL_STATIC_DRAW',0x88E4)
GL_STENCIL_BITS=_C('GL_STENCIL_BITS',0x0D57)
GL_STENCIL_BUFFER_BIT=_C('GL_STENCIL_BUFFER_BIT',0x00000400)
GL_STENCIL_CLEAR_VALUE=_C('GL_STENCIL_CLEAR_VALUE',0x0B91)
GL_STENCIL_FAIL=_C('GL_STENCIL_FAIL',0x0B94)
GL_STENCIL_FUNC=_C('GL_STENCIL_FUNC',0x0B92)
GL_STENCIL_PASS_DEPTH_FAIL=_C('GL_STENCIL_PASS_DEPTH_FAIL',0x0B95)
GL_STENCIL_PASS_DEPTH_PASS=_C('GL_STENCIL_PASS_DEPTH_PASS',0x0B96)
GL_STENCIL_REF=_C('GL_STENCIL_REF',0x0B97)
GL_STENCIL_TEST=_C('GL_STENCIL_TEST',0x0B90)
GL_STENCIL_VALUE_MASK=_C('GL_STENCIL_VALUE_MASK',0x0B93)
GL_STENCIL_WRITEMASK=_C('GL_STENCIL_WRITEMASK',0x0B98)
GL_SUBPIXEL_BITS=_C('GL_SUBPIXEL_BITS',0x0D50)
GL_SUBTRACT=_C('GL_SUBTRACT',0x84E7)
GL_TEXTURE=_C('GL_TEXTURE',0x1702)
GL_TEXTURE0=_C('GL_TEXTURE0',0x84C0)
GL_TEXTURE1=_C('GL_TEXTURE1',0x84C1)
GL_TEXTURE10=_C('GL_TEXTURE10',0x84CA)
GL_TEXTURE11=_C('GL_TEXTURE11',0x84CB)
GL_TEXTURE12=_C('GL_TEXTURE12',0x84CC)
GL_TEXTURE13=_C('GL_TEXTURE13',0x84CD)
GL_TEXTURE14=_C('GL_TEXTURE14',0x84CE)
GL_TEXTURE15=_C('GL_TEXTURE15',0x84CF)
GL_TEXTURE16=_C('GL_TEXTURE16',0x84D0)
GL_TEXTURE17=_C('GL_TEXTURE17',0x84D1)
GL_TEXTURE18=_C('GL_TEXTURE18',0x84D2)
GL_TEXTURE19=_C('GL_TEXTURE19',0x84D3)
GL_TEXTURE2=_C('GL_TEXTURE2',0x84C2)
GL_TEXTURE20=_C('GL_TEXTURE20',0x84D4)
GL_TEXTURE21=_C('GL_TEXTURE21',0x84D5)
GL_TEXTURE22=_C('GL_TEXTURE22',0x84D6)
GL_TEXTURE23=_C('GL_TEXTURE23',0x84D7)
GL_TEXTURE24=_C('GL_TEXTURE24',0x84D8)
GL_TEXTURE25=_C('GL_TEXTURE25',0x84D9)
GL_TEXTURE26=_C('GL_TEXTURE26',0x84DA)
GL_TEXTURE27=_C('GL_TEXTURE27',0x84DB)
GL_TEXTURE28=_C('GL_TEXTURE28',0x84DC)
GL_TEXTURE29=_C('GL_TEXTURE29',0x84DD)
GL_TEXTURE3=_C('GL_TEXTURE3',0x84C3)
GL_TEXTURE30=_C('GL_TEXTURE30',0x84DE)
GL_TEXTURE31=_C('GL_TEXTURE31',0x84DF)
GL_TEXTURE4=_C('GL_TEXTURE4',0x84C4)
GL_TEXTURE5=_C('GL_TEXTURE5',0x84C5)
GL_TEXTURE6=_C('GL_TEXTURE6',0x84C6)
GL_TEXTURE7=_C('GL_TEXTURE7',0x84C7)
GL_TEXTURE8=_C('GL_TEXTURE8',0x84C8)
GL_TEXTURE9=_C('GL_TEXTURE9',0x84C9)
GL_TEXTURE_2D=_C('GL_TEXTURE_2D',0x0DE1)
GL_TEXTURE_BINDING_2D=_C('GL_TEXTURE_BINDING_2D',0x8069)
GL_TEXTURE_COORD_ARRAY=_C('GL_TEXTURE_COORD_ARRAY',0x8078)
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING=_C('GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING',0x889A)
GL_TEXTURE_COORD_ARRAY_POINTER=_C('GL_TEXTURE_COORD_ARRAY_POINTER',0x8092)
GL_TEXTURE_COORD_ARRAY_SIZE=_C('GL_TEXTURE_COORD_ARRAY_SIZE',0x8088)
GL_TEXTURE_COORD_ARRAY_STRIDE=_C('GL_TEXTURE_COORD_ARRAY_STRIDE',0x808A)
GL_TEXTURE_COORD_ARRAY_TYPE=_C('GL_TEXTURE_COORD_ARRAY_TYPE',0x8089)
GL_TEXTURE_ENV=_C('GL_TEXTURE_ENV',0x2300)
GL_TEXTURE_ENV_COLOR=_C('GL_TEXTURE_ENV_COLOR',0x2201)
GL_TEXTURE_ENV_MODE=_C('GL_TEXTURE_ENV_MODE',0x2200)
GL_TEXTURE_MAG_FILTER=_C('GL_TEXTURE_MAG_FILTER',0x2800)
GL_TEXTURE_MATRIX=_C('GL_TEXTURE_MATRIX',0x0BA8)
GL_TEXTURE_MIN_FILTER=_C('GL_TEXTURE_MIN_FILTER',0x2801)
GL_TEXTURE_STACK_DEPTH=_C('GL_TEXTURE_STACK_DEPTH',0x0BA5)
GL_TEXTURE_WRAP_S=_C('GL_TEXTURE_WRAP_S',0x2802)
GL_TEXTURE_WRAP_T=_C('GL_TEXTURE_WRAP_T',0x2803)
GL_TRIANGLES=_C('GL_TRIANGLES',0x0004)
GL_TRIANGLE_FAN=_C('GL_TRIANGLE_FAN',0x0006)
GL_TRIANGLE_STRIP=_C('GL_TRIANGLE_STRIP',0x0005)
GL_TRUE=_C('GL_TRUE',1)
GL_UNPACK_ALIGNMENT=_C('GL_UNPACK_ALIGNMENT',0x0CF5)
GL_UNSIGNED_BYTE=_C('GL_UNSIGNED_BYTE',0x1401)
GL_UNSIGNED_SHORT=_C('GL_UNSIGNED_SHORT',0x1403)
GL_UNSIGNED_SHORT_4_4_4_4=_C('GL_UNSIGNED_SHORT_4_4_4_4',0x8033)
GL_UNSIGNED_SHORT_5_5_5_1=_C('GL_UNSIGNED_SHORT_5_5_5_1',0x8034)
GL_UNSIGNED_SHORT_5_6_5=_C('GL_UNSIGNED_SHORT_5_6_5',0x8363)
GL_VENDOR=_C('GL_VENDOR',0x1F00)
GL_VERSION=_C('GL_VERSION',0x1F02)
GL_VERSION_ES_CL_1_0=_C('GL_VERSION_ES_CL_1_0',1)
GL_VERSION_ES_CL_1_1=_C('GL_VERSION_ES_CL_1_1',1)
GL_VERSION_ES_CM_1_1=_C('GL_VERSION_ES_CM_1_1',1)
GL_VERTEX_ARRAY=_C('GL_VERTEX_ARRAY',0x8074)
GL_VERTEX_ARRAY_BUFFER_BINDING=_C('GL_VERTEX_ARRAY_BUFFER_BINDING',0x8896)
GL_VERTEX_ARRAY_POINTER=_C('GL_VERTEX_ARRAY_POINTER',0x808E)
GL_VERTEX_ARRAY_SIZE=_C('GL_VERTEX_ARRAY_SIZE',0x807A)
GL_VERTEX_ARRAY_STRIDE=_C('GL_VERTEX_ARRAY_STRIDE',0x807C)
GL_VERTEX_ARRAY_TYPE=_C('GL_VERTEX_ARRAY_TYPE',0x807B)
GL_VIEWPORT=_C('GL_VIEWPORT',0x0BA2)
GL_XOR=_C('GL_XOR',0x1506)
GL_ZERO=_C('GL_ZERO',0)
@_f
@_p.types(None,_cs.GLenum)
def glActiveTexture(texture):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glAlphaFunc(func,ref):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glAlphaFuncx(func,ref):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindBuffer(target,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTexture(target,texture):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glBlendFunc(sfactor,dfactor):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLenum)
def glBufferData(target,size,data,usage):pass
# Calculate length of data from size:BufferSize
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glBufferSubData(target,offset,size,data):pass
# Calculate length of data from size:BufferSize
@_f
@_p.types(None,_cs.GLbitfield)
def glClear(mask):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glClearColor(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glClearColorx(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfloat)
def glClearDepthf(d):pass
@_f
@_p.types(None,_cs.GLfixed)
def glClearDepthx(depth):pass
@_f
@_p.types(None,_cs.GLint)
def glClearStencil(s):pass
@_f
@_p.types(None,_cs.GLenum)
def glClientActiveTexture(texture):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glClipPlanef(p,eqn):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glClipPlanex(plane,equation):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glColor4f(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte,_cs.GLubyte)
def glColor4ub(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glColor4x(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMask(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glColorPointer(size,type,stride,pointer):pass
# Calculate length of pointer from type:ColorPointerType
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexImage2D(target,level,internalformat,width,height,border,imageSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexSubImage2D(target,level,xoffset,yoffset,width,height,format,imageSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLint)
def glCopyTexImage2D(target,level,internalformat,x,y,width,height,border):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTexSubImage2D(target,level,xoffset,yoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum)
def glCullFace(mode):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteBuffers(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteTextures(n,textures):pass
@_f
@_p.types(None,_cs.GLenum)
def glDepthFunc(func):pass
@_f
@_p.types(None,_cs.GLboolean)
def glDepthMask(flag):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glDepthRangef(n,f):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glDepthRangex(n,f):pass
@_f
@_p.types(None,_cs.GLenum)
def glDisable(cap):pass
@_f
@_p.types(None,_cs.GLenum)
def glDisableClientState(array):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei)
def glDrawArrays(mode,first,count):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawElements(mode,count,type,indices):pass
# Calculate length of indices from type:DrawElementsType
@_f
@_p.types(None,_cs.GLenum)
def glEnable(cap):pass
@_f
@_p.types(None,_cs.GLenum)
def glEnableClientState(array):pass
@_f
@_p.types(None,)
def glFinish():pass
@_f
@_p.types(None,)
def glFlush():pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glFogf(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glFogfv(pname,params):pass
# Calculate length of params from pname:FogParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glFogx(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glFogxv(pname,param):pass
@_f
@_p.types(None,_cs.GLenum)
def glFrontFace(mode):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glFrustumf(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glFrustumx(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenBuffers(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTextures(n,textures):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbooleanArray)
def glGetBooleanv(pname,data):pass
# Calculate length of data from pname:GetPName
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetBufferParameteriv(target,pname,params):pass
# Calculate length of params from pname:BufferPNameARB
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetClipPlanef(plane,equation):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetClipPlanex(plane,equation):pass
@_f
@_p.types(_cs.GLenum,)
def glGetError():pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetFixedv(pname,params):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetFloatv(pname,data):pass
# Calculate length of data from pname:GetPName
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glGetIntegerv(pname,data):pass
# Calculate length of data from pname:GetPName
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetLightfv(light,pname,params):pass
# Calculate length of params from pname:LightParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetLightxv(light,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetMaterialfv(face,pname,params):pass
# Calculate length of params from pname:MaterialParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetMaterialxv(face,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLvoidpArray)
def glGetPointerv(pname,params):pass
@_f
@_p.types(arrays.GLubyteArray,_cs.GLenum)
def glGetString(name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexEnvfv(target,pname,params):pass
# Calculate length of params from pname:TextureEnvParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexEnviv(target,pname,params):pass
# Calculate length of params from pname:TextureEnvParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetTexEnvxv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexParameterfv(target,pname,params):pass
# Calculate length of params from pname:GetTextureParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameteriv(target,pname,params):pass
# Calculate length of params from pname:GetTextureParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glGetTexParameterxv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glHint(target,mode):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsBuffer(buffer):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glIsEnabled(cap):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsTexture(texture):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glLightModelf(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glLightModelfv(pname,params):pass
# Calculate length of params from pname:LightModelParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glLightModelx(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glLightModelxv(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glLightf(light,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glLightfv(light,pname,params):pass
# Calculate length of params from pname:LightParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glLightx(light,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glLightxv(light,pname,params):pass
@_f
@_p.types(None,_cs.GLfloat)
def glLineWidth(width):pass
@_f
@_p.types(None,_cs.GLfixed)
def glLineWidthx(width):pass
@_f
@_p.types(None,)
def glLoadIdentity():pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glLoadMatrixf(m):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glLoadMatrixx(m):pass
@_f
@_p.types(None,_cs.GLenum)
def glLogicOp(opcode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glMaterialf(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glMaterialfv(face,pname,params):pass
# Calculate length of params from pname:MaterialParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glMaterialx(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glMaterialxv(face,pname,param):pass
@_f
@_p.types(None,_cs.GLenum)
def glMatrixMode(mode):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glMultMatrixf(m):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.GLfixed))
def glMultMatrixx(m):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glMultiTexCoord4f(target,s,t,r,q):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glMultiTexCoord4x(texture,s,t,r,q):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glNormal3f(nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glNormal3x(nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glNormalPointer(type,stride,pointer):pass
# Calculate length of pointer from type:NormalPointerType
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glOrthof(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glOrthox(l,r,b,t,n,f):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPixelStorei(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glPointParameterf(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glPointParameterfv(pname,params):pass
# Calculate length of params from pname:PointParameterNameARB
@_f
@_p.types(None,_cs.GLenum,_cs.GLfixed)
def glPointParameterx(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glPointParameterxv(pname,params):pass
@_f
@_p.types(None,_cs.GLfloat)
def glPointSize(size):pass
@_f
@_p.types(None,_cs.GLfixed)
def glPointSizex(size):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glPolygonOffset(factor,units):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed)
def glPolygonOffsetx(factor,units):pass
@_f
@_p.types(None,)
def glPopMatrix():pass
@_f
@_p.types(None,)
def glPushMatrix():pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glReadPixels(x,y,width,height,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glRotatef(angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glRotatex(angle,x,y,z):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLboolean)
def glSampleCoverage(value,invert):pass
@_f
@_p.types(None,_cs.GLclampx,_cs.GLboolean)
def glSampleCoveragex(value,invert):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glScalef(x,y,z):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glScalex(x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glScissor(x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum)
def glShadeModel(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glStencilFunc(func,ref,mask):pass
@_f
@_p.types(None,_cs.GLuint)
def glStencilMask(mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glStencilOp(fail,zfail,zpass):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glTexCoordPointer(size,type,stride,pointer):pass
# Calculate length of pointer from type:TexCoordPointerType
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTexEnvf(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTexEnvfv(target,pname,params):pass
# Calculate length of params from pname:TextureEnvParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTexEnvi(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexEnviv(target,pname,params):pass
# Calculate length of params from pname:TextureEnvParameter
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glTexEnvx(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glTexEnvxv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage2D(target,level,internalformat,width,height,border,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTexParameterf(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTexParameterfv(target,pname,params):pass
# Calculate length of params from pname:TextureParameterName
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTexParameteri(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameteriv(target,pname,params):pass
# Calculate length of params from pname:TextureParameterName
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfixed)
def glTexParameterx(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,ctypes.POINTER(_cs.GLfixed))
def glTexParameterxv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage2D(target,level,xoffset,yoffset,width,height,format,type,pixels):pass
# Calculate length of pixels from format:PixelFormat, type:PixelType
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glTranslatef(x,y,z):pass
@_f
@_p.types(None,_cs.GLfixed,_cs.GLfixed,_cs.GLfixed)
def glTranslatex(x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexPointer(size,type,stride,pointer):pass
# Calculate length of pointer from type:VertexPointerType
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glViewport(x,y,width,height):pass

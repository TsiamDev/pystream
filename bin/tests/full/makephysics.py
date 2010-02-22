#@PydevCodeAnalysisIgnore

module('tests.full.physics')
output('../temp')
config(checkTypes=True)


import tests.full.physics as physics
from shader import vec

#func(physics.simpleUpdate, inst(float), inst(int))

### Declare special paths for GLSL ###
# TODO move out of makefile?
from language.python.shaderprogram import VSContext, FSContext

glsl.output(attrslot(inst(VSContext), 'position'),   'gl_Position');
glsl.output(attrslot(inst(VSContext), 'point_size'), 'gl_PointSize');

# Fragment shader
for i in range(8):
	glsl.output(attrslot(inst(FSContext), 'colors').arrayslot(i), 'gl_FragData[%d]' % i);
glsl.output(attrslot(inst(FSContext), 'depth'), 'gl_FragDepth');

### Declare  the shader entry point ###

glsl.shader(physics.Shader, inst(vec.vec4), inst(vec.vec3), inst(vec.vec3), inst(vec.vec3), inst(vec.vec2))
glsl.shader(physics.SkyBox, inst(vec.vec4))
glsl.shader(physics.RadialBlur, inst(vec.vec4), inst(vec.vec2))
glsl.shader(physics.DirectionalBlur, inst(vec.vec4), inst(vec.vec2))

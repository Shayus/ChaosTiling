var VSHADER_SOURCE =
    'attribute vec4 a_Position;\n' +
//    'uniform mat4 u_ModelMatrix;\n' +
    'void main()\n' +
    '{\n' +
    '  gl_Position = a_Position;\n' +
//    '  gl_Position = u_ModelMatrix * a_Position;\n' +
    '}\n';
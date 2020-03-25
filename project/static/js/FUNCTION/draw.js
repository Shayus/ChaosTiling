function draw(FSHADER_SOURCE) {
    let vertice = new Float32Array([
        -1.0, -1.0,
        -1.0, 1.0,
        1.0, 1.0,
        1.0, 1.0,
        1.0, -1.0,
        -1.0, -1.0
    ]);
    //let modelMatrix = new Matrix4();
    //modelMatrix.scale(sf, sf, 1.0);
    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    
    // TODO： 查看之前是否创建过shader，如果有，删掉重建
    initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE);
    //let u_ModelMatrix = gl.getUniformLocation(gl.program, 'u_ModelMatrix');
    //gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);

    let vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertice, gl.STATIC_DRAW);
    let a_Position = gl.getAttribLocation(gl.program, 'a_Position');
    gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(a_Position);
    gl.drawArrays(gl.TRIANGLES, 0, 6);
}
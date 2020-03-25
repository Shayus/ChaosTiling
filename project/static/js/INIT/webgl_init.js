var canvas = document.getElementById('canvas');
var gl = getWebGLContext(canvas);
var sqrt3 = Math.sqrt(3);
var sf = '1.0';
function window_init() {
    var h = $(window).height() - $('#nav').height() * 1;
    var w = $(window).width() - $("#111").width() * 1.1;
    $("canvas").css({"width":w});
    $("canvas").css({"height":h});
    document.body.parentNode.style.overflowX = "hidden";
}
var cp_1,cp_2;
$('#cp1').on('changeColor', function(ev){
    cp_1 = ev.color.toRGB();
    //console.log(cp_1);
});
$('#cp2').on('changeColor', function(ev){
    cp_2 = ev.color.toRGB();
    //console.log(cp_2);
});

// 修改函数
$('#hd').on('change',function(){
    var post_data = {
        "id":$('#hd').val()
    };
    $.ajax({
        type: "POST",
        url: "gethd/",
        dataType: "json",
        data: post_data,
        success: function (data) {
            //console.log(data)
            $("#hd_view").attr("src",data);
        }
    });

})
$('#sl').on('change',function(){
    $('#showj').nextAll().remove();
    $('#showj').remove();
    var post_data = {
        "id": $('#sl').val()
    };
    $.ajax({
        type: "POST",
        url: "getsl/",
        dataType: "json",
        data: post_data,
        success: function (data) {
            $("#sl_view").attr("src",data.fshader_j_path);
            for(let i=data.fshader_j_;i>0;i--){
                //console.log(i);
                showj(i);
            }
        }
    });

})

function showj(n){
    let v = '参数'+n;
    let id = 'j_'+n;
    let source = 
        '<div id="showj" class="form-group"><label for="slRange">' +
        v +
        '</label><input type="range" class="form-control-range" id="'+
        id +
        '"></div>';
    $('#sl-form').after(source);
}

function start(){
    // 获取 铺砌方式、混沌函数、收敛检验和单位大小
    let c1 = $('#hd').val();
    let c2 = $('#sl').val();
    let c3 = $('#fs').val();
    if(c1 == 0)
        c1 = 1;
    if(c2 == 0)
        c2 = 1;
    if(c3 == 0)
        c3 = 1;
    if(typeof(cp_1)=='undefined')
        cp_1 = {r:0.0,g:0.0,b:0.0,a:1.0};
    if(typeof(cp_2)=='undefined')
        cp_2 = {r:0.0,g:0.0,b:0.0,a:1.0};
    r1 = cp_1.r/255; r2 = cp_2.r/255;
    g1 = cp_1.g/255; g2 = cp_2.g/255;
    b1 = cp_1.b/255; b2 = cp_2.b/255;
    a1 = cp_1.a/255; a2 = cp_2.a/255;
    if(r1%1==0)
        r1 += '.0';
    if(r2%1==0)
        r2 += '.0';
    if(g1%1==0)
        g1 += '.0';
    if(g2%1==0)
        g2 += '.0';
    if(b1%1==0)
        b1 += '.0';
    if(b2%1==0)
        b2 += '.0';
    if(a1%1==0)
        r1 += '.0';
    if(a2%1==0)
        r1 += '.0';
    let color1 = 'vec4 color1 = vec4(' + r1 + ',' + g1 + ',' + b1 + ',' + a1 + ');'
    let color2 = 'vec4 color2 = vec4(' + r2 + ',' + g2 + ',' + b2 + ',' + a2 + ');'
    var post_data = {
        "c1":c1,
        "c2":c2,
        "c3":c3,
    };
    //console.log(post_data)
    $.ajax({
        type: "POST",
        url: "getShader/",
        dataType: "json",
        data: post_data,
        success: function (data) {
            // 获取收敛函数的参数
            let init = '';
            for(let i=1;i<data.fshader_j_+1;i++){  
                let val = $('#j_'+i).val() / 100;
                if(val%1==0)
                    val += '.0';
                init +=  data.fshader_bc_j_+i+'='+val+';';
            }
            //console.log(init)
            // 获取大小参数
            let dx = $('#dx').val();
            if(dx==''){
                dx=1;
            }
            if(dx%1 == 0){
                dx += '.0'
            }
            // 初始化FSHADER_SOURCE
            let FSHADER_SOURCE = 
            data.fshader_head + 
            init +
            data.fshader_sf + dx + ';' +
            data.fshader_fun + 
            data.fshader_g + 
            data.fshader_j + 
            data.fshader_fun_end + 

            data.fshader_color_set + data.fshader_g_n_ + '.0;' + 
            color1 + 
            color2 +
            data.fshader_color + 
            data.fshader_unit +
            data.fshader_main;

            //console.log(FSHADER_SOURCE);
            draw(FSHADER_SOURCE);

            // ajax返回FSHADER_SOURCE，完成组装
            //draw();
        }
    });
}
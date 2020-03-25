from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import *
import json
# Create your views here.
def home(request):
    return render(request, 'project/dashboard.html')

def init(request):
    function = AppShaderG.objects.all().values('id','discribe')
    judge    = AppShaderJ.objects.all().values('id','discribe')
    shape    = AppShaderMain.objects.all().values('id','discribe')
    data = {
        'function':list(function),
        'judge'   :list(judge),
        'shape'   :list(shape)
    }
    return JsonResponse(data,safe=False)

def gethd(request):
    data = request.POST.get("id")
    return JsonResponse(AppShaderG.objects.get(id=data).path, safe=False)

    
def getsl(request):
    c2 = request.POST.get("id")
    data = {
        # 获得j函数需要几个参数
        'fshader_j_' :      AppShaderJ.objects.get(id=c2).extra,
        # 获得j函数图片地址
        'fshader_j_path':   AppShaderJ.objects.get(id=c2).path,
    }
    print(data)
    return JsonResponse(data, safe=False)


def getdd(request):
    data = request.POST.get("id")
    print(data)
    if(data=="1"):
        rd = "/static/images/dd1.png"
        return JsonResponse(rd, safe=False)
    elif (data=="2"):
        rd = "/static/images/dd2.png"
        return JsonResponse(rd, safe=False)
    elif (data=="3"):
        rd = "/static/images/dd3.png"
        return JsonResponse(rd, safe=False)
    else:
        rd = 'error'
        return JsonResponse(rd,safe=False)


def getShader(request):
    
    c1 = request.POST.get("c1")     #hd
    c2 = request.POST.get("c2")     #sl
    c3 = request.POST.get("c3")     #fx

    data = {
        
        # 获得G函数循环次数
        'fshader_g_':       AppShaderG.objects.get(id=c1).num,
        # 获得FSHADER_SOURCE
        'fshader_sf':       AppShaderBc.objects.get(name='FSHADER_sf').content,
        'fshader_head' :    AppShaderBc.objects.get(name='FSHADER_HEAD').content,
        'fshader_fun':      AppShaderBc.objects.get(name='FSHADER_FUN_f').content,
        'fshader_fun_end':  AppShaderBc.objects.get(name='FSHADER_FUN_end').content,
        'fshader_color':    AppShaderBc.objects.get(name='FSHADER_COLOR').content,
        'fshader_color_set':AppShaderBc.objects.get(name='FSHADER_COLOR_SET').content,
        'fshader_bc_j_':    AppShaderBc.objects.get(name='FSHADER_j_').content,

        'fshader_g':        AppShaderG.objects.get(id=c1).fshader_g,
        'fshader_g_n_':      AppShaderG.objects.get(id=c1).num,

        'fshader_j':        AppShaderJ.objects.get(id=c2).fshader_j,
        'fshader_j_':       AppShaderJ.objects.get(id=c2).extra,

        'fshader_unit':     AppShaderMain.objects.get(id=c3).fshader_unit,
        'fshader_main':     AppShaderMain.objects.get(id=c3).fshader_main,
    }

    return JsonResponse(data,safe=False)
# coding:utf-8
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template

from models import User
# Create your views here.
from .form import *


# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密__码', widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            # User.objects.get_or_create(username = username,password = password)
            registAdd = User.objects.get_or_create(username=username, password=password)[1]
            if registAdd == False:
                # return HttpResponseRedirect('/share/')
                return render_to_response('share.html', {'registAdd': registAdd, 'username': username})
            else:
                return render_to_response('share.html', {'registAdd': registAdd})

    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 对比提交的数据与数据库中的数据
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/index/')
                # 将username写入浏览器cookie，失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))


# 登录成功
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})


# 退出登录

def logout(req):
    response = HttpResponse('logout!!!')
    # 清除cookie里保存的username
    response.delete_cookie('username')
    return response


def share(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            return render_to_response('share.html', {'username': username})
    else:
        uf = UserForm()
    return render_to_response('share.html', {'uf': uf})


# 添加学生记录
def addstudent(request):
    username = request.COOKIES.get('username', '')
    form = StuForm()
    if request.method == "POST":
        form = StuForm(request.POST or None)
        if form.is_valid():
            form.save()
    t = get_template('addstudent.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c),{'username': username})


def viewstudent(req):
    stuid = req.GET.get("stuid")
    delstuid = req.GET.get("del")
    editstuid = req.GET.get("edit")
    username = req.COOKIES.get('username', '')
    if delstuid:  # 如果有delstuid 视作删除,这是 ajax传过来的请求做的处理
        stulist = student.objects.filter(stuid=delstuid).delete()

    elif stuid:  # 如果有stuid 视做查询,
        stulist = student.objects.filter(stuid=stuid).order_by('stuid')
    elif editstuid:

        stulist = student.objects.filter(stuid=editstuid).delete()
    else:
        stulist = student.objects.all().order_by('stuid')

    return render_to_response("viewstudent.html",
                              context_instance=RequestContext(req, {"stulist": stulist ,'username': username}
                                                            ))


def editstudent(request):
    form = StuForm
    c = RequestContext(request, locals())
    if request.method == 'POST':
        form = StuForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'viewstudent.html')

    t = get_template('editstudent.html')
    return HttpResponse(t.render(c))


def addgrade(request):
    username = request.COOKIES.get('username', '')
    form = GradeForm()
    if request.method == "POST":
        form = GradeForm(request.POST or None)
        if form.is_valid():
            form.save()
    t = get_template('addgrade.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def searchgrade(req):
    stuid = req.GET.get("stuid")
    username = req.COOKIES.get('username', '')

    gradelist = grade.objects.filter(stuid=stuid).order_by('stuid')
    return render_to_response("searchgrade.html",
                              context_instance=RequestContext(req, {"gradelist": gradelist, 'username': username}
                                                              ))

def editgrade(req):
    stuid = req.GET.get("stuid")
    delstuid = req.GET.get("del")
    alterstuid = req.GET.get("alter")

    if delstuid:  # 如果有delstuid 视作删除,这是 ajax传过来的请求做的处理
        gradelist = grade.objects.filter(stuid=delstuid).delete()

    elif stuid:  # 如果有stuid 视做查询,
        gradelist = grade.objects.filter(stuid=stuid).order_by('stuid')
    elif alterstuid:

        gradelist = grade.objects.filter(stuid=alterstuid).delete()
    else:
        gradelist = grade.objects.all().order_by('stuid')

    return render_to_response("editgrade.html",
                              context_instance=RequestContext(req, {"gradelist": gradelist}
                                                              ))


def altergrade(request):
    form = GradeForm
    c = RequestContext(request, locals())
    username = req.COOKIES.get('username', '')

    if request.method == 'POST':
        form = GradeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'base.html')

    t = get_template('altergrade.html')
    return HttpResponse(t.render(c))


def viewclass(req):
    acaname = req.GET.get("acaname")
    username = req.COOKIES.get('username', '')

    stulist = student.objects.filter(acaname=acaname)

    return render_to_response("viewclass.html",
                              context_instance=RequestContext(req, {"stulist": stulist, 'username': username}
                                                              ))


def viewclassstu(req):
    acaname = req.GET.get("acaname")
    classnum = req.GET.get("classnum")
    username = req.COOKIES.get('username', '')

    stulist = student.objects.filter(classnum=classnum, acaname=acaname)
    return render_to_response("viewclassstu.html",
                              context_instance=RequestContext(req, {"stulist": stulist, 'username': username}
                                                              ))


def changepsw(req):
    username = req.COOKIES.get('username', '')

    return render_to_response("changepsw.html", {'username': username})

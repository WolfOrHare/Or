#-*-coding:utf-8-*-
from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,Http404
from django import forms
from webapp.models import User,Article

class UserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    # if request.method == 'POST':
    #     userf = UserForm(request.POST)
    #     if userf.is_valid():
    #         username = userf.cleaned_data['username']
    #         password = userf.cleaned_data['password']
    #
    #         User.objects.create(username = username,password = password)
    #         return HttpResponse('／login／')
    # else:
    #     userf = UserForm()
    #
    # return render_to_response('regist.html',{'userf':userf})
# def login(request):
#     request.is_ajax()
#     if request.method == 'POST':
#         userf = UserForm(request.POST)
#
#         if userf.is_valid():
#             username = userf.cleaned_data['username']
#             password = userf.cleaned_data['password']
#
#             users = User.objects.filter(username__exact=username, password__exact=password)
#             if users:
#                 request.session['username'] = username
#                 response =  HttpResponseRedirect('/index/')
#                 return response
#             else:
#                 return HttpResponseRedirect('/login/')
#     else:
#         userf = UserForm()
#     return render_to_response('login.html', {'userf': userf})
def login(request):
     return render(request,'login.html')
     #return render(request, 'login_test.html')

def login_check(request):
    #http://blog.csdn.net/brynao/article/details/76268725
    #后续要完善把，改成只能用email作为用户名的形式，已经备份到有道
    input_email = request.POST.get('email')
    input_pwd = request.POST.get('password')
    #查询用户密码是否有效
    users = User.objects.filter(username__exact=input_email, password__exact=input_pwd)
    print(users)
    if users:
        request.session['email'] = input_email
        request.session['input_pwd'] = input_pwd
        return JsonResponse({'msg': 'ok'})
    else:
        return JsonResponse({'msg': 'fail_user'})

def register(request):
    #获取前台传入的用户名，密码
    input_email = request.POST.get('reg_email')
    input_pwd = request.POST.get('reg_password')
    exa_input_pwd = request.POST.get('exa_password')
    # print(input_email+'--->'+input_pwd+'--->'+exa_input_pwd)
    #查询数据库中数据是否存在
    users = User.objects.filter(username__exact=input_email)
    print(users.all())

    try:
        if users or users is None:
            print('用户名错误！'+users)
            return JsonResponse({'msg': 'exa_fail_user'})

        #否则确认用户或密码是否有效，无效返回
        elif (input_pwd is None) or (exa_input_pwd is None):
            return JsonResponse({'msg': 'exa_password'})


        elif (input_pwd is None) or (input_pwd != exa_input_pwd):
            return JsonResponse({'msg': 'exa_fail_reg'})

        #有效添加数据库记录并跳转到主页，并记录session
        else:
            User.objects.create(username =input_email, password=input_pwd)
            request.session['email'] = input_email
            request.session['input_pwd'] = input_pwd

            return JsonResponse({'msg': 'reg_ok'})

    except TypeError:
        #这是可以在div里实现的
        print('类型错误')
        return JsonResponse({'msg': 'exa_password'})

def index(request):
    username = request.session.get('email', 'password')
    return render_to_response('index.html', {'username': username})

def logout(request):

    try:
        del request.session['email']
    except KeyError:
        pass
    return HttpResponseRedirect('/index/')

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})
def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

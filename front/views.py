from django.http import HttpResponse
#重定向
from django.shortcuts import redirect,reverse
#如果很多个网页都有首页，登录页面，当出现同一个名字的时候，django混
#所以要定义应用命名空间
def index(request):
    #若没有传用户名，则跳转到登录页面
    username=request.GET.get("username")
    if username:
        return HttpResponse("前台首页")
    else:
        #通过name那个参数进行反转
        return redirect(reverse("front:login"))
def login(request):
    return HttpResponse("前台登录页面")

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("cms首页")
def login(request):
    return HttpResponse("cms登录页面")
# Create your views here.

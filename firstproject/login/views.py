from django.shortcuts import render
from .models import Login

# Create your views here.
def login(request) : 
    return render(request,"login/test3.html")

def check(request) :
    user_id = request.GET.get('uid')
    user_pwd = request.GET.get('pwd')
    print(user_id)
    print(user_pwd)
    user_infos = Login.objects.all()
    # userid = Login.objects.get(id=user_id)

    for user_info in user_infos:
        if (user_info.id == user_id and user_info.password == user_pwd):
            text = "로그인 성공"
            break
        else: 
            text = "로그인 실패.."

    context = {'text' : text}

    return render(request, "login/check.html", context)

def main(request) :
    return render(request, "login/test.html")
from django.shortcuts import render, redirect
from message.models import Content, Message


def index(request):
    return render(request, 'index.html')


def show_content(request):
    db = Content.objects.all()
    return render(request, "content.html", {"data": db})


def show_message(request):
    # 判断是否为GET
    if request.method == "GET":
        # 获取数据库数据
        db = Message.objects.all()
        return render(request, 'message/show_message.html', {"date": db})
    # 判断是否为POST
    elif request.method == "POST":
        # 接受参数
        name = request.POST.get("name")
        content = request.POST.get("content")
        # 判断参数是否为空
        if name != "" and content != "":
            # 链接数据库
            db = Message()
            db.name = name
            db.content = content
            db.save()
            return redirect("/message/")

        else:
            db = Message.objects.all()
            return render(request, "message/show_message.html", {"error": "留言人或留言信息不能为空哦", "date": db})

    else:
        return redirect("/")

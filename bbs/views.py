from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from bbs.form import PostForm
from bbs.models import Board, Users


# Create your views here.

def index(request):

    # num1 = request.GET.get("var1")
    # num2 = request.GET.get("var2")
    return render(request, "bbs/index.html")


def list(request):
    posts = Board.objects.all().order_by('-post_number')
    context = {'posts': posts}
    return render(request, 'bbs/list.html', context)


def write(request):
    form = PostForm(request.POST or None)

    if request.method == "POST":
        # print("write POST")
        
        if form.is_valid():
            # print("VALID")
            post = form.save(commit=False)
            post.save()
        return redirect("/bbs/list/")

    # request.method=="GET":
    context = {'postForm': form}
    return render(request, "bbs/write.html", context)

def read(request, post_num):
    post = Board.objects.get(post_number=post_num)
    context = {'post':post}
    return render(request, "bbs/read.html", context)

def delete(request, post_num):
    post = Board.objects.get(post_number=post_num)
    post.delete()
    return redirect("/bbs/list/")

def update(request, post_num):
    post = Board.objects.get(post_number=post_num)

    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect("/bbs/list/")
        
    # request.method=="GET":
    form =PostForm(instance=post)
    context = {'postForm': form}
    return render(request, "bbs/write.html", context)

# 테스트
# def postdata(request):
#     num1 = request.POST.get("var1")
#     num2 = request.POST.get("var2")
#     context = {"key1": int(num1) + int(num2)}

#     return render(request, "bbs/sendpost.html", context)

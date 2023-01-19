from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from bbs.write import PostForm
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
            # print("Something wrong")
            post = form.save(commit=False)
            post.save()
        return redirect("/bbs/write")

    # print("write GET")
    context = {'postForm': form}
    return render(request, "bbs/write.html", context)

# 테스트
# def postdata(request):
#     num1 = request.POST.get("var1")
#     num2 = request.POST.get("var2")
#     context = {"key1": int(num1) + int(num2)}

#     return render(request, "bbs/sendpost.html", context)

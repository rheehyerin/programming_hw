from django.shortcuts import render, redirect
from blog.forms import CommentModelForm


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def comment_new(request):
    #유저가 정보를 입력하는 부분과 정보를 입력한 뒤에 보여지는 부분을 구분하는 method

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CommentModelForm()

        return render(request, 'blog/comment_form.html',{'form':form,})
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm, CommentForm

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'posting_hw/post_list.html',{'post_list':post_list})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comment_set.all()
    comment_form = CommentModelForm()
    comment_form_ver_2 = CommentForm()
    return render(request, 'posting_hw/post_detail.html',{
        'post': post,
        'comment_form': comment_form,
        'comments':comments,
        'comment_form_ver_2': comment_form_ver_2,
    })


def comment_new(request, post_pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False) #db 에는 아직 저장하진 마라.
            comment.post = post
            comment.save()
            return redirect('posting:post_detail', post.pk)
    else:
        form = CommentModelForm()

    return render(request, 'posting_hw/comment_form.html', {
        'form': form,
    })


def post_write(request):

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return post_list(request)
        else:
            return redirect('posting:post_write')
    else:
        form = PostModelForm()

        return render(request, 'posting_hw/post_write.html',{'post_form':form})

def comment_new_ver_2(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form_2 = CommentForm(request.POST, request.FILES)
        if form_2.is_valid():
            ment = form_2.save(commit=False)
            ment.post = post
            ment.save()
            return redirect('posting:post_detail', post.pk)
    else:
        form_2 = CommentForm()

    return render(request, 'posting_hw/comment_form.html',{'form_2':form_2,})

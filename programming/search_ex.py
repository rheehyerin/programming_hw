from blog.models import Post
Post.objects.filter(title_contains="hello")
Post.objects.filter(title_icontains='hello')

q = request.GET.get('q', None)
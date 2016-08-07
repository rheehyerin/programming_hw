from django.contrib import admin
from blog.models import Post, Comment, Tag, Contact, ZipCode, ZipCode_ver_2, ZipCode2


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

admin.site.register(Tag)

admin.site.register(Contact)

admin.site.register(ZipCode)

admin.site.register(ZipCode_ver_2)

class ZipCode2Admin(admin.ModelAdmin):
    list_display = ['code', 'city', 'gu', 'dong', 'road']

admin.site.register(ZipCode2, ZipCode2Admin)
from django.contrib import admin
from .models import Post, PostImage, Comments


class ImageAdmin(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 4

class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdmin,)
    list_display = ('title', 'owner', 'post_count')
    def post_count(self,obj):
        return obj.likes.filter(is_like=True).count()
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Comments)
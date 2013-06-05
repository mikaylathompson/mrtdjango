from django.contrib import admin
from blog.models import Post, Comment, Tag

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1

class PostAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'title', 'author', 'text', 'edit_date']
	inlines = [CommentInline]




admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
admin.site.register(Tag)
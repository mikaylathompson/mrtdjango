# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment, Tag
from django.utils import timezone


def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:9]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if (request.POST):
		post.comment_set.create(commentor=request.POST['name'], com_text=request.POST['comtext'], com_date=timezone.now())
	comment_list = post.comment_set.order_by('com_date')
	return render(request, 'blog/detail.html', {'post': post, 'comment_list': comment_list})

def write(request):
	if (request.POST):
		t_title = request.POST['title']
		t_pub_date = timezone.now()
		t_edit_date = timezone.now()
		t_author = request.POST['author']
		t_text = request.POST['text']
		post = Post(title=t_title, pub_date=t_pub_date, edit_date=t_edit_date, author=t_author, text=t_text)
		post.save()
		return render(request, 'blog/write.html', {'post': post})
	else:
		return render(request, 'blog/write.html')


	
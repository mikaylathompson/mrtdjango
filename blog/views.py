# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment, Tag


def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'blog/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	comment_list = post.comment_set.order_by('-com_date')
	# comment_list = []
	# for c in post.comment_set.all():
	# 	comment_list.append(c)


	# comment_list = get_object_or_404(Post.objects.filter(id=post_id)[0].comment_set.all(), pk=post_id)
	# comment_text = [].append([c.com_text for c in Post.objects.filter(id=post_id)[0].comment_set.all()])
	# comment_auth = [].append([c.commentor for c in Post.objects.filter(id=post_id)[0].comment_set.all()])
	# comment_date = [].append([c.com_date for c in Post.objects.filter(id=post_id)[0].comment_set.all()])
	# render_hash = {'post': post, 'com_text': comment_text, 'commentor': comment_auth, 'com_date': comment_date}

	return render(request, 'blog/detail.html', {'post': post, 'comment_list': comment_list})


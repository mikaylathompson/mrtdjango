# Create your views here.
from django.http import HttpResponse
from blog.models import Post, Comment, Tag


def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	output = '<br> '.join([p.title for p in latest_post_list])
	return HttpResponse(output)

def detail(request, post_id):
	return HttpResponse("You're looking at a specific post. <br><br> This is where you add a comment.")

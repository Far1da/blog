

# Create your views here.
from pyexpat import generic

from posts.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name ="posts/post_list.html"







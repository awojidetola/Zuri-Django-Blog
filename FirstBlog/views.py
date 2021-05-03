from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post,Category, Comment
from .forms import PostForm,EditForm, CommentForm
from django.urls import reverse_lazy


#def home(request):
#	return render (request, 'home.html', {})


def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats)
	return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})

class HomeView(ListView):
	model= Post
	template_name = 'home.html'
	ordering =['-post_date']
	#ordering = ['-id']


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__' #Display all
	#fields = ('title','title_tag','body') #Displays just specifics

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__' #Display all
	#fields = ('title','title_tag','body') #Displays just specifics
	def form_valid (self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)
	success_url =reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__' #Display all

	#fields = ('title','title_tag','body') #Displays just specifics
	
class UpdatePostView(UpdateView):
	model=Post
	form_class= EditForm
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url =reverse_lazy('home')

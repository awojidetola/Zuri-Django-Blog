from django import forms
from . models import Post
from .models import Category
from .models import Comment

choices=Category.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
	choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author','category', 'body')

		widgets = {
			'title': forms.TextInput (attrs= {'class': 'form-control', 'placeholder':'Enter the Title Here!'}),
			'title_tag': forms.TextInput (attrs= {'class': 'form-control'}),
			'author': forms.TextInput (attrs= {'class': 'form-control', 'value':" ",'id':'elder','type':'hidden'}),

			#'author': forms.Select (attrs= {'class': 'form-control'}),
			'category': forms.Select (choices=choice_list, attrs= {'class': 'form-control'}),
			'body': forms.Textarea (attrs= {'class': 'form-control', 'placeholder': "Enter some text here"}),


		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body')

		widgets = {
			'title': forms.TextInput (attrs= {'class': 'form-control', 'placeholder':'Enter the Title Here!'}),
			'title_tag': forms.TextInput (attrs= {'class': 'form-control'}),
			#'author': forms.Select (attrs= {'class': 'form-control'}),
			'body': forms.Textarea (attrs= {'class': 'form-control', 'placeholder': "Enter some text here"}),


			}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput (attrs= {'class': 'form-control', 'placeholder':'Enter your Name Here!'}),
			'body': forms.Textarea (attrs= {'class': 'form-control', 'placeholder': "Enter your comment"}),


			}
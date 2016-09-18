from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """docstring for PostForm"""
    # def __init__(self, arg):
    #     super(PostForm, self).__init__()
    #     self.arg = arg
    #     
    class Meta:
        model = Post
        fields = ('title', 'content')
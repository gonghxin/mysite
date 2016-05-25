from django import forms
from .models import Post
from django.contrib import admin
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
		#js=('tiny_mce/tiny_mce.js','textareas.js')  
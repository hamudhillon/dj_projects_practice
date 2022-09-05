from dataclasses import field
from django import forms
from .models import blogPost
class Myform(forms.Form):
    title=forms.CharField(widget=forms.TextInput(
         attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
    ))
    post_by=forms.CharField(widget=forms.TextInput(
         attrs={
                "placeholder": "Post By",
                "class": "form-control"
            }
    ))
    desc=forms.CharField(widget=forms.Textarea(
         attrs={
                "placeholder": "Description",
                "class": "form-control"
            }
    ))
    # image=forms.ImageField()
    class Meta:
        model=blogPost
        fields=('title','post_by','desc',
        # 'image'
        )

       
     

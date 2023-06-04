from django import forms 
from .models import Post


class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('개발', '개발'),
        ('CS', 'CS'),
        ('신기술', '신기술'),
    ]

    category = forms.ChoiceField(
        label='분류',
        label_suffix='',
        choices=CATEGORY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                'style': 'width: 100px;'
            }
        ),
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'category',)
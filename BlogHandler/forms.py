from django import forms
from .models import Article, Author


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['author'] = forms.CharField(max_length=100, required=True)
    class Meta:
        model = Article
        fields = ('title', 'content', )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title'}),
            'content': forms.Textarea(attrs={
                'class': 'text_input',
                'name': 'article_content'}),
        }

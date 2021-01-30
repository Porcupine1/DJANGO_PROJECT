from django import forms
from .models import Article, Author
from tinymce.widgets import TinyMCE
from django.utils.translation import gettext_lazy as _



class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['author'] = forms.CharField(max_length=100, required=True)
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'article_title'}),
            'content': TinyMCE(mce_attrs={
                'class': 'article_content'}),
        }
        labels = {
            'content': _('Write article here'),
        }

    def clean(self):
        rt = super().clean()
        self.cleaned_data['title'] = self.cleaned_data.get('title').title()
        return rt
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'icerik', 'draft', 'ders']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.isdigit():
            raise forms.ValidationError('lutfen sadece sayı ')
        if '@' in title:
            raise forms.ValidationError('@ kullanmayınz')
        return title


class OdemeForm(forms.Form):
    odeme=forms.IntegerField(label='Ödenecek Tutar')





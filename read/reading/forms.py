from django import forms
from .models import Read


class ReadingForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ('title', 'url', 'data')


        # your_name = forms.CharField(label='Your name', max_length=100)
        # title = forms.CharField(label='Title',max_length=200)
        # url = forms.URLField(label='Url')
        # data = forms.CharField(label='Content', max_length=4000, widget=forms.Textarea)
        # created_date = forms.DateField()
        # country = models.CharField(max_length=50)
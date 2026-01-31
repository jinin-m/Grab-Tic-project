from django import forms

from .models import Movies

class MovieForm(forms.ModelForm):

    class Meta:

        model = Movies

        # fields = ['name','description','runtime','photo','release_date','certification','cast','languages','genre']

        exclude = ['uuid','active_status']

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Movie Name'}),

            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Movie Description','rows':4}),

            'photo':forms.FileInput(attrs={'class':'form-control'}),

            'runtime':forms.TimeInput(attrs={'class':'form-control','type':'time'}),

            'release_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'certification':forms.Select(attrs={'class':'form-select'}),

            'languages':forms.SelectMultiple(attrs={'class':'form-select'}),

            'cast':forms.SelectMultiple(attrs={'class':'form-select'}),

            'genre':forms.SelectMultiple(attrs={'class':'form-select'}),
        }
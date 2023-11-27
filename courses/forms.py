from typing import List
from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
        ]
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'matthewpogi':
            raise forms.ValidationError(f"This is not a valid title, this title {title} is my name")
        return title
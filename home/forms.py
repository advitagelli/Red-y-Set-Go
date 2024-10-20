from django import forms
from django import forms
from .models import UserCycleData

class UserCycleDataForm(forms.ModelForm):
    class Meta:
        model = UserCycleData
        fields = ['cramp_level', 'cycle_start_date', 'cycle_end_date', 'height', 'weight', 'age']
        
        widgets = {
            'cramp_level': forms.Select(attrs={'class': 'form-select'}),
            'cycle_start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cycle_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter height in cm'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter weight in pounds'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = field.replace('_', ' ').capitalize()
            self.fields[field].widget.attrs['class'] = 'form-control' if 'form-control' not in self.fields[field].widget.attrs else self.fields[field].widget.attrs['class']
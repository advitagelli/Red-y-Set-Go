from django import forms
from django import forms
from .models import UserCycleData

class UserCycleDataForm(forms.ModelForm):
    class Meta:
        model = UserCycleData
        fields = [
            'current_date',
            'cramp_level',
            'height',
            'weight',
            'age',
            'previous_cycle_start',
            'previous_cycle_end'
        ]
        widgets = {
            'current_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cramp_level': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'previous_cycle_start': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'previous_cycle_end': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = field.replace('_', ' ').capitalize()
            self.fields[field].widget.attrs['class'] = 'form-control' if 'form-control' not in self.fields[field].widget.attrs else self.fields[field].widget.attrs['class']
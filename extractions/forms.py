from django import forms
from .models import Prescription
from .models import CaseStudy

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'input-field'}),
            'doctor_name': forms.TextInput(attrs={'class': 'input-field'}),
            'patient_name': forms.TextInput(attrs={'class': 'input-field'}),
            'age': forms.NumberInput(attrs={'class': 'input-field'}),
            'diagnosis': forms.Textarea(attrs={'class': 'input-field', 'rows': 2}),
            'medicine_name': forms.TextInput(attrs={'class': 'input-field'}),
            'dosage': forms.TextInput(attrs={'class': 'input-field'}),
            'frequency': forms.TextInput(attrs={'class': 'input-field'}),
            'duration': forms.TextInput(attrs={'class': 'input-field'}),
            'remarks': forms.Textarea(attrs={'class': 'input-field', 'rows': 2}),
        }



class CaseStudyForm(forms.ModelForm):
    class Meta:
        model = CaseStudy
        fields = ['patient_name', 'diagnosis', 'treatment', 'outcome']

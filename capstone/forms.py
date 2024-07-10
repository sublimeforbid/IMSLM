from django.forms import ModelForm, DateTimeInput
from django import forms
from .models import BarangayUser

class AdminForm(ModelForm):
    password=forms.Charfield(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = BarangayUser
        fields = '__all__'
        widgets = {
            'office_hours_weekdays': DateTimeInput(attrs={'type': 'datetime-local'}),
            'office_hours_weekends': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def clean(self):
        cleaned_data = super(AdminForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match"
            )
        
        return cleaned_data
from django import forms
from .models import Student

class SignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','college_name','branch','email','gender','highestdegree','phone_no','SFID','degree','stream','resume']


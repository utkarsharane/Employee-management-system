# employee_management/forms.py
from django import forms
from .models import EmployeeSalary

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        model = EmployeeSalary
        fields = ['salary', 'date_range']

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'mobile_number', 'employee_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'employee_code': 'Employee Code',
            'mobile_number': 'Mobile Number'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['employee_code'].required = False

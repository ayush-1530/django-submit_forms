from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class StudentForm(forms.Form):
        name = forms.CharField(max_length=100)
        enrollment_number = forms.IntegerField()
        department = forms.CharField(max_length=20)
        date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type" : "date"}))


      
        

        def __init__(self, *args, **kwargs):
             super(StudentForm, self).__init__(*args, **kwargs)
             self.helper = FormHelper()
             self.helper.form_method = 'post'
             self.helper.add_input(Submit('submit', 'Submit'))



class EmployeeForm(forms.Form):
       name = forms.CharField(max_length= 20)
       employee_id = forms.IntegerField()
       department = forms.CharField(max_length=8)
       date_of_joining = forms.DateField(widget=forms.DateInput(attrs={"type" : "date"}))


       def __init__(self, *args, **kwargs):
              super(EmployeeForm, self).__init__(*args, **kwargs)
              self.helper = FormHelper()
              self.helper.form_method = 'post'
              self.helper.add_input(Submit('submit', 'Submit'))





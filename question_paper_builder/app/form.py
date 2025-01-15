import datetime
from django import forms
from django.core.validators import MinValueValidator

class question_paper_form(forms.Form):
    college = [
        ('kk wagh','kk wagh'),
        ('Met','Met'),
        ('SNJB','SNJB'),
        ('NDNVP','NDNVP'),

    ]

    dept = [
        ('Computer Engineering', 'Computer Engineering'), 
        ('AIML', 'AIML'), 
        ('IT','IT'),
        ('ENTC','ENTC'),

    ]

    sem = [
        ('SEM I', 'SEM I'), 
        ('SEM II', 'SEM II'),  
        ('SEM III', 'SEM III'), 
        ('SEM IV', 'SEM IV'), 
        ('SEM V', 'SEM V'), 

    ]
    
    year = [
        ('First Year', 'First Year'), 
        ('Second Year', 'Second Year'),  
        ('ThirdYear', 'Third Year'), 
    ]


    college_name = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=college)
    branch_name = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=dept)
    year = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=year)
    semester = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}), choices=sem)
    faculty = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Enter Faculty Name'}), required=True)
    subject_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Enter Subject Name'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': "form-control", 'type' : 'date'}),validators=[MinValueValidator(limit_value=datetime.date.today(), message="Invalid date. Please select a date starting from today.")])
    qb = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control", 'type' : 'file', 'placeholder' : 'Question Bank'}), required=True)
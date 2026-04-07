from django import forms
from myapp.models import Jobpost,LOCATION_TYPE,EXPERIENCE,JOB_TYPE,EMPLOYMENT_TYPE

class JobPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the job title",
                "class": "form-control",
            }
        ))
    description = forms.CharField(widget= forms.TextInput(attrs={
        "placeholder":"Enter the job description",
        "class": "form-control",
    }))

    salary = forms.DecimalField(widget= forms.NumberInput(attrs={
        "placeholder":"Enter the salary",
        "class": "form-control",
    }))
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'E.g. Remote, Default City'})
    )
    location_type = forms.ChoiceField(choices=LOCATION_TYPE, widget=forms.Select(
        attrs={
        "class":"form-control",
        }))
    experience_required = forms.ChoiceField(choices=EXPERIENCE, widget=forms.Select(
        attrs={
        "class":"form-control",
        }))
    job_type = forms.ChoiceField(choices=JOB_TYPE, widget=forms.Select(
        attrs={
        "class":"form-control",
        }))
    
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE, widget=forms.Select(
        attrs={
        "class":"form-control",
        }))
    
    skills_required = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'E.g. Django, CSS'})
    )
    
    class Meta:
        model = Jobpost
        fields = ["title","description","salary",
                  "job_type","employment_type",
                  "experience_required","location","location_type","skills_required"]

class JobFilterForm(forms.Form):
    job_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Job Title...'})
    )
    location_type = forms.ChoiceField(
        required=False,
        choices=LOCATION_TYPE,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'City/Location...'})
    )
    job_type = forms.ChoiceField(
        required=False,
        choices=JOB_TYPE, 
        widget=forms.Select(attrs={
        "class":"form-control",
        })
    )

    organization_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter organization name',
            'class': 'form-control'
        })
    )
    
    salary = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter salary range',
            'class': 'form-control'
        })
    )
    
    skills_required = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by skills'})
    )

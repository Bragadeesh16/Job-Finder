from django import forms
from myapp.models import Jobpost,LOCATION_TYPE,EXPERIENCE,JOB_TYPE,EMPLOYMENT_TYPE
from account.models import skills,CitiesModel

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
    location = forms.ModelChoiceField(
        queryset=CitiesModel.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),required=False
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
    
    skills_required = forms.ModelMultipleChoiceField(
    queryset=skills.objects.all(),
    widget=forms.SelectMultiple(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%;'
    }))
    
    class Meta:
        model = Jobpost
        fields = ["title","description","salary",
                  "job_type","employment_type",
                  "experience_required","location","location_type","skills_required"]

class JobFilterForm(forms.ModelForm):
    organization_name = forms.CharField(widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the organization name",
                "class": "form-control",
            }
        ))
    location_type = forms.CharField(widget= forms.TextInput(attrs={
        "placeholder":"Enter the job location",
        "class": "form-control",
    }))

    salary = forms.DecimalField(widget= forms.NumberInput(attrs={
        "placeholder":"Enter the salary",
        "class": "form-control",
    }))
    location = forms.CharField(widget= forms.TextInput(attrs={
        "placeholder":"Enter the job type or location ",
        "class": "form-control",
    }))
    job_name = forms.ChoiceField(widget=forms.Select(
            attrs={
                "placeholder": "select the required skills",
                "class": "form-control",
            }
        ))
    
    class Meta:
        model = Jobpost
        fields = ["title","description","salary","location","skills_required"]


class JobFilterForm(forms.Form):
    job_name = forms.ModelChoiceField(
        queryset=Jobpost.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    location_type = forms.ChoiceField(
        required=False,
        choices=LOCATION_TYPE,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    location = forms.ModelChoiceField(
        queryset=CitiesModel.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    job_type = forms.ChoiceField(choices=JOB_TYPE, widget=forms.Select(
        attrs={
        "class":"form-control",
        }))

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
    
    skills_required = forms.ModelMultipleChoiceField(
        queryset=skills.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control select2',
            'style': 'width: 100%;'
        })
    )

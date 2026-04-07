from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser,Organization,UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
                "class": "form-control",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter phone number",
                "class": "form-control",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
                "placeholder": "Enter password",
                "class": "form-control",
            }),
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={
                "placeholder": "Enter Confirm password",
                "class": "form-control",
            }),
        help_text=None,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "phone_number", "password1", "password2"]

class OrganizationRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
                "class": "form-control",
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter phone number",
                "class": "form-control",
            }
        )
    )
    organization_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Organization name",
                "class": "form-control",
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
                "placeholder": "Enter password",
                "class": "form-control",
            }),
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={
                "placeholder": "Enter Confirm password",
                "class": "form-control",
            }),
        help_text=None,
    )

    class Meta:
        model = CustomUser
        fields = ["organization_name", "email", "phone_number", "password1", "password2"]


class OrganizationProfileForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Organization name",
                "class": "form-control",
            }
        )
    )
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country'})
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'})
    ) 

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter address",
                "class": "form-control",
            }
        )
    )
    website = forms.URLField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter website URL",
                "class": "form-control",
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Enter description like what type of work you do",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Organization
        fields = ["name",  "country", "city", "address", "website", 'description']

class UserProfileForm(forms.ModelForm):

    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country'})
    )
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'})
    )

    address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter location",
                "class": "form-control",
            }
        )
    )
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "placeholder": "Upload profile picture",
                "class": "form-control",
            }
        ),
    )
    resume = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "placeholder": "Upload resume",
                "class": "form-control",
            }
        ),
    )
    skills = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Python, SQL, React'})
    )

    class Meta:
        model = UserProfile
        fields = ["country", "city","address", "profile_picture", "resume", "skills",]

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter email-address",
                "class": "form-control",
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": "form-control"}
        ),
    )

from django import forms

class ContactForm(forms.Form):
    fname=forms.CharField(label='First Name',
        widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter your first name'
                }
        )
    )

    lname = forms.CharField(label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }
        )
    )

    username = forms.CharField(label='User Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your user name'
            }
        )
    )
    password = forms.CharField(label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )
    email = forms.CharField(label='Email Id',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email Id'
            }
        )
    )
    mobile = forms.CharField(label='Mobile Number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your mobile number'
            }
        )
    )

class LoginForm(forms.Form):
    username=forms.CharField(label='User Name',
                             widget=forms.TextInput(
                                 attrs={
                                     'class':'form-control',
                                     'placeholder':'Enter your user name'
                                 }
                             )
                )
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Enter your password'
                                   }
                             )
                )

class CourseForm(forms.Form):
    fname=forms.CharField(label='First Name',
        widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter your first name'
                }
        )
    )

    lname = forms.CharField(label='Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }
        )
    )

    cname = forms.CharField(label='Course Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your course name'
            }
        )
    )

    email = forms.CharField(label='Email Id',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email Id'
            }
        )
    )

    mobile = forms.CharField(label='mobile',
        widget=forms.TextInput(
             attrs={
                 'class': 'form-control',
                 'placeholder': 'Enter your password'
             }
        )
    )
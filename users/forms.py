from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        error_messages={
            'required': 'El nombre de usuario es obligatorio.',
            'max_length': 'El nombre de usuario no puede exceder 150 caracteres.',
            'unique': 'Este nombre de usuario ya está en uso.',
        }
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Por favor, ingresa un correo electrónico.',
            'invalid': 'Ingresa un correo electrónico válido.',
        }
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        error_messages={
            'required': 'El nombre es obligatorio.',
            'max_length': 'El nombre no puede exceder 30 caracteres.',
        }
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        error_messages={
            'required': 'El apellido es obligatorio.',
            'max_length': 'El apellido no puede exceder 30 caracteres.',
        }
    )
    password1 = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Por favor, ingresa una contraseña.',
            'password_mismatch': 'Las contraseñas no coinciden.',
        }
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        strip=False,
        error_messages={
            'required': 'Por favor, confirma tu contraseña.',
            'password_mismatch': 'Las contraseñas no coinciden.',
        }
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
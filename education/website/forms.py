from django.forms import ModelForm, ImageField
from .models import Room, Post, User, NewStudent, NewTeacher
from django.contrib.auth.forms import UserCreationForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User

        labels = {
            'username': 'Nazwa użytkownika',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class NewTeacherForm(forms.ModelForm):
    class Meta:
        model = NewTeacher

        labels = {
            'name': 'Imie i nazwisko korepetytora',
            'phone_number': 'Numer telefonu',
            'school': 'Najwyższy osiągnięty stopień edukacji',
            'age': 'Wiek',
            'language': 'Czy znasz język polski na poziomie ojczystym?'
        }

        fields = ['name', 'phone_number', 'school', 'age', 'language']



class ApplyTeacherForm(UserCreationForm):
    class Meta:
        model = User

        labels = {
            'username': 'Nazwa użytkownika (będzie używana w Strefie Wiedzy)',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = NewStudent

        labels = {
            'name': 'Imie i nazwisko ucznia',
            'phone_number': 'Numer telefonu',
            'subject': 'Wybierz przedmiot',
            'school': 'Stopień edukacji',
            'level': 'Wybierz rodzaj zajęć',
        }

        fields = ['name', 'phone_number', 'subject', 'school', 'level']

class ApplyStudentForm(UserCreationForm):
    class Meta:
        model = User

        labels = {
            'username': 'Nazwa użytkownika (będzie używana w Strefie Wiedzy)',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

    image = ImageField(required=False)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class PostForm(forms.ModelForm):
    event_datetime = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        label='Data',  # You can customize the label here
        input_formats=['%Y-%m-%dT%H:%M'],  # Define the input format (adjust it to your needs)
    )

    class Meta:
        model = Post
        labels = {
            'title': 'Tytuł',
            'description': 'Opis',
            'course': 'Kurs',
        }
        fields = ['title', 'description', 'course', 'event_datetime']
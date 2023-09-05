from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    lessons = models.IntegerField(default=-1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class ContactMessage(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.email


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

    def preserve_user_on_delete(self):
        if self.host and self.host.deleted:
            self.host = None
            self.save()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='message_images/', blank=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    students = models.ManyToManyField(User, related_name='courses_enrolled', blank=True)
    courseCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-courseCreated']

    def __str__(self):
        return self.name


class Post(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='postParticipants', blank=True)
    postUpdated = models.DateTimeField(auto_now=True)
    postCreated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    event_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-postUpdated', '-postCreated']

    def __str__(self):
        return self.title


class CourseMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    messageUpdated = models.DateTimeField(auto_now=True)
    messageCreated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='message_images/', blank=True, null=True)

    class Meta:
        ordering = ['-messageUpdated', '-messageCreated']

    def __str__(self):
        return self.body[0:50]


class NewTeacher(models.Model):
    SCHOOL_CHOICES = [
        ('podstawowa', 'Szkoła podstawowa'),
        ('średnia', 'Szkoła średnia'),
        ('maturalna', 'Klasa maturalna'),
        ('praktyki', 'Praktyki'),
        ('licencjat', 'Licencjat'),
        ('magister', 'Magister'),
        ('inżynier', 'Inżynier'),
        ('doktor', 'Doktor'),
    ]

    LANGUAGE = [
        ('tak', 'Tak'),
        ('nie', 'Nie'),
    ]

    name = models.CharField(max_length=50, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Numer telefonu musi byc w formacie: '999 999 999'. Maksymalnie 15 cyfr."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    school = models.CharField(choices=SCHOOL_CHOICES, max_length=20, null=True)
    age = models.CharField(max_length=20, null=True)
    language = models.CharField(choices=LANGUAGE, max_length=20, null=True)

    def __str__(self):
        return self.name

class NewStudent(models.Model):
    SCHOOL_CHOICES = [
        ('podstawowa', 'Szkoła podstawowa'),
        ('średnia', 'Szkoła średnia'),
        ('maturalna', 'Klasa maturalna'),
        ('wyższa', 'Szkoła wyższa'),
    ]

    LEVEL_CHOICES = [
        ('rozwijające', 'Rozwijające'),
        ('koordynujące', 'Koordynujące'),
    ]

    name = models.CharField(max_length=50, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Numer telefonu musi byc w formacie: '999 999 999'. Maksymalnie 15 cyfr."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    subject = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    school = models.CharField(choices=SCHOOL_CHOICES, max_length=20, null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=20, null=True)

    def __str__(self):
        return self.name

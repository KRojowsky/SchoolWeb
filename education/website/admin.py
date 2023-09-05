from django.contrib import admin
from .models import Room, Topic, Message, Course, Post, CourseMessage, User, ContactMessage, NewStudent, NewTeacher
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'display_groups', 'lessons')
    list_display_links = ('email',)  # Make 'username' clickable to edit other fields
    list_editable = ('username', 'lessons')

    def display_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    display_groups.short_description = 'Groups'


admin.site.register(User, CustomUserAdmin)
admin.site.register(NewStudent)
admin.site.register(NewTeacher)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(CourseMessage)
admin.site.register(ContactMessage)


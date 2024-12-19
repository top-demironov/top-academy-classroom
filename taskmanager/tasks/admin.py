from django.contrib import admin

from tasks.models import Project, Task, User, StatusTask

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(StatusTask)
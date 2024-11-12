from django.contrib import admin

from qa.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
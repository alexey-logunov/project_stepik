from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'added_at', 'rating', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('author',)
    list_filter = ('author', 'title')


admin.site.register(Question, QuestionAdmin)
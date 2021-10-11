from django.contrib import admin
from .models import Question
from django.utils.safestring import mark_safe


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'added_at', 'rating', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('author',)
    list_filter = ('author', 'title')
    fields = ('title', 'text', 'added_at', 'rating', 'author', 'likes')
    readonly_fields = ('added_at', 'likes')
    save_on_top = True

    # def get_photo(self, obj):
    #     if obj.photo:
    #         return mark_safe(f'<img src="{obj.photo.url}" width="75">')
    #     else:
    #         return 'Фото не добавлено'
    #
    # get_photo.short_description = 'Фото'


admin.site.register(Question, QuestionAdmin)

admin.site.site_title = 'Управление вопросами'
admin.site.site_header = 'Управление вопросами'

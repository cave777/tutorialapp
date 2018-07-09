from django.contrib import admin
from .models import Lesson, Language, StudentExperience, TutorialSeries


# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'active',)


admin.site.register(Language, LanguageAdmin)

admin.site.register(StudentExperience)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'free_preview')
    exclude = ('slug',)


admin.site.register(Lesson, LessonAdmin)


class TutorialSeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'archived',)
    exclude = ('slug',)


admin.site.register(TutorialSeries, TutorialSeriesAdmin)

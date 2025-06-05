from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# The following class defines how the Choice model will be displayed as an inline within the Question model in the admin interface.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# The following class defines how the Question model will be displayed in the admin interface.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

# The following line registers the Question model with the admin site using the QuestionAdmin class.
admin.site.register(Question, QuestionAdmin)

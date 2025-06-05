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
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # Adds a "Filter" to the admin interface to filter questions by their publication date.
    list_filter = ["pub_date"]
    # Adds a "Search" box to the admin interface to search questions by their text.
    search_fields = ["question_text"]

# The following line registers the Question model with the admin site using the QuestionAdmin class.
admin.site.register(Question, QuestionAdmin)

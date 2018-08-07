from django.contrib import admin
# from models import Person
from blog.models import Person, Blog


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
    )
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'length',
    )
admin.site.register(Person, PersonAdmin)
admin.site.register(Blog, BlogAdmin)

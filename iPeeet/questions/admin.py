from django.contrib import admin
class Questions(admin.ModelAdmin):
    pass
admin.site.register(Author, Questions)
# Register your models here.

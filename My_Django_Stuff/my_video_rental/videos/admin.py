from django.contrib import admin
from videos import models


class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

    search_fields = ['title','length']

    list_filter = ['release_year','length','title']

    list_display = ['title','release_year','length']

    list_editable = ['length'] 

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)

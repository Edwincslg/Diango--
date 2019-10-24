
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Note, Note002

# admin.site.register(Note)


class Note002Inline(admin.TabularInline):
    model = Note002
    extra = 3


class NoteResource(resources.ModelResource):
   class Meta:
        model = Note


class NoteAdmin(ImportExportModelAdmin):
    resource_class = NoteResource
    # inlines = [SOPDetailInline]
    list_display = ('seq','subject','detail')
    # list_filter = ['is_active',]
    # ordering = ('app','page')
    
    inlines = [Note002Inline]
    search_fields = ['subject','detail']
   
admin.site.register(Note, NoteAdmin)
from django.contrib import admin

# Register your models here.

from .models import Word_Freq

class WordAdmin(admin.ModelAdmin):
  list_display = ('word', 'freq')
  list_display_links = ('word',)
  list_per_page = 25

admin.site.register(Word_Freq, WordAdmin)
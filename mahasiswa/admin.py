from django.contrib import admin

from .models import Mahasiswa

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'programstudi', 'angkatan')


# Register your models here.

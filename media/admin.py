from django.contrib import admin
from .models import *

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    display = ("description")

class AnimationAdmin(admin.ModelAdmin):
    display = ("description")

class MusicAdmin(admin.ModelAdmin):
    display = ("description")

class SimulationAdmin(admin.ModelAdmin):
    display = ("description")

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Animation, AnimationAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Simulation, SimulationAdmin)

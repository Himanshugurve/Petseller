from django.contrib import admin
from .models import Animal,Category,AnimalBreed,AnimalColor,AnimalLocation,AnimalImage

admin.site.register(Animal)
admin.site.register( Category)
admin.site.register(AnimalColor)
admin.site.register(AnimalBreed)
admin.site.register(AnimalLocation)
admin.site.register(AnimalImage)


class AnimalAdmin(admin.ModelAdmin):
    prepopulated_fields={'animal_slug':('animal_name',)}


# Register your models here.

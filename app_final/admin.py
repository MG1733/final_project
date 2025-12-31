from django.contrib import admin
from app_final.models import category,articles
# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display=['category_names','created_at']

class articlesadmin(admin.ModelAdmin):
    list_display=['title','author','category','updated_at','status']
    prepopulated_fields={
        'slug':('title',)
    }
admin.site.register(category,categoryadmin)
admin.site.register(articles,articlesadmin)

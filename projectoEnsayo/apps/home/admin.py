from models import Articles
from django.contrib import admin

class ArticlesAdmin(admin.ModelAdmin):
	fields = ['title', 'pub_date', 'autor', 'main_content']

admin.site.register(Articles, ArticlesAdmin)
from django.contrib import admin
from .models import Post

# Register your models here.



class PostAdmin(admin.ModelAdmin):
	#list of fields displayed in the admin page
	
	list_display=('title','slug','author','created')

	list_filter=('status','created','publish','author')

	search_fields=('title','author')

	prepopulated_fields={'slug':('title',)}
	
	data_hierachy='publish'
	
	ordering=['status','publish']

admin.site.register(Post,PostAdmin)

	
	

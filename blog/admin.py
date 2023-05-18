from django.contrib import admin
from .models import Blog,BlogParagraph,BlogImage

admin.site.register(Blog)
admin.site.register(BlogParagraph)
admin.site.register(BlogImage)
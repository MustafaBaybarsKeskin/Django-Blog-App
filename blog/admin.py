from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Blog)    # bu işlem direkt admin.register."" seklinde de yapilabilirdi.
class BlogAdmin(SummernoteModelAdmin):   
    list_display = ["id","title","author","created_date"]
    list_display_links = ["id","title","created_date"]
    search_fields = ["title","content"]
    list_filter = ["created_date"]
    list_editable = ()
    list_per_page = 20
    summernote_fields = ['content',]

    class Meta: 
        model = Blog

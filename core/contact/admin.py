from django.contrib import admin
from .models import Comments, Contacts, ReplyMessage, CommentAuthors

# Register your models here.

admin.site.register(Contacts)
admin.site.register(Comments)
admin.site.register(CommentAuthors)
admin.site.register(ReplyMessage)
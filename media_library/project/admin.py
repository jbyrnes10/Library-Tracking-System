from django.contrib import admin
from project.models import User, MediaItem, MediaHistory

class UserAdmin(admin.ModelAdmin):
    user_list = ('user_id', 'first_name', 'last_name')

class MediaAdmin(admin.ModelAdmin):
    library_media = ('title', 'author', 'type', 'isbn', 'past_borrowers', 'topic', 'subtopic')

class MediaHistoryAdmin(admin.ModelAdmin):
    history_list = ('date_out', 'date_due', 'date_returned', 'borrower')

admin.site.register(User, UserAdmin)
admin.site.register(MediaItem, MediaAdmin)
admin.site.register(MediaHistory, MediaHistoryAdmin)

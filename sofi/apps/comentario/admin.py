from django.contrib.comments.models import Comment
from django.contrib import admin

from evento.models import Evento
def evento(self):
    if self.content_type.name == "evento":
        return Evento.objects.get(id=self.object_pk)
            

Comment.add_to_class('evento', evento)

class ComentarioAdmin(admin.ModelAdmin):
    fields = ('is_public',)
    list_display = ('user_name', 'user_email', 'comment', 'submit_date', 'evento', 'is_public')
    list_filter = ('submit_date', 'is_public',)



admin.site.unregister(Comment)
admin.site.register(Comment, ComentarioAdmin)

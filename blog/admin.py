from django.contrib import admin

# Register your models here.

from .models import Post

# Register your models here.
admin.site.register(Post)


'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        import logging
        logger = logging.getLogger(__name__)
        try:
            return super().changelist_view(request, extra_context)
        except Exception:
            logger.exception("Post admin changelist failed")
            raise
            '''
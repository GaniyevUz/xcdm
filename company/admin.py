from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import TextField
from django.utils.html import format_html, strip_tags
from django_ckeditor_5.widgets import CKEditor5Widget
from modeltranslation.admin import TranslationAdmin
from ordered_model.admin import OrderedModelAdmin

from .models import Category, Project, Blog, Faq, TeamCategory, TeamMember, TeamPosition
from re import search


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    exclude = ('slug',)
    list_display = ['id', 'title', 'type', 'image_logo', 'description_short', 'project_type', 'preview',
                    'description_long', 'video', 'image', 'youtube_link']

    def image(self, obj: Project):
        if obj.image:
            return format_html(f'<img style="border-radius: 5px;" width="50px" height="50px" src="{obj.image.url}"/>')
        return "No Image"

    image.short_description = 'Project Image'


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'create_at', 'banner_image']
    formfield_overrides = {
        TextField: {'widget': CKEditor5Widget},
    }
    list_display_links = ('id', 'title')

    def banner_image(self, obj: Blog):
        if obj.banner:
            return format_html(f'<img style="border-radius: 5px;" width="100px" height="35px" src="{obj.banner.url}"/>')
        return "No Image"

    banner_image.short_description = 'Banner'


@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(TeamCategory)
class TeamCategoryAdmin(OrderedModelAdmin):
    list_display = ['id', 'title', 'move_up_down_links']


@admin.register(TeamPosition)
class TeamPositionAdmin(TranslationAdmin):
    list_display = ['id', 'title']


@admin.register(TeamMember)
class TeamMemberAdmin(OrderedModelAdmin):
    exclude = ('slug',)
    list_display = ['id', 'full_name', 'image_html', 'position', 'linkedin_url', 'move_up_down_links']
    list_display_links = ('id', 'full_name')
    sortable_by = 'position', 'full_name'

    def image_html(self, obj: TeamMember):
        if obj.image:
            return format_html(f'<img style="border-radius: 5px;" width="50px" height="50px" src="{obj.image.url}"/>')
        return "No Image"

    image_html.short_description = 'Image'

    def linkedin_url(self, obj: TeamMember):
        pattern = r'linkedin\.com\/(?:in|company)\/([a-zA-Z0-9\-]+)\/?'
        match = search(pattern, obj.linkedin)
        if match:
            return format_html(f'<a href="{obj.linkedin}">{match.group(1)}</a>')
        return format_html(f'<a href="{obj.linkedin}">{obj.linkedin}</a>')

    linkedin_url.short_description = 'Linkedin'

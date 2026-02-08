from django.contrib import admin
from .models import Project, Resume, Skill, About


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_editable = ['featured', 'order']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Display Settings', {
            'fields': ('featured', 'order')
        }),
    )

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'uploaded_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'uploaded_at']
    readonly_fields = ['uploaded_at', 'updated_at']
    fieldsets = (
        ('Resume Information', {
            'fields': ('title', 'file', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('uploaded_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order']

    fieldsets = (
        ('Skill Details', {
            'fields': ('name', 'category', 'proficiency', 'order')
        }),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'updated_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'updated_at']
    readonly_fields = ['updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'profile_image', 'is_active')
        }),
        ('Content', {
            'fields': ('about_content', 'education_content'),
            'description': 'You can use HTML tags for formatting'
        }),
        ('Timestamps', {
            'fields': ('updated_at',),
            'classes': ('collapse',)
        }),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        """Use textarea for text fields to support HTML editing"""
        if db_field.name in ['about_content', 'education_content']:
            kwargs['widget'] = admin.widgets.AdminTextareaWidget()
        return super().formfield_for_dbfield(db_field, request, **kwargs)

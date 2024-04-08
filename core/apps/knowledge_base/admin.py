from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Characteristic, Skill, Language, Section, Source, Die, Coin, Alignment


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    ordering = ('title',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title')
    list_display_links = ('title',)
    ordering = ('title',)


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_skills', 'section', 'source')
    list_display_links = ('title',)
    ordering = ('pk',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('skills')

    @admin.display(description='Skills')
    def display_skills(self, obj: Characteristic):
        skill_links = []
        for skill in obj.skills.all():
            skill_url = reverse(f'admin:{skill._meta.app_label}_{skill._meta.model_name}_change', args=[skill.id])
            skill_links.append(f'<a href="{skill_url}">{skill.title}</a>')

        return format_html('<br>'.join(skill_links))


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'characteristic', 'section', 'source')
    list_display_links = ('title',)
    ordering = ('title',)
    search_fields = ('title', 'characteristic__title', 'description')
    list_filter = ('characteristic',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'speakers', 'script', 'description', 'section', 'source')
    list_display_links = ('title',)
    list_filter = ('type',)
    ordering = ('title',)


@admin.register(Die)
class DieAdmin(admin.ModelAdmin):
    list_display = ('title', 'modifier', 'section', 'source')


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_title', 'rate', 'section', 'source')


@admin.register(Alignment)
class AlignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'section', 'source')

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Characteristic, Skill


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'display_skills')
    list_display_links = ('title',)
    ordering = ('pk',)

    @admin.display(description='Skills')
    def display_skills(self, obj: Characteristic):
        skill_links = []
        for skill in obj.skills.all():
            skill_url = reverse(f'admin:{skill._meta.app_label}_{skill._meta.model_name}_change', args=[skill.id])
            skill_links.append(f'<a href="{skill_url}">{skill.title}</a>')

        return format_html('<br>'.join(skill_links))


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'characteristic')
    list_display_links = ('title',)
    ordering = ('title',)
    search_fields = ('title', 'characteristic__title', 'description')
    list_filter = ('characteristic',)

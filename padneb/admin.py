from django.contrib import admin
from .models import Member, Chapter, Guardian, Contribution
# Register your models here.


class MemberList(admin.ModelAdmin):
    list_display = ('first_name', 'middle_initial', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')
    search_fields = ('last_name', )
    ordering = ['last_name']


class ChapterList(admin.ModelAdmin):
    list_display = ('code_chapter', 'chapter_name')
    search_fields = ('chapter_name',)
    ordering = ['chapter_name']


class ContributionList(admin.ModelAdmin):
    list_display = ('member', 'date', 'amount', 'type')
    search_fields = ('member',)
    ordering = ['member']


class GuardianList(admin.ModelAdmin):
    list_display = ('member', 'fist_name', 'last_name', 'relation_to_member')
    search_fields = ('member',)
    ordering = ['member']


admin.site.register(Chapter, ChapterList)
admin.site.register(Member, MemberList)
admin.site.register(Guardian, GuardianList)
admin.site.register(Contribution, ContributionList)

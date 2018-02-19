from django.contrib import admin
from stories.models import *


class ChapterInline(admin.StackedInline):
	model = Chapter
	extra = 0

class CharacterInline(admin.StackedInline):
	model = Character
	extra = 0

class PlaceInline(admin.StackedInline):
	model = Place
	extra = 0

class SkillInLine(admin.StackedInline):
	model = Skill
	extra = 0

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
	inlines = (ChapterInline, CharacterInline, PlaceInline,)
	prepolulated_fields = {'slug': ('title',)}
	list_display = ('title', 'author', 'user', 'id',)
	list_filter = ('author', 'user',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
	prepolulated_fields = {'slug': ('title',)}
	list_display = ('title', 'number', 'story',)
	list_filter = ('story',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	prepolulated_fields = {'slug': ('title',)}
	list_display = ('name', 'story',)
	list_filter = ('story',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	prepolulated_fields = {'slug': ('title',)}
	list_display = ('name', 'story',)
	list_filter = ('story',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	prepolulated_fields = {'slug': ('title',)}
	list_display = ('name', 'place', 'story',)
	list_filter = ('story', 'place')
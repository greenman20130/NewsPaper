from django.contrib import admin
from .models import Category, Post
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)
 
 
# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display =  ('title', 'text', 'author_id')
    list_filter = ('author', 'category',) # добавляем примитивные фильтры в нашу админку
    search_fields = ('title',) # тут всё очень похоже на фильтры из запросов в базу
 
class CategoryAdmin(TranslationAdmin):
    model = Category
 
 
class MyModelAdmin(PostAdmin, TranslationAdmin):
    model = Post
 
# Register your models here.
 
admin.site.register(Category)
admin.site.register(Post, MyModelAdmin)

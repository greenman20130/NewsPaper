from .models import Category, MyModel, Post
from modeltranslation.translator import register, TranslationOptions # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться
 
 
# регистрируем наши модели для перевода
 
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category', ) # указываем, какие именно поля надо переводить в виде кортежа
 
 
@register(MyModel)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Post)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
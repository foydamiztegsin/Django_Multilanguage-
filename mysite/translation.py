from .models import Categories, Products
from modeltranslation.translator import TranslationOptions, register

@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Products)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('product_name', 'product_discription')
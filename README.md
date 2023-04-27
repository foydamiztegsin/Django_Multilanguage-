# Loyiha ikki bosqichdan iborat!
    - 1 - bosqich: Loyihani o'zgarmaydigan sozlarni  tarjima qilib chiqish
    - 2 - bosqich: O'zimizning modelimizni ko'p tillik qilish ma'lmotlarni chiqarish


# Kerakli dasturni o'rnatib oling: [Gettext](https://mlocati.github.io/articles/gettext-iconv-windows.html)


# 1. Loyihani yaratishni boshlang.

```rb
mkdir DjangoMultilanguage 
cd DjangoMultilanguage
mkdir templates
mkdir static

django-admin startproject myproject .
python manage.py startapp mysite

```

- Loyiha uchun muhit yarating:

```rb
python -m venv venv
venv\Scripts\activate
```

- Loyiha setting.py fayliga appni kiriting:

```rb
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',  # siz yaratgan app
]
```
- Loyiha setting.py faylida templates ni sozlash:

```rb
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Loyiha setting.py faylida static ni sozlash:

```rb
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
```

- Loyiha setting.py faylida language(tillar sozlamalari) sozlash:

```rb
from django.utils.translation import gettext_lazy as  _
LANGUAGES = [
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
]
LOCALE_PATHS = [
    BASE_DIR/'locale/',   # locale nomli papka yarating uni ichida  uz va  ru papkalarni hosil qiling
]
```

- Middlewareni o'zgartish kiriting:

```rb
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',              # kiritish
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

- templates papkasiga index.html fayl yarating:
    - birinchi o'zgartirilmagan htmlni, templates papakasini ichidagi firsthtml faylida topasiz!


- Siz yaratgan app ichidagi views.py fayliga quydagilarni yozing:
```rb
#(fuksiya ko'rinishi)
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')
```

- Loyiha urls.py fayliga quydagilarni kiritib qoýing:

```rb
from django.contrib import admin
from django.urls import path
from mysite import views                                         # kiritish
from django.conf.urls.i18n import i18n_patterns                  # kiritish

urlpatterns = i18n_patterns(                                     # kiritish
    path('admin/', admin.site.urls),
    path('',views.homepage),                                     # kiritish
)
```

- html faylimizdagi sozlarni tarjima qilish uchun 
kodlarni bosh qismiga 
```rb 
{% load i18n %}


<h3>Главные категории</h3>
<h3>{% trans 'Главные категории' %} </h3>   # kerakli sozlarni tarjima qilish usuli

``` 
yozing va kerakli sozni shu ko'rinishga o'zgartiring

- O'zgatirib bo'lgach terminal orqali ushbu buyruqni bering:

```rb
django-admin makemessages --all
``` 
processing locale ru
processing locale uz  #ushbu ko'rinishda javob olishingiz kerak!


- locale faylidan uz papkasiga kiring va ichidagi faylni oching ushbu kodni qidiring:

```rb
#: .\templates\index.html:627
msgid "Главные категории"
msgstr "Bosh toifalar"              # qo'lda kiriting
``` 
locale faylidan ru papkasiga kiring va ichidagi faylni oching ushbu kodni qidiring:

```rb
#: .\templates\index.html:627
msgid "Главные категории"
msgstr "Главные категории"           # qo'lda kiriting
``` 
yozib bo'lgach terminal orqali ushbu buyruqni bering: tasdiqlash uchun
```rb
django-admin compilemessages
```
fayllarni compile qilib chiqadi, kuting....

- Loyihani ishga tushiring

```rb
loyiha ushbu manzilda ishga tushadi:                   "http://127.0.0.1:8000/uz/"
Rus tilini tekshirish uchun uz ni ru ga o'zgartiring:  "http://127.0.0.1:8000/ru/"
``` 

<hr>
<hr>

# 2 - bosqich
- Modelsda ma'lumotlarimizni ham ko'p tillik qilish:

- Fayllarga o'zgaritirish kiritishni boshlang:
loyiha setting.py fayliga 


```rb
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'modeltranslation',    # malumotlarni ikkita tillik qilish uchun
    'mysite',  # siz yaratgan app
]
```

- Siz yaratgan app ichdagi models.py da kerakli modellarni yarating

from django.db import models

```rb
class Categories(models.Model):
    name                = models.CharField(max_length=150)
    
    
class Products(models.Model):
    category_id         = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name        = models.CharField(max_length=250)
    product_price       = models.IntegerField()
    product_discription = models.TextField()
```


- terminal orqali buyruqlarni bering

```rb
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # user yaratib oling admin qismidan mahsulot kiritish uchun
```

- Siz yaratgan app ichda admin.py fayliga kodlarni yozing:

```rb
from django.contrib import admin
from .models import Categories, Products
from django.contrib.auth.models import User,Group
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Categories)
admin.site.register(Products)
```

- Siz yaratgan app ichda views.py fayliga o'zgarishlarni yozing:

```rb
from django.shortcuts import render
from .models import Categories, Products
# Create your views here.
def homepage(request):
    
    categories = Categories.objects.all()
    products = Products.objects.all()
    data = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', data)

```

- App(siz yaratgan app) ichda translation.py faylini hosil qiling va kodlarni yozing:

```rb
from .models import Categories, Products
from modeltranslation.translator import TranslationOptions, register

@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Products)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('product_name', 'product_discription')
```

- terminal orqali buyruqlarni bering:

```rb
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- "html kodlarini qolgan bosqichlari kodlari loyiha fayllarida mavjud asosiylari qo'llanmada yozib chiqildi"

 <hr>
 Mehnatimiz sizga foyda berayotgan bolsa GITHUB profilimizga obuna bo'ling va telegram kanalimizda reaksiyalarni qoldiring 👍
 
# *E'tiboringiz uchun rahmat* Savollaringiz bo'lsa [Telegram](https://t.me/foydamizteg_sin)

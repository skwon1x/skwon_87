from django.contrib import admin
from .models import OnlineShop

# Register your models here.

# login admin pass 1

# Создаём класс для отображения модели в админ панели
class OnlineShopAdmin(admin.ModelAdmin):
    # created_date это функция объявленная в models.OnlineShop для отображения поля created_time
    # updated_date это функция объявленная в models.OnlineShop для отображения поля updated_time
    list_display = ['id', 'title', 'description', 'price', 
                    'created_date', 'updated_date', 'auction', 'image', 'user'
                ]
    list_filter = ['auction', 'created_time']
    
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image', 'user')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(OnlineShop, OnlineShopAdmin)
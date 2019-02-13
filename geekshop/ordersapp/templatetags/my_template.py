from django import template
from django.conf import settings

register = template.Library()

URL_PREFIX = '/media/'

# def media_folder_products(string):
#     if not string:
#         string = 'products_images/default.jpg'
# MEDIA_URL подставляем из файла настроек проекта settings.py
#     return f'{settings.MEDIA_URL}{string}'
# или можно, так используя URL_PREFIX:
def media_folder_products(string):
    if not string:
        string = 'products_images/default.jpg'

    new_string = "{}{}".format(URL_PREFIX, string)

    return new_string

@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/default.jpg'
    # MEDIA_URL подставляем из файла настроек проекта settings.py
    return f'{settings.MEDIA_URL}{string}'

register.filter('media_folder_products', media_folder_products)


# для проверки(файл можно запускать как есть)
if __name__ == '__main__':
    print(media_folder_products('products_images/product1.jpg'))
    print(media_folder_products(''))
from django.contrib import admin
from .models import Book,Publisher,Author

# Register your models here.


admin.site.register([Book,Publisher,Author])
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     search_fields = list_display
#     list_filter = list_display
#
#
# @admin.register(Publisher)
# class PublisherAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     search_fields = list_display
#     list_filter = list_display
#
#
# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     search_fields = list_display
#     list_filter = list_display
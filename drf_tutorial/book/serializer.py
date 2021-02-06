from rest_framework.validators import UniqueTogetherValidator

from .models import Book
from rest_framework import serializers
from .models import Book,Author,Publisher


# 当前只会展示出作者的id,如何展示出作者 的具体信息？
"""
 {
            "id": 1,
            "title": "python入门",
            "price": "9.90",
            "publish": 1,
            "authors": [
                1
            ]
        }
"""
# 方案一：会展示出作者的所有信息
"""
        {
            "id": 1,
            "title": "python入门",
            "price": "9.90",
            "publish": {
                "id": 1,
                "name": "清华出版社",
                "address": "北京"
            },
            "authors": [
                {
                    "id": 1,
                    "name": "arvin",
                    "age": 18,
                    "gender": true
                }
            ]
        }
"""
# 方案二：可以指定要展示作者的哪些信息
"""
 {
            "id": 1,
            "authors": [
                {
                    "name": "arvin"
                }
            ],
            "title": "python入门",
            "price": "9.90",
            "publish": 1
        }
"""
# 方案三 ,默认展示的Author的__str__方法
"""
{
            "id": 1,
            "authors": [
                "arvin"
            ],
            "title": "python入门",
            "price": "9.90",
            "publish": 1
        }
"""
# 方案四（推荐）
"""
{
            "id": 1,
            "authors": [
                "arvin"
            ],
            "title": "python入门",
            "price": "9.90",
            "publish": 1
        }
"""


# 自定义校验，三种方案
# https://www.django-rest-framework.org/api-guide/serializers/#validation
# 方案A：校验单个字段
# 方案B：校验所有字段
# 方案C：可以把需要重复使用的校验单独写成函数

def multiple_of_two(value):
    if value % 2 != 0:
        raise serializers.ValidationError('Not a multiple of two')


class AuthorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Author
        fields = ['name']


class BookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)

class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)  # 方案二
    # authors = serializers.StringRelatedField(many=True)  # 方案三
    authors = serializers.SlugRelatedField(  # 方案四
        many=True,
        # read_only=True,
        queryset=Author.objects.all(),
        slug_field='name',  # 指定要展示的字段
        allow_null=False
    )
    price = serializers.DecimalField(max_digits=6, decimal_places=2, validators=[multiple_of_two])  # 方案C

    def validate_price(self, value):  # 方案A：校验单个字段,value 是字段值
        if value < 0 or value > 100:
            raise serializers.ValidationError("价格必须在0到100之间。")
        return value

    def validate(self, attrs):  # 方案B：校验多个字段，attrs是所有字段值
        print(attrs)

        return attrs

    def validated_authors(self, value):
        print('authors', value)
        return value

    class Meta:
        model = Book
        fields = '__all__'
        list_serializer_class = BookListSerializer
        # exclude = []  # 指定要排除的字段
        # depth = 2  # 方案一：会展示出作者的所有信息






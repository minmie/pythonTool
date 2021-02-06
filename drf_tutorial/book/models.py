from django.db import models

# Create your models here.


class Author(models.Model):
    gender_choices = (
        (True, '男'),
        (False, '女')
    )

    name = models.CharField(max_length=32)
    age = models.SmallIntegerField(default=18)
    gender = models.BooleanField(choices=gender_choices)

    class Meta:
        db_table = 'AUTHOR'  # 表名
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Publisher(models.Model):

    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    class Meta:
        db_table = 'PUBLISHER'  # 表名
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # publish = models.ForeignKey(to=Publisher, on_delete=models.CASCADE,null=True,blank=True)  # null=True：允许数据库存储空值；blank=True：允许前端不填该值，两个默认都是False
    publish = models.ForeignKey(to=Publisher, on_delete=models.CASCADE,null=True)  # null=True：允许数据库存储空值；blank=True：允许前端不填该值，两个默认都是False
    authors = models.ManyToManyField(to=Author, related_name='books')   # related_name 用于反向查询;多对多字段允许为空

    class Meta:
        db_table = 'BOOK'  # 表名
        verbose_name = "书籍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
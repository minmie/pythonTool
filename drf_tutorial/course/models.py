from django.db import models
from django.conf import settings
# Create your models here.

# help_text: 前端展示提示
# verbose_name： 字段信息
# auto_now_add： 创建时自动填充时间
# auto_now： 更新是自动填充时间

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="课程名称", verbose_name="名称")
    introduction = models.TextField(help_text="课程简介", verbose_name="简介")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                help_text="课程讲师", verbose_name="讲师")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="课程价格", verbose_name="价格")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'COURSE'  # 表名
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name
        ordering = ("price",)  # 排序字段

    def __str__(self):
        return self.name

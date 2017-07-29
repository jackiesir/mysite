from django.db import models

# Create your models here.

#  数据库里面创建Reporter表
class Reporter(models.Model):
    #创建 full_name 数据库字段，并设置改字段为文本类型，长度为70个字符
    full_name=models.CharField(max_length=70)
    #modles.py中class设置的数据,本身返回为一个类,如果想直接返回某一个字段的值,可以定义__str__,比如:
    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
    def __str__(self):
        return self.headline


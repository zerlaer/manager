from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()


class Message(models.Model):
    name = models.CharField(max_length=100)  # 留言人
    content = models.TextField()  # 留言内容
    time = models.TimeField(auto_now_add=True)  # 留言时间

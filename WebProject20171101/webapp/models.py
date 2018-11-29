#-*-coding:utf-8-*-
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(u"博客标题",max_length = 100)        #博客标题
    category = models.CharField(u"博客标签",max_length = 50,blank = True)       #博客标签
    pub_date = models.DateTimeField(u"发布日期",auto_now_add = True,editable=True)       #博客发布日期
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    content = UEditorField(u"文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/webapp/images/",
                           toolbars='besttome',filePath='uploads/webapp/files/')

    def __str__(self):
        return self.title

    class Meta:     #按时间下降排序
        ordering = ['-pub_date']
        verbose_name = "文章"
        verbose_name_plural = "文章"
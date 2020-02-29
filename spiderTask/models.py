from django.db import models

from datetime import datetime
from django.db import models


class BaseMode(models.Model):
    class Meta:
        abstract = True

    def to_dict(self, *ignore_fileds):
        '''将一个 model 转换成一个 dict'''
        attr_dict = {}
        for field in self._meta.fields:  # 遍历所有字段
            name = field.attname  # 取出字段名称
            if name not in ignore_fileds:  # 检查是否是需要忽略的字段
                tem_attr = getattr(self, name)
                if isinstance(tem_attr, datetime):
                    attr_dict[name] = tem_attr.strftime("%Y-%m-%d %X")  # 获取字段对应的值
                else:
                    attr_dict[name] = getattr(self, name)  # 获取字段对应的值
        return attr_dict


class Temp(BaseMode):
    class Meta:
        verbose_name_plural = '零时打卡记录'
        db_table = 'temp'

    name = models.CharField(max_length=255, default='', verbose_name='名字')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class Employee(BaseMode):
    class Meta:
        verbose_name_plural = '员工信息表'
        db_table = 'employee'

    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    name = models.CharField(max_length=255, default='', verbose_name='姓名')
    age = models.IntegerField(default=33, verbose_name='年龄')
    phone = models.CharField(max_length=255, default='', verbose_name='手机号')
    sex = models.CharField(max_length=10, choices=SEX, verbose_name='性别')
    img = models.ImageField(verbose_name='本人头像', upload_to='emplyeePic/')
    jobTime = models.DateTimeField(auto_now=True, verbose_name='入职时间')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class JobConf(BaseMode):
    class Meta:
        verbose_name_plural = '上下班时间配置表'
        db_table = 'jobconf'

    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    name = models.CharField(max_length=255, default='', verbose_name='标题')
    startTime = models.TimeField(verbose_name='工作开始时间')
    endTime = models.TimeField(verbose_name='工作结束时间')
    isSelect = models.CharField(max_length=10, default='0', verbose_name='是否生效')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class CountRet(BaseMode):
    class Meta:
        verbose_name_plural = '出勤记录表'
        db_table = 'countret'

    name = models.CharField(max_length=255, default='', verbose_name='员工姓名')
    startTime = models.TimeField(verbose_name='上班时间')
    endTime = models.TimeField(verbose_name='下班时间')
    couldStartTime = models.TimeField(verbose_name='规定上班时间', null=True)
    couldEndTime = models.TimeField(verbose_name='规定下班时间', null=True)
    dec = models.CharField(max_length=255, default='', verbose_name='出勤描述')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

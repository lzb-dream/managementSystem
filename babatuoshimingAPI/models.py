from django.db import models
import datetime

class Materiel(models.Model):
    # 添加者
    add_name = models.CharField(max_length=200, blank=True)
    # 货物类名
    cargo_name = models.CharField(max_length=200, default=None)
    # 货物子类
    cargo_info = models.JSONField(default=list)
    # 货物类添加时间
    add_time = models.DateTimeField(null=True)
    # 入库数量
    quantity_in_storage = models.IntegerField(default=0)
    # 使用数量
    quantity_used = models.IntegerField(default=0)
    # 出库数量
    outbound_quantity = models.IntegerField(default=0)
    # 损耗数量
    loss_quantity = models.IntegerField(default=0)
    # 库存数量
    available_quantity = models.IntegerField(default=0)
    # 进货对象
    merchant = models.CharField(max_length=50, blank=True)
    # 货物类备注
    remark = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'materiel'
        verbose_name = '货物管理'
        verbose_name_plural = verbose_name


class Users(models.Model):
    username = models.CharField(max_length=255,default='用户', verbose_name='用户')
    account_number = models.CharField(max_length=10, verbose_name='账号', unique=True)
    password = models.CharField(max_length=20,verbose_name='密码')
    addTime = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        (0, '禁用'),
        (1, '教师'),
        (2, '财务'),
        (3, '超级管理员')
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    class Meta:
        db_table = 'users'
        verbose_name = '所有用户'
        verbose_name_plural = verbose_name


# 申请使用的表，并记录使用记录
class UseLogList(models.Model):
    submitter = models.ForeignKey(to=Users, on_delete=models.SET_NULL, null=True)
    user_class = models.CharField(max_length=20)
    user_log = models.CharField(max_length=255)

    class Meta:
        db_table = 'Use_log_list'
        verbose_name = '所有用户'
        verbose_name_plural = verbose_name



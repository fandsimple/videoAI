from django.contrib import admin

from spiderTask.models import Temp, Employee, JobConf, CountRet

admin.site.site_header = '智能打卡系统'
admin.site.site_title = '智能打卡系统'


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10  # 每页显示多少条
    actions_on_top = True  # 顶部操作显示
    actions_on_bottom = True  # 底部操作显示
    actions_selection_counter = True  # 选中条数显示
    empty_value_display = ' 空白 '  # 空白字段显示格式


@admin.register(Temp)
class TempAdmin(BaseAdmin):
    ordering = ('id',)
    list_display = ("name", 'createTime')  # 显示字段
    search_fields = ('name',)  # 搜索条件配置
    list_filter = ('name',)  # 过滤字段配置
    # list_editable = ['taskName']

    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


@admin.register(Employee)
class TempAdmin(BaseAdmin):
    ordering = ('id',)
    list_display = (
        'name',
        'age',
        'phone',
        'sex',
        'img',
        'jobTime',
        'createTime',
    )  # 显示字段
    search_fields = ('name',)  # 搜索条件配置
    list_filter = ('sex', 'age')  # 过滤字段配置
    # list_editable = ['taskName']

    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


@admin.register(JobConf)
class TempAdmin(BaseAdmin):
    ordering = ('id',)
    list_display = (
        'name',
        'startTime',
        'endTime',
        'isSelect',
        'createTime',
    )  # 显示字段
    search_fields = ('name',)  # 搜索条件配置
    # list_filter = ('sex', 'age')  # 过滤字段配置
    # list_editable = ['taskName']

    # list_display_links = ('id', 'caption') # 配置点击进入详情字段



@admin.register(CountRet)
class TempAdmin(BaseAdmin):
    ordering = ('id',)
    list_display = (
        'name',
        'startTime',
        'endTime',
        'couldStartTime',
        'couldEndTime',
        'dec',
        'createTime',
    )  # 显示字段
    search_fields = ('name',)  # 搜索条件配置
    list_filter = ('dec', )  # 过滤字段配置
    # list_editable = ['taskName']

    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import django
import datetime
import time
import pdb

sys.path.append('/Users/fanding/spiderAdmin')  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'spiderAdmin.settings'  # 设置项目的配置文件
django.setup()  # 加载项目配置

from spiderTask.models import Employee, Temp, CountRet, JobConf


def time_cmp(first, second):
    return int(first.strftime("%H%M%S")) - int(second.strftime("%H%M%S"))


def countRet():
    users = Employee.objects.all()
    jobconf = JobConf.objects.filter(isSelect='1')
    if not jobconf:
        print('数据库配置错误')
    ruleStartTime = jobconf[0].startTime
    ruleEndTime = jobconf[0].endTime
    for user in users:
        msg = ''
        # pdb.set_trace()
        jobRet = Temp.objects.filter(name=user.name).order_by('createTime')

        todayInfo = datetime.datetime.now().strftime("%Y-%m-%d").split('-')
        todayInfo = datetime.date(int(todayInfo[0]), int(todayInfo[1]), int(todayInfo[2]))
        ret = CountRet.objects.filter(createTime__startswith=todayInfo).filter(name=user.name)
        if ret:
            # 库中已经存在此统计数据
            continue

        if not jobRet:
            # 当日没来
            countret = CountRet()
            countret.name = user.name
            countret.startTime = datetime.datetime(1995, 10, 24)
            countret.endTime = datetime.datetime(1995, 10, 24)
            countret.couldStartTime = ruleStartTime
            countret.couldEndTime = ruleEndTime
            countret.dec = '当日没来'
            countret.save()
        elif len(jobRet) == 1:
            # 只签到一次
            dbTime = jobRet[0].createTime
            res = time_cmp(ruleStartTime, dbTime)
            if res >= 0:
                msg = '正常出勤，早退'
            else:
                msg = '迟到，早退'

            countret = CountRet()
            countret.name = user.name
            countret.startTime = dbTime
            countret.endTime = datetime.datetime(1995,10,24)
            countret.couldStartTime = ruleStartTime
            countret.couldEndTime = ruleEndTime
            countret.dec = msg
            countret.save()

        elif len(jobRet) == 2:
            # 签到两次
            dbStartTime = jobRet[0].createTime
            dbEndTime = jobRet[1].createTime
            res1 = time_cmp(ruleStartTime, dbStartTime)
            res2 = time_cmp(ruleEndTime, dbEndTime)
            if res1 >= 0:
                msg = '正常出勤'
            else:
                msg = '迟到'
            if res2 <= 0:
                msg += ',正常出勤'
            else:
                msg += ',早退'
            countret = CountRet()
            countret.name = user.name
            countret.startTime = dbStartTime
            countret.endTime = dbEndTime
            countret.couldStartTime =ruleStartTime
            countret.couldEndTime = ruleEndTime
            countret.dec = msg
            countret.save()



if __name__ == '__main__':
    countRet()

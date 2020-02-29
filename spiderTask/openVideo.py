#!/usr/bin/python
# -*- coding: utf-8 -*-

import face_recognition
import cv2
import os
import sys
import django
sys.path.append('/Users/fanding/spiderAdmin')  # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'spiderAdmin.settings'  # 设置项目的配置文件
django.setup()  # 加载项目配置

from spiderTask.models import Temp
import datetime
import time


def writeToDb(face_names):
    if not face_names:
        return
    for pface in face_names:
        if pface == 'unknown':
            continue
        else:
            now = datetime.datetime.today()
            now = datetime.datetime(now.year, now.month, now.day)
            after = now + datetime.timedelta(days=1)
            temp = Temp.objects.filter(name=pface).order_by('-createTime').filter(createTime__range=(now, after))
            if len(temp) >= 2:
                continue
            elif temp:
                # 判断与上次打卡时间是否相差5分钟
                dbTime = temp[0].createTime
                currentTime = datetime.datetime.now()
                print((currentTime - dbTime).seconds)
                if (currentTime - dbTime).seconds <= 10:
                    continue
                temp = Temp()
                temp.name = pface
                temp.save()
            else:
                temp = Temp()
                temp.name = pface
                temp.save()


def face(path):
    # 存储知道人名列表
    known_names = []
    # 存储知道的特征值
    known_encodings = []
    for image_name in os.listdir(path):
        load_image = face_recognition.load_image_file(os.path.join(path, image_name))  # 加载图片
        image_face_encoding = face_recognition.face_encodings(load_image)[0]  # 获得128维特征值
        known_names.append(image_name.split(".")[0])
        known_encodings.append(image_face_encoding)
    print(known_encodings)

    # 打开摄像头，0表示内置摄像头
    video_capture = cv2.VideoCapture(0)

    process_this_frame = True

    while True:
        ret, frame = video_capture.read()
        # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
        rgb_frame = frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_frame)  # 获得所有人脸位置
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  # 获得人脸特征值
            face_names = []  # 存储出现在画面中人脸的名字
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_names[first_match_index]
                else:
                    name = "unknown"
                face_names.append(name)

        # 存储人名字
        print(face_names)
        writeToDb(face_names)

        process_this_frame = not process_this_frame
        # 将捕捉到的人脸显示出来
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)  # 画人脸矩形框
            # 加上人名标签
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    # face("/Users/fanding/gitProjects/spiderAdmin/spiderTask/images")  # 存放已知图像路径
    face("/Users/fanding/spiderAdmin/static/upload/emplyeePic")  # 存放已知图像路径

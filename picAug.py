import csv
import os
import shutil
from keras.preprocessing.image import ImageDataGenerator
import cv2
datagen = ImageDataGenerator(
    rotation_range=180, # 角度值，0~180，影象旋轉
    width_shift_range=0.2, # 水平平移，相對總寬度的比例
    height_shift_range=0.2, # 垂直平移，相對總高度的比例
    shear_range=20, # 隨機錯切換角度
    zoom_range=[1,1.5], # 隨機縮放範圍
    horizontal_flip=True, # 一半影象水平翻轉
    vertical_flip=True,
    fill_mode='reflect', # 填充新建立畫素的方法
    brightness_range=[0.5, 1.3],#亮度調整範圍
    channel_shift_range =50,#通道偏移
)
classes =os.listdir('./flowers/')
for pClass in classes:
    print(pClass)
    dirs = os.listdir('./flowers/'+pClass)
    for pic in dirs:
      img = cv2.imread('./flowers/'+pClass+'/'+pic)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      img = img.reshape((1,) + img.shape)
      i=0
      for batch in datagen.flow(img, batch_size=1,save_to_dir='./flowers/'+pClass+'/' ,save_prefix='ps', save_format='jpeg'):
        if i > 10:
          break
        i += 1


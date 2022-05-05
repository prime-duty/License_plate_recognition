#批量修改尺寸
import os
from PIL import Image
dir_img1="/home/duty/dissertation/train_image"
dir_img2="/home/duty/dissertation/train_label"
dir_save1="/home/duty/train_image"
dir_save2="/home/duty/train_label"
size=(512,512)

#获取目录下所有图片名
# list_temp = os.listdir(dir_img)
# list_img = list_temp[1:] #因为列表中第0项为Mac OS X操作系统所创造的隐藏文件  .DS_Store，所以从第一项开始取

#获得路径、打开要修改的图片
for i in range(500):
    # old_image1 = Image.open(dir_img1+"/%d.png" % i)
    old_image2 = Image.open(dir_img2+"/%d.png" % i)
    # save_path1 = dir_save1+("/%d.png" % i)
    save_path2 = dir_save2+("/%d.png" % i)

    #保存修改尺寸后的图片
    # old_image1.resize(size, Image.ANTIALIAS).save(save_path1)
    old_image2.resize(size, Image.ANTIALIAS).save(save_path2)
print("Done!")

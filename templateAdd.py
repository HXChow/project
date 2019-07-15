from PIL import Image
import numpy as np
import glob
import os

# 测试数据：
# distance_to_top = 315


def temp_add(path_temp, path_image, path_save, distance_to_top):

    path_file_number = glob.glob(path_image+'/*.jpg')  # 指定文件下个数
    i_num = len(path_file_number)  # 图片数量

    img_length = 640  # 窗口大小
    img_width = 392  # 窗口大小

    if os.path.exists(path_image + "/0.jpg") is True:  # 判断图片是否从"0.jpg"开始
        for i in range(i_num):
            i_temp = Image.open(path_temp)
            img = Image.open(path_image + "/" + np.str(i) + ".jpg")  # 图片固定格式：例如，"0.jpg"，"1.jpg"，…
            # img.thumbnail((img_length, img_width))  # 图片缩略（保持纵横比）
            img = img.resize((img_length, img_width))  # 适应窗口（图片有拉伸）
            i_temp.paste(img, (0, distance_to_top))
            # i_temp.show()
            i_temp.save(path_save + '/' + np.str(i) + '.jpg')
    else:
        for i in range(i_num):
            i_temp = Image.open(path_temp)
            img = Image.open(path_image + "/" + np.str(i + 1) + ".jpg")  # 图片固定格式：例如，"1.jpg"，"2.jpg"，…
            # img.thumbnail((img_length, img_width))  # 图片缩略（保持纵横比）
            img = img.resize((img_length, img_width))  # 适应窗口（图片有拉伸）
            i_temp.paste(img, (0, distance_to_top))
            # i_temp.show()
            i_temp.save(path_save + '/' + np.str(i + 1) + '.jpg')


if __name__ == '__main__':

    path_temp1 = 'F:/summerProject/temp000/t001.jpg'  # 背景模板文件  # 模板文件可选择
    # path_image1 = 'F:/summerProject/2019041'  # 视频图片文件夹1
    path_image1 = 'F:/summerProject/2019042'  # 视频图片文件夹2(测试用)
    path_save1 = 'F:/summerProject/new_temp'  # 保存的文件夹
    distance_to_top = 315  # 例如，图片或视频起始位置从离最上面315像素开始

    temp_add(path_temp1, path_image1, path_save1, distance_to_top)
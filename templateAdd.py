from PIL import Image
import numpy as np
import glob

# 测试数据：
# distance_to_top = 315


def temp_add(path_temp, path_image, path_save, distance_to_top):

    path_file_number = glob.glob(path_image+'/*.jpg')  # 指定文件下个数
    i_num = len(path_file_number)  # 图片数量

    for i in range(i_num):
        i_temp = Image.open(path_temp)
        img = Image.open(path_image + "/00" + np.str(i + 1) + ".jpg")
        # img = Image.open(path_image + "/00"+np.str(i + 1)+".jpg")
        # img.thumbnail((640, 392))  # 图片缩略（保持纵横比）
        img = img.resize((640, 392))  # 适应窗口（图片有拉伸）
        i_temp.paste(img, (0, distance_to_top))
        # i_temp.show()
        i_temp.save(path_save + '/00' + np.str(i + 1) + '.jpg')


if __name__ == '__main__':

    path_temp1 = 'F:/summerProject/temp000/t001.jpg'  # 背景模板文件  # 模板文件可选择
    path_image1 = 'F:/summerProject/2019041'  # 视频图片文件夹1
    # path_image1 = 'F:/summerProject/14back'  # 视频图片文件夹2（备选）
    path_save1 = 'F:/summerProject/new_temp'  # 保存的文件夹
    distance_to_top1 = 315  # 例如，图片或视频起始位置从离最上面315像素开始

    temp_add(path_temp1, path_image1, path_save1, distance_to_top1)

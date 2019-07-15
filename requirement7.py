import numpy as np
import cv2
import glob
import os


def delgreen(path_green, path_bg, path_save):
    """

    :param path_green: 扣绿图片路径
    :param path_bg: 背景图片路径
    :param path_save: 保存路径
    :return:
    """

    path_file_number = glob.glob(path_green+'/*.jpg')  # 指定文件下个数
    p_num = len(path_file_number)  # 图片数量

    if os.path.exists(path_green + "/0.jpg") is True:
        for k in range(p_num):
            img = cv2.imread(path_green + "/" + np.str(k) + ".jpg")  # 图片名字示例：0.jpg、1.jpg……
            img_back = cv2.imread(path_bg)

            img_back = cv2.resize(img_back, None, fx=0.7, fy=0.7)
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            rows, cols, channels = img.shape

            # 将图片转换为hsv类型
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # 获取mask
            # lower_green = np.array([35, 43, 46])  # 绿色的范围，下限
            lower_green = np.array([35, 80, 100])
            upper_green = np.array([77, 255, 255])  # 绿色的范围，上限
            mask = cv2.inRange(hsv, lower_green, upper_green)

            # height = img.shape[0]  # 长度
            # width = img.shape[1]  # 宽度
            height, width, dep = img.shape  # 获取图像的高，宽以及深度
            for i in range(height):
                for j in range(width):
                    if (img[i, j, 0] != 0) and (img[i, j, 2] != 0):
                        if ((img[i, j, 1]/img[i, j, 0]) < 1.2) or ((img[i, j, 1]/img[i, j, 2]) < 1.2):
                            mask[i, j] = 0

            # 腐蚀膨胀
            erode = cv2.erode(mask, None, iterations=1)
            dilate = cv2.dilate(erode, None, iterations=1)

            # 遍历替换
            center = [50, 50]  # 在新背景图片中的位置
            for i in range(rows):
                for j in range(cols):
                    if dilate[i, j] == 0:  # 0代表黑色的点
                        img_back[center[0]+i, center[1]+j] = img[i, j]  # 此处替换颜色，为BGR通道

            # 保存到文件夹
            cv2.imwrite(path_save + '/' + np.str(k)+'.jpg', img_back)

    else:
        for k in range(p_num):
            img = cv2.imread(path_green + "/" + np.str(k + 1) + ".jpg")  # 图片名字示例：1.jpg、2.jpg……
            img_back = cv2.imread(path_bg)

            img_back = cv2.resize(img_back, None, fx=0.7, fy=0.7)
            img = cv2.resize(img, None, fx=0.4, fy=0.4)
            rows, cols, channels = img.shape

            # 将图片转换为hsv类型
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # 获取mask
            # lower_green = np.array([35, 43, 46])  # 绿色的范围，下限
            lower_green = np.array([35, 80, 100])
            upper_green = np.array([77, 255, 255])  # 绿色的范围，上限
            mask = cv2.inRange(hsv, lower_green, upper_green)

            # height = img.shape[0]  # 长度
            # width = img.shape[1]  # 宽度
            height, width, dep = img.shape  # 获取图像的高，宽以及深度
            for i in range(height):
                for j in range(width):
                    if (img[i, j, 0] != 0) and (img[i, j, 2] != 0):
                        if ((img[i, j, 1] / img[i, j, 0]) < 1.2) or ((img[i, j, 1] / img[i, j, 2]) < 1.2):
                            mask[i, j] = 0

            # 腐蚀膨胀
            erode = cv2.erode(mask, None, iterations=1)
            dilate = cv2.dilate(erode, None, iterations=1)

            # 遍历替换
            center = [50, 50]  # 在新背景图片中的位置
            for i in range(rows):
                for j in range(cols):
                    if dilate[i, j] == 0:  # 0代表黑色的点
                        img_back[center[0] + i, center[1] + j] = img[i, j]  # 此处替换颜色，为BGR通道

            # 保存到文件夹
            cv2.imwrite(path_save + '/' + np.str(k + 1) + '.jpg', img_back)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    path_green1 = 'F:/summerProject/111111'  # 待扣绿图文件夹
    path_bg1 = 'F:/summerProject/projectCode/b001.jpg'  # 背景图文件或文件夹
    path_save1 = 'F:/summerProject/new111'  # 保存的文件夹

    delgreen(path_green1, path_bg1, path_save1)



from PIL import Image
import numpy as np
import glob


def pic_water(img_path, logo_path, save_path):  # Picture watermarking 图片加水印
    """

    :param img_path: 图片路径
    :param logo_path: 水印路径
    :param save_path: 保存路径
    :return:
    """

    path_file_number = glob.glob(img_path+'/*.jpg')  # 指定文件下个数
    p_num = len(path_file_number)  # 图片数量

    path_file_number2 = glob.glob(logo_path + '/*.png')  # 指定文件下个数
    l_num = len(path_file_number2)  # 水印数量

    if p_num <= l_num:  # 图片数量小于等于水印数量
        for i in range(p_num):
            img = Image.open(img_path+"/00"+np.str(i + 1)+".jpg")
            logo = Image.open(logo_path+"/"+np.str(i + 1)+".png")

            layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
            layer.paste(logo, (img.size[0]-logo.size[0], img.size[1]-logo.size[1]))

            img_after = Image.composite(layer, img, layer)
            # img_after.show()
            img_after.save(save_path + '/00' + np.str(i) + '.jpg')

    else:  # 图片数量大于水印数量

        p_times = p_num // l_num
        p_mob = p_num % l_num

        for j in range(p_times):
            if (j + 1) % 2 != 0:
                for k in range(l_num):
                    img = Image.open(img_path + "/00" + np.str(k + 1 + j * l_num) + ".jpg")
                    logo = Image.open(logo_path + "/" + np.str(k + 1) + ".png")

                    layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
                    layer.paste(logo, (img.size[0] - logo.size[0], img.size[1] - logo.size[1]))

                    img_after = Image.composite(layer, img, layer)
                    # img_after.show()
                    img_after.save(save_path + '/00' + np.str(k + 1 + j * l_num) + '.jpg')
            else:
                for k in range(l_num):
                    img = Image.open(img_path + "/00" + np.str(k + 1 + j * l_num) + ".jpg")
                    logo = Image.open(logo_path + "/" + np.str(l_num - k) + ".png")

                    layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
                    layer.paste(logo, (img.size[0] - logo.size[0], img.size[1] - logo.size[1]))

                    img_after = Image.composite(layer, img, layer)
                    # img_after.show()
                    img_after.save(save_path + '/00' + np.str(k + 1 + j * l_num) + '.jpg')
        for h in range(p_mob):
            img = Image.open(img_path + "/00" + np.str(h + 1 + p_times * l_num) + ".jpg")
            logo = Image.open(logo_path + "/" + np.str(h + 1) + ".png")

            layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
            layer.paste(logo, (img.size[0] - logo.size[0], img.size[1] - logo.size[1]))

            img_after = Image.composite(layer, img, layer)
            # img_after.show()
            img_after.save(save_path + '/00' + np.str(h + 1 + p_times * l_num) + '.jpg')


if __name__ == '__main__':

    img_path1 = 'F:/summerProject/14back'  # 图片文件夹
    logo_path1 = 'F:/summerProject/14simple'  # 水印文件夹
    save_path1 = 'F:/summerProject/new14simple'  # 保存的文件夹

    pic_water(img_path1, logo_path1, save_path1)

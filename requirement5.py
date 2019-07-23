from moviepy.editor import *
from natsort import natsorted
import os
import numpy as np


def vediost(file_path, save_path, name):
    """

    :param file_path: 视频文件地址
    :param save_path: 保存地址
    :param name: 视频命名
    :return:
    """
    # 定义一个数组
    list0 = []

    for root, dirs, files in os.walk(file_path):
        # 按文件名排序
        # files.sort()
        files = natsorted(files)
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp4
            if os.path.splitext(file)[1] == '.mp4':
                # 拼接成完整路径
                filePath = os.path.join(root, file)
                # 载入视频
                video = VideoFileClip(filePath)
                # 添加到数组
                list0.append(video)

    # 拼接视频
    final_clip = concatenate_videoclips(list0)

    # 生成目标视频文件
    final_clip.write_videofile(save_path + "/" + np.str(name) + ".mp4", fps=25, remove_temp=False)


if __name__ == '__main__':
    vedio_path = "F:/summerProject/usingSimple"  # 视频所在文件夹
    save_path = "F:/summerProject/newvideo"  # 视频保存文件夹
    name = "target001"  # 视频命名
    vediost(vedio_path, save_path, name)

# -*- coding: utf-8 -*-

import subprocess

def video_add(video_header, video_file, file_name, path_save):

    cmd = "ffmpeg -y -i " + video_header + " -i " + video_file + " -f mp4 -vcodec libx264 " + path_save + "/" + file_name + ".mp4"
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    video_header = 'D:/233/123.mp4' # 片头视频
    video_file = 'D:/233/456.mp4' # 视频
    path_save = 'D:/233'  # 视频保存文件夹
    file_name = 'target01'  # 视频命名

    video_add(video_header, video_file, file_name, path_save)



import subprocess
import shutil
from moviepy.editor import VideoFileClip

def video_add_mp3(file_name, mp3_file, path_save):
    clip = VideoFileClip(file_name)
    outfile_name = file_name.split('.')[0] + '-txt.mp4'
    subprocess.call('ffmpeg -y -i ' + file_name + ' -i ' + mp3_file + ' -t '+str(clip.duration)+' -strict -2 -f mp4 ' + outfile_name,shell=True)
    shutil.move(outfile_name , path_save)


if __name__ == '__main__':
    file_name = 'D:/233/test.mp4'
    mp3_file = 'D:/233/star.mp3'
    path_save = 'D:/test'
    video_add_mp3(file_name, mp3_file,path_save)


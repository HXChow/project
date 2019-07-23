import os
import os.path
import time
import shutil
import requirement2
import tkinter
import tkinter.messagebox

# path = 'C:\\Users\\73497\\Desktop\\photo'


def traverse_photo(src_dir ,number,t,dest_dir,qianzhui,mode):
    """

    :param src_dir:            #图片原路径
    :param dest_dir:            #目标保存路径
    :param qianzhui:           # 文件夹前缀
    :param number:              #照片最低数量
    :param mode:              #模式
    :return:
    """

    numz=1
    for i in range(t):
        flag=0
        dirs = os.listdir(src_dir)                       # 获取指定路径下的文件
        PhotoNumber=len(dirs)
        if(PhotoNumber>=number):
            filename=qianzhui+'-'+str(numz)
            requirement2.copy_files(dest_dir,src_dir,filename,mode)
            numz+=1
        time.sleep(1)
    # if(flag!=1):
    #     shutil.rmtree(src_dir)                         #删除文件夹内所有文件
    #     os.mkdir(src_dir)                              #删除文件夹内所有文件
    #     tkinter.messagebox.showinfo('提示', '文件夹已清空')
    return numz-1

if __name__=='__main__':
    src_dir='C:/Users/Mr.Chow/Desktop/123'
    dest_dir='C:/Users/Mr.Chow/Desktop/234'
    qianzhui='ws'
    mode='作者信息'
    traverse_photo(src_dir ,1,30,dest_dir,qianzhui,mode)
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
import requirement1
import requirement2
import requirement3
import requirement4
import requirement4_1
import requirement4_2
import requirement4_3
import requirement4_4
import requirement5
import requirement6
import requirement7
import templateAdd
import vedioAudio
import time

class R1Thread(QThread):
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal(str)
    def __init__(self,src_dir ,number,t,dest_dir,qianzhui,mode):
        super(R1Thread, self).__init__()
        self.src_dir = src_dir
        self.number = number
        self.t = t
        self.dest_dir = dest_dir
        self.qianzhui = qianzhui
        self.mode = mode

    def run(self):
        time_star = time.time()
        s = str(requirement1.traverse_photo(self.src_dir, self.number, self.t, self.dest_dir, self.qianzhui, self.mode))
        time_stop = time.time()
        total_time = str("耗时{:.2f} s".format(time_stop - time_star))
        # print(s)
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3[str].emit(s)

class R2Thread(QThread):
    _signal2 = pyqtSignal(str)
    def __init__(self, dest_dir,  file_path, filename):
        super(R2Thread,self).__init__()
        self.dest_dir = dest_dir
        self.file_path = file_path
        self.filename = filename

    def run(self):
        time_star = time.time()
        requirement2.copy_files(self.dest_dir, self.file_path, self.filename)
        time_stop = time.time()
        total_time = str("耗时{:.2f} s".format(time_stop - time_star))
        self._signal2[str].emit(total_time)

class R3Thread(QThread):    #排序
    _signal = pyqtSignal()
    def __init__(self, filename, mode):
        super(R3Thread, self).__init__()
        self.filename = filename
        self.mode = mode

    def run(self):
        requirement3.rename(self.filename, self.mode)
        self._signal.emit()

class R4Thread(QThread):   #对比度，亮度，饱和度调整确定
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()

    def __init__(self, image_path, a, g, p):
        super(R4Thread, self).__init__()
        self.image_path = image_path
        self.a = a
        self.g = g
        self.p = p

    def run(self):
        time_star = time.time()
        requirement4_2.picsave(self.image_path, self.a, self.g, self.p)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()

class R5Thread(QThread):  #视频合成
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()
    _signal4 = pyqtSignal()

    def __init__(self,im_dir,save_dir,VideoName,fps,num):
        super(R5Thread, self).__init__()
        self.im_dir = im_dir
        self.save_dir = save_dir
        self.VideoName = VideoName
        self.fps = fps
        self.num = num

    def run(self):
        time_star = time.time()
        requirement4.CompositeVideo(self.im_dir,self.save_dir,self.VideoName,self.fps,self.num)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()
        self._signal4.emit()


class R6Thread(QThread):   #拼接
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()
    _signal4 = pyqtSignal()

    def __init__(self,file_path, save_path, name):
        super(R6Thread, self).__init__()
        self.file_path = file_path
        self.save_path = save_path
        self.name = name

    def run(self):
        time_star = time.time()
        requirement5.vediost(self.file_path, self.save_path, self.name)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()
        self._signal4.emit()

class R7Thread(QThread):
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)

    def __init__(self, img_path, save_path):
        super(R7Thread, self).__init__()
        self.img_path = img_path
        self.save_path = save_path

    def run(self):
        time_star = time.time()
        requirement4_3.warpaffine(self.img_path, self.save_path)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)

class R8Thread(QThread):     #图片裁剪
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()

    def __init__(self, file_path, save_path):
        super(R8Thread, self).__init__()
        self.file_path = file_path
        self.save_path = save_path

    def run(self):
        time_star = time.time()
        requirement4_4.main(self.file_path, self.save_path)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()

class R9Thread(QThread):    #图片扣绿
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()

    def __init__(self, path_green, path_bg, path_save):
        super(R9Thread, self).__init__()
        self.path_green = path_green
        self.path_bg = path_bg
        self.path_save = path_save

    def run(self):
        time_star = time.time()
        requirement7.delgreen(self.path_green, self.path_bg, self.path_save)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()


class R10Thread(QThread):    #滤镜应用全部
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()

    def __init__(self, image_path, tag):
        super(R10Thread, self).__init__()
        self.img_path = image_path
        self.tag=tag

    def run(self):
        time_star = time.time()
        requirement4_1.picsave( self.img_path,self.tag)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()


class R11Thread(QThread):    #加水印
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()

    def __init__(self, img_path, logo_path, save_path):
        super(R11Thread, self).__init__()
        self.img_path = img_path
        self.logo_path = logo_path
        self.save_path = save_path

    def run(self):
        time_star = time.time()
        requirement6.pic_water(self.img_path, self.logo_path, self.save_path)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()

class R12Thread(QThread):    #加模板
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)
    _signal3 = pyqtSignal()

    def __init__(self, path_temp, path_image, path_save, distance_to_top):
        super(R12Thread, self).__init__()
        self.path_temp = path_temp
        self.path_image = path_image
        self.path_save = path_save
        self.distance_to_top = distance_to_top

    def run(self):
        time_star = time.time()
        templateAdd.temp_add(self.path_temp, self.path_image, self.path_save, self.distance_to_top)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)
        self._signal3.emit()

class R13Thread(QThread):    #加音频
    _signal = pyqtSignal()
    _signal2 = pyqtSignal(str)

    def __init__(self, file_name, mp3_file, path_save):
        super(R13Thread, self).__init__()
        self.file_name = file_name
        self.mp3_file = mp3_file
        self.path_save = path_save

    def run(self):
        time_star = time.time()
        vedioAudio.video_add_mp3(self.file_name, self.mp3_file, self.path_save)
        time_stop = time.time()
        total_time = str("总耗时{:.2f} s".format(time_stop - time_star))
        self._signal.emit()
        self._signal2[str].emit(total_time)

















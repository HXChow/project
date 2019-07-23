# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap,QImage
from MainUI import Ui_MainWindow
import os
import sys
import cv2
import time
import Thread
import shutil
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


class  MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        #禁止主窗口最大化及拉伸
        self.setFixedSize(self.width(), self.height())

        # 让图片或视频自适应label大小
        self.label_15.setScaledContents(True)
        self.label_19.setScaledContents(True)
        self.label_22.setScaledContents(True)
        self.label_43.setScaledContents(True)
        self.label_44.setScaledContents(True)

        # 设置计数器上下限
        self.spinBox.setRange(0, 1000)
        self.spinBox_2.setRange(1, 9999)
        self.spinBox_3.setRange(0, 20)
        self.spinBox_4.setRange(0, 100)
        self.spinBox_5.setRange(12, 24)
        self.spinBox_6.setRange(1, 5)
        self.spinBox_7.setRange(0, 50)

        #lineEdit框初始值
        self.lineEdit_4.setText(str(0))
        self.lineEdit_5.setText(str(1))
        self.lineEdit_11.setText(str(10))
        self.lineEdit_12.setText(str(30))
        self.lineEdit_13.setText(str(12))
        self.lineEdit_14.setText(str(1))
        self.lineEdit_23.setText(str(50))

        #spinBox 初始值
        self.spinBox_2.setValue(1)
        self.spinBox_3.setValue(10)
        self.spinBox_4.setValue(30)
        self.spinBox_7.setValue(50)

        # QApplication.setStyle(QStyleFactory.create('cleanlooks'))

        #视频播放区
        # self.player = QMediaPlayer()
        # self.player.setVideoOutput(self.widget)  # 视频播放输出的widget
        # self.btn_open.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        # self.btn_play.clicked.connect(self.playVideo)  # play
        # self.btn_stop.clicked.connect(self.pauseVideo)  # pause
        # self.player.positionChanged.connect(self.changeSlide)  # change Slide

        # self.btn_open.clicked.connect(self.openVideoFile)

        #信号区（已按界面按钮顺序排版）
        # tab 1(初步处理）
        self.spinBox.valueChanged.connect(self.Valuechange)
        self.spinBox_2.valueChanged.connect(self.Valuechange_2)
        self.SelectFileBtn.clicked.connect(self.slot_btn_chooseDir)
        self.SelectSaveAdressBtn.clicked.connect(self.slot_btn_choosesave)
        self.NameBtn.clicked.connect(self.selectName)
        self.SelectTypeBtn.clicked.connect(self.selectStyle)
        self.ConfirmBtn.clicked.connect(self.Confirm)
        # self.SaveFileBtn.clicked.connect(self.slot_btn_chooseMutiFile)
        # self.SelectFileBtn_2.clicked.connect(self.slot_btn_chooseDir_2)
        # self.ConfirmBtn_2.clicked.connect(self.Confirm_2)

        # tab 2（图像处理①）
        #self.SelectPhoto.clicked.connect(self.OpenImage)
        self.SelectFileBtn_3.clicked.connect(self.slot_btn_chooseDir_3)

        self.AdjustBtn.clicked.connect(self.Process)
        self.spinBox_3.valueChanged.connect(self.Valuechange_3)
        self.spinBox_4.valueChanged.connect(self.Valuechange_4)
        self.spinBox_7.valueChanged.connect(self.Valuechange_7)
        self.ConfirmBtn_8.clicked.connect(self.Confirm_3_1)

        self.radioButton.clicked.connect(self.Filter_1)
        self.radioButton_2.clicked.connect(self.Filter_2)
        self.radioButton_3.clicked.connect(self.Filter_3)
        self.radioButton_4.clicked.connect(self.Filter_4)
        self.radioButton_5.clicked.connect(self.Filter_5)
        self.radioButton_6.clicked.connect(self.Filter_6)
        self.radioButton_7.clicked.connect(self.Filter_7)
        self.radioButton_8.clicked.connect(self.Filter_8)
        self.ConfirmBtn_4.clicked.connect(self.Confirm_3)

        # tab 3（图像处理②）
        self.SelectFileBtn_5.clicked.connect(self.slot_btn_chooseDir_5)
        self.SelectSaveAdressBtn_4.clicked.connect(self.slot_btn_choosesave_3)
        self.ConfirmBtn_9.clicked.connect(self.Process_2)

        self.SelectPhoto_6.clicked.connect(self.slot_btn_chooseFile_3)
        self.SelectSaveAdressBtn_5.clicked.connect(self.slot_btn_choosesave_4)
        self.ConfirmBtn_10.clicked.connect(self.Process_3)

        self.SelectPhoto_3.clicked.connect(self.slot_btn_chooseFile)
        self.SelectPhoto_4.clicked.connect(self.slot_btn_chooseFile_2)
        self.SelectSaveAdressBtn_6.clicked.connect(self.slot_btn_choosesave_5)
        self.ConfirmBtn_5.clicked.connect(self.Process_4)

        #tab 4（图像处理③）
        self.SelectFileBtn_7.clicked.connect(self.slot_btn_chooseDir_7)
        self.SelectSaveAdressBtn_7.clicked.connect(self.slot_btn_choosesave_6)
        self.SelectLogo.clicked.connect(self.slot_btn_chooseDir_8)
        self.ConfirmBtn_6.clicked.connect(self.Confirm_6)

        self.SelectFileBtn_8.clicked.connect(self.slot_btn_chooseDir_9)
        self.SelectSaveAdressBtn_8.clicked.connect(self.slot_btn_choosesave_8)
        self.SelectTemp.clicked.connect(self.slot_btn_chooseFile_4)
        self.ConfirmBtn_11.clicked.connect(self.Confirm_7)

        # tab 5（视频合成）
        self.SelectFileBtn_4.clicked.connect(self.slot_btn_chooseDir_4)
        self.SelectSaveAdressBtn_3.clicked.connect(self.slot_btn_choosesave_2)
        self.NameBtn_2.clicked.connect(self.selectName_2)

        self.spinBox_5.valueChanged.connect(self.Valuechange_5)
        self.spinBox_6.valueChanged.connect(self.Valuechange_6)
        self.ConfirmBtn_7.clicked.connect(self.Confirm_4)

        #tab 6（后期处理）
        self.SelectFileBtn_6.clicked.connect(self.slot_btn_chooseDir_6)
        self.SelectSaveAdressBtn_2.clicked.connect(self.slot_btn_choosesave_7)
        self.SelectViedo.clicked.connect(self.slot_btn_chosseFile_3)
        self.NameBtn_3.clicked.connect(self.selectName_3)
        self.CombineBtn.clicked.connect(self.Confirm_5)

        self.SelectFileBtn_9.clicked.connect(self.slot_btn_chooseFile_5)
        self.SelectFileBtn_10.clicked.connect(self.slot_btn_chooseFile_6)
        self.SelectSaveAdressBtn_9.clicked.connect(self.slot_btn_choosesave_9)
        self.ConfirmBtn_12.clicked.connect(self.Confirm_8)

    #槽函数区
    #播放视频
    # def openVideoFile(self):
    #     self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
    #     self.player.play()  # 播放视频
    #
    # def playVideo(self):
    #     self.player.play()
    #
    # def pauseVideo(self):
    #     self.player.pause()
    #
    # def changeSlide(self, position):
    #     self.vidoeLength = self.player.duration() + 0.1
    #     self.sld_video.setValue(round((position / self.vidoeLength) * 100))
    #     self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')

    # def openVideoFile(self):
    #     global videoName  # 在这里设置全局变量以便在线程中使用
    #     videoName, videoType = QFileDialog.getOpenFileName(self,  # 返回路径下视频的全名称
    #                                                        "打开视频", os.getcwd(),
    #                                                        # "",
    #                                                        " *.mp4;;*.avi;;All Files (*)")
    #     t =R14Thread(self)
    #     t.changePixmap.connect(self.setImage)
    #     t.start()
    #
    # def setImage(self, image):
    #     self.label_43.setPixmap(QPixmap.fromImage(image))


#初步处理
    def Valuechange(self):  #输入阈值
        self.lineEdit_4.setText(str(self.spinBox.value()))

    def Valuechange_2(self):    #输入刷新时间
        self.lineEdit_5.setText(str(self.spinBox_2.value()))

    def slot_btn_chooseDir(self):   #选择文件夹
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            #print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit.setText(dir_choose)

            # self.SelectFileBtn.setEnabled(False)
            # self.t = Thread.R1Thread(dir_choose, self.spinBox.value(), self.spinBox_2.value())
            # self.t.Daemon = True
            # self.t._signal.connect(self.set_btn)
            # self.t.start()
        #requirement1.traverse_photo(dir_choose, self.spinBox.value(), self.spinBox_2.value())

    # def set_btn(self):
    #     self.SelectFileBtn.setEnabled(True)

    # def slot_btn_chooseMutiFile(self):
    #     dir_files, ok = QFileDialog.getOpenFileNames(None,
    #                                                  "多文件选择", os.getcwd(),"All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")
    #     #print(ok)
    #     if ok and len(dir_files) == 0:
    #         #print("\n取消选择")
    #         return
    #     if (len(dir_files) != 0):
    #         self.lineEdit_3.setText(' '.join(dir_files))

    def slot_btn_choosesave(self):  #选择保存的文件夹
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            #print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_2.setText(dir_save)

    def selectName(self):   #输入前缀
        name,ok = QInputDialog.getText(self, "输入前缀", "输入前缀名称:",
                                        QLineEdit.Normal)
        if name == "":
            #print("\n取消命名")
            return
        if ok and (len(name) != 0):
            self.lineEdit_8.setText(name)

    def selectStyle(self):  #选择排序方式
        list = ["品牌", "拍摄时间", "作者信息", "系统排序"]
        style, ok = QInputDialog.getItem(self, "排序方式", "请选择照片排序方式", list)
        if style == "":
            # print("\n取消选择")
            return
        if ok:
            self.lineEdit_7.setText(style)

    # 初步处理确认按钮
    def Confirm(self):
        # dest_dir=self.lineEdit_2.text()
        # file_path=self.lineEdit_3.text()
        # file_path=file_path.split(" ")              #str 转 list
        # filename=self.lineEdit_8.text()
        #requirement2.copy_files( dest_dir,  file_path, filename)
        # self.t1 = Thread.R2Thread(dest_dir, file_path, filename)
        # self.t1.Daemon = True
        # self.t1._signal2[str].connect(self.Event)
        # self.t1.start()
        self.ConfirmBtn.setEnabled(False)
        number = self.spinBox.value()
        t = self.spinBox_2.value()
        src_dir = self.lineEdit.text()
        dest_dir = self.lineEdit_2.text()
        qianzhui = self.lineEdit_8.text()
        mode = self.lineEdit_7.text()
        # requirement1.traverse_photo(src_dir ,number,t,dest_dir,qianzhui,mode)
        self.t = Thread.R1Thread(src_dir ,number,t, dest_dir, qianzhui, mode)
        self.t.Daemon = True
        self.t._signal.connect(self.set_btn)
        self.t._signal2[str].connect(self.Event)
        self.t._signal3[str].connect(self.Return)
        self.t.start()

    def set_btn(self):    #按钮阻塞，下同
        self.ConfirmBtn.setEnabled(True)

    def Return(self,s):  #返回最新的地址
        dest_dir = self.lineEdit_2.text()
        name = self.lineEdit_8.text()
        last_dir = dest_dir + "/" + name + "-" + s
        last_name = name + "-" + s
        save_dir = dest_dir + "/" + last_name
        self.lineEdit_6.setText(last_name)
        self.lineEdit_3.setText(last_dir)
        self.lineEdit_9.setText(last_dir)
        self.lineEdit_15.setText(last_dir)
        self.lineEdit_17.setText(last_dir)
        self.lineEdit_19.setText(last_dir)
        self.lineEdit_21.setText(dest_dir)
        self.lineEdit_22.setText(dest_dir)
        self.lineEdit_24.setText(last_dir)
        self.lineEdit_25.setText(save_dir)
        self.lineEdit_27.setText(save_dir)
        self.lineEdit_28.setText(save_dir)
        self.lineEdit_29.setText(last_dir)
        self.lineEdit_30.setText(save_dir)
        self.lineEdit_32.setText(save_dir)
        self.lineEdit_45.setText(last_dir)

        #print(last_dir)

    # def slot_btn_chooseDir_2(self):
    #     dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
    #     if dir_choose == "":
    #         #print("\n取消选择")
    #         return
    #     if (len(dir_choose) != 0):
    #         self.lineEdit_6.setText(dir_choose)

    # def Confirm_2(self):
    #     filename = self.lineEdit_6.text()
    #     mode = self.lineEdit_7.text()
    #     #requirement3.rename(filename, mode)
    #     self.t2 = Thread.R3Thread(filename, mode)
    #     self.t2.Daemon = True
    #     self.t2._signal.connect(self.Event_2)
    #     self.t2.start()

# 图像处理①
    def slot_btn_chooseDir_3(self):     #选择图片文件夹
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            #print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_15.setText(dir_choose)

    def OpenImage(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                       "打开图片",os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        jpg = QPixmap(imgName)
        self.label_15.setPixmap(jpg)
        if imgName == "":
            #print("\n取消选择")
            return
        if (len(imgName)!=0):
            self.lineEdit_16.setText(imgName)
            #print(imgName)

    def filename(self):                  #获取文件夹下第一张照片地址
        return os.path.join(self.lineEdit_15.text(),os.listdir(self.lineEdit_15.text())[0])

    def filename_2(self):
        return os.path.join(self.lineEdit_30.text(), os.listdir(self.lineEdit_30.text())[0])

    def filename_3(self):
        return os.path.join(self.lineEdit_32.text(), os.listdir(self.lineEdit_32.text())[0])

    def fliename_4(self):
        return os.path.join(self.lineEdit_28.text(), os.listdir(self.lineEdit_28.text())[0])

    #调整锐度、饱和度、对比度按钮
    def Process(self):
        img_dir = self.filename()
        requirement4_2.picshow(img_dir)

    #输入对比度，亮度，锐度
    def Valuechange_3(self): #对比度
        self.lineEdit_11.setText(str(self.spinBox_3.value()))

    def Valuechange_4(self): #亮度
        self.lineEdit_12.setText(str(self.spinBox_4.value()))

    def Valuechange_7(self):    #饱和度
        self.lineEdit_23.setText(str(self.spinBox_7.value()))

    # 对比度、亮度、饱和度应用到全部确认按钮
    def Confirm_3_1(self):
        self.ConfirmBtn_8.setEnabled(False)
        image_path = self.lineEdit_15.text()
        a = self.spinBox_3.value()
        g = self.spinBox_4.value()
        p = self.spinBox_7.value()
        # requirement4_2.picsave(image_path, a, g, p)
        self.t3 = Thread.R4Thread(image_path, a, g, p)
        self.t3.Daemon = True
        self.t3._signal.connect(self.set_btn_7)
        self.t3._signal2[str].connect(self.Event)
        self.t3._signal3.connect(self.Update)
        self.t3.start()

    def set_btn_7(self):
            self.ConfirmBtn_8.setEnabled(True)

    #滤镜按钮
    def Filter_1(self): #黑白
        requirement4_1.picshow(self.filename(),1)

    def Filter_2(self): #冷色
        requirement4_1.picshow(self.filename(), 2)

    def Filter_3(self): #怀旧
        requirement4_1.picshow(self.filename(), 3)

    def Filter_4(self): #暖色
        requirement4_1.picshow(self.filename(), 4)

    def Filter_5(self): #清新
        requirement4_1.picshow(self.filename(), 5)

    def Filter_6(self): #轮廓
        requirement4_1.picshow(self.filename(), 6)

    def Filter_7(self): #边界
        requirement4_1.picshow(self.filename(), 7)

    def Filter_8(self): #浮雕
        requirement4_1.picshow(self.filename(), 8)

    #滤镜应用到全部按钮
    def Confirm_3(self):
        #image_path = self.filename()
        image_path = self.lineEdit_15.text()
        if self.radioButton.isChecked():        #isChecked()返回单选按钮的状态，返回值True或False
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 1)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_2.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 2)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_3.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 3)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_4.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 4)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_5.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 5)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_6.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 6)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_7.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 7)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()
        if self.radioButton_8.isChecked():
            self.ConfirmBtn_4.setEnabled(False)
            self.t10 = Thread.R10Thread(image_path, 8)
            self.t10.Daemon = True
            self.t10._signal.connect(self.set_btn_8)
            self.t10._signal2[str].connect(self.Event)
            self.t10._signal3.connect(self.Update)
            self.t10.start()

    def set_btn_8(self):
        self.ConfirmBtn_4.setEnabled(True)

    def Update(self):      #预览处理好的图片
        #display = self.lineEdit_16.text()
        display = self.filename()
        jpg = QPixmap(display)
        self.label_15.setPixmap(jpg)

# 图像处理②
    def slot_btn_chooseFile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_choose == "":
            # print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_17.setText(dir_choose)

    def slot_btn_chooseFile_2(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                           "选择图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")

        jpg = QPixmap(imgName)
        self.label_22.setPixmap(jpg)
        if imgName == "":
                #print("\n取消选择")
                return
        if (len(imgName) != 0):
                self.lineEdit_18.setText(str(imgName))

    def slot_btn_chooseDir_5(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_choose == "":
            #print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_24.setText(dir_choose)

    def slot_btn_choosesave_3(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            #print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_25.setText(dir_save)

    def slot_btn_chooseFile_3(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                           "打开图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        jpg = QPixmap(imgName)
        self.label_22.setPixmap(jpg)

        if imgName == "":
                #print("\n取消选择")
                return
        if (len(imgName) != 0):
                self.lineEdit_26.setText(imgName)

    def Update_2(self):
        display = self.lineEdit_26.text()
        (display, tempfilename) = os.path.split(display)
        show = self.lineEdit_27.text() + "/" + tempfilename
        jpg = QPixmap(show)
        self.label_22.setPixmap(jpg)


    def slot_btn_choosesave_4(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            #print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_27.setText(dir_save)

    def slot_btn_choosesave_5(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            # print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_28.setText(dir_save)

    #防抖处理
    def  Process_2(self):
        self.ConfirmBtn_9.setEnabled(False)
        img_path = self.lineEdit_24.text()
        save_path = self.lineEdit_25.text()
        #requirement4_3.warpaffine(img_path, save_path)
        self.t7 = Thread.R7Thread(img_path, save_path)
        self.t7.Daemon = True
        self.t7._signal.connect(self.set_btn_4)
        self.t7._signal2[str].connect(self.Event)
        self.t7.start()

    def set_btn_4(self):
        self.ConfirmBtn_9.setEnabled(True)

    #图片裁剪
    def Process_3(self):
        self.ConfirmBtn_10.setEnabled(False)
        file_path = self.lineEdit_26.text()
        save_path = self.lineEdit_27.text()
        #requirement4_4.main(file_path, save_path)
        self.t8 = Thread.R8Thread(file_path, save_path)
        self.t8.Daemon = True
        self.t8._signal.connect(self.set_btn_5)
        self.t8._signal2[str].connect(self.Event)
        self.t8._signal3.connect(self.Update_2)
        self.t8.start()

    def set_btn_5(self):
        self.ConfirmBtn_10.setEnabled(True)

    #图片扣绿
    def Process_4(self):
        self.ConfirmBtn_5.setEnabled(False)
        path_green = self.lineEdit_17.text()
        path_bg = self.lineEdit_18.text()
        path_save = self.lineEdit_28.text()
        #requirement7.delgreen(path_green, path_bg, path_save)
        self.t9 = Thread.R9Thread(path_green, path_bg, path_save)
        self.t9.Daemon = True
        self.t9._signal.connect(self.set_btn_6)
        self.t9._signal2[str].connect(self.Event)
        self.t9._signal3.connect(self.Update_4)
        self.t9.start()

    def set_btn_6(self):
        self.ConfirmBtn_5.setEnabled(True)

    def Update_4(self):
        # save = self.lineEdit_28.text()
        # display = save + "/" + str(0) + ".jpg"
        display = self.fliename_4()
        jpg = QPixmap(display)
        self.label_22.setPixmap(jpg)

# 图像处理③
    # 加水印
    def slot_btn_chooseDir_7(self, dir_choose):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            # print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_19.setText(dir_choose)

    def slot_btn_chooseDir_8(self, dir_choose):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            # print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_20.setText(dir_choose)

    def slot_btn_choosesave_6(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            # print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_30.setText(dir_save)

    # 加模板
    def slot_btn_chooseDir_9(self, dir_choose):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            # print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_29.setText(dir_choose)

    def slot_btn_chooseFile_4(self):
        imgName, imgType = QFileDialog.getOpenFileName(None,
                                                       "选择图片", os.getcwd(), "", "*.jpg;;*.png;;All Files(*)")
        jpg = QPixmap(imgName)
        self.label_19.setPixmap(jpg)
        if imgName == "":
            # print("\n取消选择")
            return
        if (len(imgName) != 0):
            self.lineEdit_31.setText(str(imgName))

    def slot_btn_choosesave_8(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            # print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_32.setText(dir_save)

    # 加水印确认
    def Confirm_6(self):
        self.ConfirmBtn_6.setEnabled(False)
        img_path = self.lineEdit_19.text()
        logo_path = self.lineEdit_20.text()
        save_path = self.lineEdit_30.text()
        # requirement6.pic_water(img_path, logo_path, save_path)
        self.t11 = Thread.R11Thread(img_path, logo_path, save_path)
        self.t11.Daemon = True
        self.t11._signal.connect(self.set_btn_9)
        self.t11._signal2[str].connect(self.Event)
        self.t11._signal3.connect(self.Update_5)
        self.t11.start()

    def set_btn_9(self):
        self.ConfirmBtn_6.setEnabled(True)

    def Update_5(self):
        display = self.filename_2()
        jpg = QPixmap(display)
        self.label_19.setPixmap(jpg)

    # 加模板确认
    def Confirm_7(self):
        self.ConfirmBtn_11.setEnabled(False)
        path_temp = self.lineEdit_31.text()
        path_image = self.lineEdit_29.text()
        path_save = self.lineEdit_32.text()
        distance_to_top = 315
        # templateAdd.temp_add(path_temp, path_image, path_save, distance_to_top)
        self.t12 = Thread.R12Thread(path_temp, path_image, path_save, distance_to_top)
        self.t12.Daemon = True
        self.t12._signal.connect(self.set_btn_10)
        self.t12._signal2[str].connect(self.Event)
        self.t12._signal3.connect(self.Update_6)
        self.t12.start()

    def set_btn_10(self):
        self.ConfirmBtn_11.setEnabled(True)

    def Update_6(self):
        display =self.filename_3()
        jpg = QPixmap(display)
        self.label_19.setPixmap(jpg)

# 视频合成
    def slot_btn_chooseDir_4(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_choose == "":
            #print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_9.setText(dir_choose)

    def selectName_2(self):
        name, ok = QInputDialog.getText(self, "输入名称", "输入视频名称:",
                                        QLineEdit.Normal)
        if ok and (len(name) != 0):
            self.lineEdit_10.setText(name)

    def slot_btn_choosesave_2(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            #print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_45.setText(dir_save)

    def Valuechange_5(self, value):
        self.lineEdit_13.setText(str(self.spinBox_5.value()))

    def Valuechange_6(self, value):
        self.lineEdit_14.setText(str(self.spinBox_6.value()))

    #合成视频确认
    def Confirm_4(self):
        self.ConfirmBtn_7.setEnabled(False)
        im_dir=self.lineEdit_9.text()
        save_dir = self.lineEdit_45.text()
        VideoName = self.lineEdit_10.text()
        fps = self.spinBox_5.value()
        num = self.spinBox_6.value()
        #requirement4.CompositeVideo(im_dir, save_dir, VideoName, fps, num)
        self.t5 = Thread.R5Thread(im_dir, save_dir, VideoName, fps, num)
        self.t5.Daemon = True
        self.t5._signal.connect(self.set_btn_2)
        self.t5._signal2[str].connect(self.Event)
        self.t5._signal3.connect(self.Update_3)
        self.t5._signal4.connect(self.Return_2)
        self.t5.start()

    def Return_2(self):
        save = self.lineEdit_45.text()
        self.lineEdit_22.setText(save)
        self.lineEdit_21.setText(save)

    def set_btn_2(self):
        self.ConfirmBtn_7.setEnabled(True)

    def Update_3(self):  #在label播放视频
        global videoName
        save = self.lineEdit_45.text()
        name = self.lineEdit_10.text()
        videoName = save + "/" + name + ".mp4"
        self.t = R14Thread(self)
        self.t.changePixmap.connect(self.setImage_2)
        self.t.start()

    def setImage_2(self, image):
        self.label_43.setPixmap(QPixmap.fromImage(image))

        # display = PyQt5.QtCore.QUrl("file:///" + save + "/" + name + ".mp4")
        # self.player.setMedia(QMediaContent(display))
        # self.player.play()

    #后期处理
    #拼接
    def slot_btn_chooseDir_6(self, dir_choose):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if dir_choose == "":
            #print("\n取消选择")
            return
        if (len(dir_choose) != 0):
            self.lineEdit_22.setText(dir_choose)

    def slot_btn_choosesave_7(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            # print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_21.setText(dir_save)

    def slot_btn_chosseFile_3(self):
        global videoName  # 在这里设置全局变量以便在线程中使用
        videoName, videoType = QFileDialog.getOpenFileName(self,  # 返回路径下视频的全名称
                                                           "打开视频", os.getcwd(),
                                                           # "",
                                                           " *.mp4;;*.avi;;All Files (*)")
        if videoName == "":
            return
        if (len(videoName) != 0):
            self.lineEdit_16.setText(videoName)
        copy_dir = self.lineEdit_22.text()
        shutil.copy(videoName, copy_dir)
        t = R14Thread(self)
        t.changePixmap.connect(self.setImage)
        t.start()

    def setImage(self, image):
        self.label_44.setPixmap(QPixmap.fromImage(image))

    def selectName_3(self):
        name, ok = QInputDialog.getText(self, "输入名称", "输入视频名称:",
                                        QLineEdit.Normal)
        if ok and (len(name) != 0):
            self.lineEdit_33.setText(name)

    #加音频
    def slot_btn_chooseFile_5(self):
        Vedio,VedioType = QFileDialog.getOpenFileName(None,
                                                       "选择视频", os.getcwd(),"*.mp4")

        if Vedio == "":
            # print("\n取消选择")
            return
        if (len(Vedio) != 0):
            self.lineEdit_34.setText(str(Vedio))

    def slot_btn_chooseFile_6(self):
        Audio, AudioType = QFileDialog.getOpenFileName(None,
                                                       "选择视频", os.getcwd(), "*.mp3")

        if Audio == "":
            # print("\n取消选择")
            return
        if (len(Audio) != 0):
            self.lineEdit_35.setText(str(Audio))

    def slot_btn_choosesave_9(self):
        dir_save = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if dir_save == "":
            # print("\n取消选择")
            return
        if (len(dir_save) != 0):
            self.lineEdit_36.setText(dir_save)

    # 拼接确认
    def Confirm_5(self):
        self.CombineBtn.setEnabled(False)
        file_path = self.lineEdit_22.text()
        save_path = self.lineEdit_21.text()
        name = self.lineEdit_33.text()
        #requirement5.vediost(file_path, save_path, name)
        self.t6 = Thread.R6Thread(file_path, save_path, name)
        self.t6.Daemon = True
        self.t6._signal.connect(self.set_btn_3)
        self.t6._signal2[str].connect(self.Event)
        self.t6._signal3.connect(self.Update_7)
        self.t6._signal4.connect(self.Return_3)
        self.t6.start()

    def Return_3(self):
        save = self.lineEdit_21.text()
        name = self.lineEdit_33.text()
        save2 = self.lineEdit_2.text()
        video_dir = save + "/" + name + ".mp4"
        self.lineEdit_34.setText(video_dir)
        self.lineEdit_36.setText(save2)

    def set_btn_3(self):
        self.CombineBtn.setEnabled(True)

    def Update_7(self):
        global videoName
        save = self.lineEdit_21.text()
        name = self.lineEdit_33.text()
        videoName = save + "/" + name + ".mp4"
        self.t = R14Thread(self)
        self.t.changePixmap.connect(self.setImage)
        self.t.start()

    #加音频确认
    def Confirm_8(self):
        self.ConfirmBtn_12.setEnabled(False)
        file_name = self.lineEdit_34.text()
        mp3_file = self.lineEdit_35.text()
        path_save = self.lineEdit_36.text()
        #vedioAudio.video_add_mp3(file_name, mp3_file, path_save)
        self.t13 = Thread.R13Thread(file_name, mp3_file, path_save)
        self.t13.Daemon = True
        self.t13._signal.connect(self.set_btn_11)
        self.t13._signal2[str].connect(self.Event)
        self.t13.start()

    def set_btn_11(self):
        self.ConfirmBtn_12.setEnabled(True)


    #弹窗事件（显示已完成和运行时间）
    def Event(self, total_time):
        reply = QMessageBox.information(self,"提示",
                                        "已完成，" + total_time,
                                        QMessageBox.Yes)


class R14Thread(QThread):  # 采用线程来播放视频

    changePixmap = pyqtSignal(QtGui.QImage)

    def run(self):
        cap = cv2.VideoCapture(videoName)
        while (cap.isOpened() == True):
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                                 QImage.Format_RGB32)  # 在这里可以对每帧图像进行处理，
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                time.sleep(0.05)  # 控制视频播放的速度
            else:
                break

# class myVideoWidget(QVideoWidget):
#     def __init__(self,parent=None):
#         super(QVideoWidget,self).__init__(parent)

if __name__ == '__main__':
    s = '2019-07-26 01:00:00'
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if s > now():
        app = QApplication(sys.argv)
        myWin = MyMainWindow()
        myWin.show()
        sys.exit(app.exec_())
    else:
        sys.exit()



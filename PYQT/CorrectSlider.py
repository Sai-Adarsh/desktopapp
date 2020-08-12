import sys
import json
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider,QPushButton,QLabel,QMessageBox
from mba_data_access import returnImg

image1="tile_500um.png"

class MainWindow():
    def __init__(self):
        self.app=QtWidgets.QApplication(sys.argv)
        self.window=QtWidgets.QMainWindow()
        self.imagepath="tile_500um.png"
        self.imagepath2="samples/test.png"
        self.initGui()
        self.window.setWindowTitle("Crowd Cell")
        self.window.setGeometry(500,200,500,550)
        self.window.setStyleSheet("border:3px solid #4e4e4e; background-color:#FFFFFF")
        self.window.show()
        sys.exit(self.app.exec_())
    def initGui(self):
        self.applyBtn=QtWidgets.QPushButton("Left",self.window)
        self.applyBtn.setGeometry(280,370,120,30)
        self.applyBtn.setStyleSheet("background-color:#4e4e4e;color:#f7f7f7")
        self.applyBtn.clicked.connect(self.on_lftclick)
       

        self.rightBtn=QtWidgets.QPushButton("Right",self.window)
        self.rightBtn.setGeometry(100,370,120,30)
        self.rightBtn.setStyleSheet("background-color:#4e4e4e;color:#ffffff")
        self.rightBtn.clicked.connect(self.on_click)

        self.l1=QtWidgets.QLabel("ThresHold :",self.window)
        self.l1.setGeometry(200,420,120,30)
        self.l1.setStyleSheet("background-color:#ffffff;color:#4e4e4e;border :0px solid")
        self.l1.setFont(QtGui.QFont('Times', 15))

        self.l2=QtWidgets.QLabel("0                                         100",self.window)
        self.l2.setGeometry(180,470,150,30)
        self.l2.setStyleSheet("background-color:#ffffff;color:#4e4e4e;border :0px solid")
        self.l2.setFont(QtGui.QFont('Times', 10))

        self.slider=QtWidgets.QSlider(Qt.Horizontal,self.window)
        self.slider.setGeometry(180, 450, 150, 30)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.valueChanged[int].connect(self.changeValue)

        self.l3=QtWidgets.QLabel(self.window)
        self.l3.setGeometry(250,480,20,30)
        self.l3.setStyleSheet("background-color:#ffffff;color:#4e4e4e;border :0px solid")
        self.l3.setFont(QtGui.QFont('Times', 10))
        

        #self.tslider=QtWidgets.QSlider(Qt.Horizontal,self.window)
        #self.tslider.setGeometry(60, 450, 150, 30)
        #self.tslider.setMinimum(1)
        #self.tslider.valueChanged[int].connect(self.changeValue)

        self.l4=QtWidgets.QLabel("CROWD CELL",self.window)
        self.l4.setGeometry(190,20,130,40)
        self.l4.setStyleSheet("background-color:#ffffff;color:#4e4e4e;border :0px solid")
        self.l4.setFont(QtGui.QFont('Times', 15))

   
        self.label=QtWidgets.QLabel(self.window)
        self.label.setGeometry(100,50,300,300)
        self.label.setStyleSheet("background-color:#FFFFFF")
        self.image=QtGui.QImage(self.imagepath)
        self.pixmapImage=QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmapImage)
        self.label.setScaledContents(True)
        
    #def on_submit(self):
        #self.image=QtGui.QImage(self.imagepath2)
        #self.pixmapImage=QtGui.QPixmap.fromImage(self.image)
       # self.label.setPixmap(self.pixmapImage)
          
       
    def on_lftclick(self):    
        
        self.image=QtGui.QImage(self.imagepath)
        self.pixmapImage=QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmapImage)
        
         
    
    def changeValue(self, value):
        value=value
        
        returnImg(value)
        self.image=QtGui.QImage(self.imagepath2)
        self.pixmapImage=QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmapImage)
        #size = self.slider.value()
        self.l3.setText(str(value))
        with open('samples/person.txt') as json_file:
                  data = json.load(json_file)
        #print(data)
        msg = QtWidgets.QMessageBox(self.window)
        msg.setWindowTitle("Segmented Cells")
        msg.setGeometry(700,400,800,500)
        msg.setText(str(data))
        msg.show()


    def on_click(self):
        
        self.image=QtGui.QImage(self.imagepath2)
        self.pixmapImage=QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmapImage)
       # return (image2)

   
        
main=MainWindow()
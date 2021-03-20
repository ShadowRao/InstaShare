from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qrcode
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1930, 1306)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QtCore.QRect(0, +5,1920, 1110))        
       # self.label.setPixmap(QPixmap(r"C:\Users\shadd\Downloads\Background.jpg")) 
        self.CS_label = QtWidgets.QLabel(self.centralwidget)
        self.CS_label.setGeometry(QtCore.QRect(820, 70, 356, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CS_label.setFont(font)
        self.CS_label.setObjectName("CS_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 160, 531, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Assignment_VL = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Assignment_VL.setContentsMargins(0, 0, 0, 0)
        self.Assignment_VL.setObjectName("Assignment_VL")
        self.Assignment_label = QtWidgets.QLabel(self.layoutWidget)
        self.Assignment_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Assignment_label.setObjectName("Assignment_label")
        self.Assignment_label.setStyleSheet("background-color: lightgreen") 
        self.Assignment_VL.addWidget(self.Assignment_label)
        self.Assignment_textbox = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.Assignment_textbox.setObjectName("Assignment_textbox")
        self.Assignment_VL.addWidget(self.Assignment_textbox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(610, 160, 521, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Homework_VL = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.Homework_VL.setContentsMargins(0, 0, 0, 0)
        self.Homework_VL.setObjectName("Homework_VL")
        self.Homework_Label = QtWidgets.QLabel(self.layoutWidget1)
        self.Homework_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Homework_Label.setObjectName("Homework_Label")
        self.Homework_Label.setStyleSheet("background-color: lightgreen") 
        self.Homework_VL.addWidget(self.Homework_Label)
        self.Homework_textbox = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.Homework_textbox.setObjectName("Homework_textbox")
        self.Homework_VL.addWidget(self.Homework_textbox)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(962, 840, 221, 51))
        self.SaveButton.setObjectName("SaveButton")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 560, 1071, 221))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.Notice_VL = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.Notice_VL.setContentsMargins(0, 0, 0, 0)
        self.Notice_VL.setObjectName("Notice_VL")
        self.Notice_label = QtWidgets.QLabel(self.layoutWidget2)
        self.Notice_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Notice_label.setObjectName("Notice_label")
        self.Notice_label.setStyleSheet("background-color: lightgreen")         
        self.Notice_VL.addWidget(self.Notice_label)
        self.Notice_textbox = QtWidgets.QTextEdit(self.layoutWidget2)
        self.Notice_textbox.setObjectName("Notice_textbox")
        self.Notice_VL.addWidget(self.Notice_textbox)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(1240, 160, 621, 621))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.Notes_VL = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.Notes_VL.setContentsMargins(0, 0, 0, 0)
        self.Notes_VL.setObjectName("Notes_VL")
        self.Notes_label = QtWidgets.QLabel(self.layoutWidget3)
        self.Notes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Notes_label.setObjectName("Notes_label")
        self.Notes_label.setStyleSheet("background-color: lightgreen") 
        self.Notes_VL.addWidget(self.Notes_label)
        self.Notes_Textbox = QtWidgets.QTextEdit(self.layoutWidget3)
        self.Notes_Textbox.setObjectName("Notes_Textbox")
        self.Notes_VL.addWidget(self.Notes_Textbox)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1240, 60, 529, 24))
        self.widget.setObjectName("widget")
        self.Created_HL = QtWidgets.QHBoxLayout(self.widget)
        self.Created_HL.setContentsMargins(0, 0, 0, 0)
        self.Created_HL.setObjectName("Created_HL")
        self.CreatedDate_label = QtWidgets.QLabel(self.widget)
        self.CreatedDate_label.setObjectName("CreatedDate_label")
        self.Created_HL.addWidget(self.CreatedDate_label)
        self.Created_Line = QtWidgets.QLineEdit(self.widget)
        self.Created_Line.setObjectName("Created_Line")
        self.Created_HL.addWidget(self.Created_Line)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(1240, 110, 529, 24))
        self.widget1.setObjectName("widget1")
        self.DueDate_HL = QtWidgets.QHBoxLayout(self.widget1)
        self.DueDate_HL.setContentsMargins(0, 0, 0, 0)
        self.DueDate_HL.setObjectName("DueDate_HL")
        spacerItem = QtWidgets.QSpacerItem(23, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.DueDate_HL.addItem(spacerItem)
        self.DueDate_label = QtWidgets.QLabel(self.widget1)
        self.DueDate_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DueDate_label.setObjectName("DueDate_label")
        self.DueDate_HL.addWidget(self.DueDate_label)
        self.DueDate_Line = QtWidgets.QLineEdit(self.widget1)
        self.DueDate_Line.setObjectName("DueDate_Line")
        self.DueDate_HL.addWidget(self.DueDate_Line)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(60, 110, 491, 24))
        self.widget2.setObjectName("widget2")
        self.Subject_HL = QtWidgets.QHBoxLayout(self.widget2)
        self.Subject_HL.setContentsMargins(0, 0, 0, 0)
        self.Subject_HL.setObjectName("Subject_HL")
        self.Subject_label = QtWidgets.QLabel(self.widget2)
        self.Subject_label.setObjectName("Subject_label")
        self.Subject_HL.addWidget(self.Subject_label)
        self.Subject_line = QtWidgets.QLineEdit(self.widget2)
        self.Subject_line.setObjectName("Subject_line")
        self.Subject_HL.addWidget(self.Subject_line)
# =============================================================================
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(560, 70, 93, 28))
#         self.pushButton.setObjectName("pushButton")
# =============================================================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1930, 26))
        self.menubar.setObjectName("menubar")
        self.menuA_Section = QtWidgets.QMenu(self.menubar)
        self.menuA_Section.setObjectName("menuA_Section")
        self.menuB_Section = QtWidgets.QMenu(self.menubar)
        self.menuB_Section.setObjectName("menuB_Section")
        self.menuC_section = QtWidgets.QMenu(self.menubar)
        self.menuC_section.setObjectName("menuC_section")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAssignments = QtWidgets.QAction(MainWindow)
        self.actionAssignments.setObjectName("actionAssignments")
        self.menubar.addAction(self.menuA_Section.menuAction())
        self.menubar.addAction(self.menuB_Section.menuAction())
        self.menubar.addAction(self.menuC_section.menuAction())
        

        self.retranslateUi(MainWindow)
       # self.SaveButton.pressed.connect(self.Assignment_textbox.selectAll)
        self.SaveButton.released.connect(self.clickMethod)
    #    self.pushButton.pressed.connect(self.Assignment_textbox.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "InstaShare"))
        self.CS_label.setText(_translate("MainWindow", "Computer Science Engineering"))
        self.Assignment_label.setText(_translate("MainWindow", "Assignments"))
        self.Homework_Label.setText(_translate("MainWindow", "HomeWork"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.Notice_label.setText(_translate("MainWindow", "Important Notice"))
        self.Notes_label.setText(_translate("MainWindow", "Notes"))
        self.CreatedDate_label.setText(_translate("MainWindow", "Created Date"))
        self.DueDate_label.setText(_translate("MainWindow", "Due Date"))
        self.Subject_label.setText(_translate("MainWindow", "Subjects"))
        self.menuA_Section.setTitle(_translate("MainWindow", "A Section"))
        self.menuB_Section.setTitle(_translate("MainWindow", "B Section"))
        self.menuC_section.setTitle(_translate("MainWindow", "C section"))
        self.actionAssignments.setText(_translate("MainWindow", "Assignments"))
    


    def clickMethod(self):
        Sub1=(self.Subject_line.text())
        file1 = open("C:/Users/shadd/Documents/Subjects.txt","w+")
        file1.writelines(Sub1) 
        file1.close()
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Subjects.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Sub.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Sub.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Sub.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()
        
        Cre1=(self.Created_Line.text())
        file2=open("C:/Users/shadd/Documents/Created.txt","w+")
        file2.writelines(Cre1)
        file2.close()   
        
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Created.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Cre.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Cre.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Cre.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()        

        
        Due1=(self.DueDate_Line.text())
        file3=open("C:/Users/shadd/Documents/Due.txt","w+")
        file3.writelines(Due1)
        file3.close()
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Due.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Due.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Due.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Due.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()        
        
        Ass1=(self.Assignment_textbox.toPlainText())
        file4=open("C:/Users/shadd/Documents/Ass.txt","w+")
        file4.writelines(Ass1)      
        file4.close()
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Ass.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Ass.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Ass.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Ass.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()        
        
        Hom1=(self.Homework_textbox.toPlainText())
        file5=open("C:/Users/shadd/Documents/Hom.txt","w+")
        file5.writelines(Hom1)      
        file5.close()
        file4.close()
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Hom.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Hom.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Hom.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Hom.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()         
        
                

        Not1=(self.Notes_Textbox.toPlainText())
        file6=open("C:/Users/shadd/Documents/Notes.txt","w+")
        file6.writelines(Not1)      
        file6.close() 
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Notes.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Notes.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Hom.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Notes.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()          

        Notice1=(self.Notice_textbox.toPlainText())
        file7=open("C:/Users/shadd/Documents/Notice.txt","w+")
        file7.writelines(Notice1)      
        file7.close() 
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        with open("C:/Users/shadd/Documents/Notice.txt","r") as fie:
            file_drive = drive.CreateFile({'title' :'Notice.docx' })  
            file_drive.SetContentString(fie.read()) 
            file_drive.Upload()
        
        file_list = drive.ListFile({'q': "title contains 'Notice.docx' and trashed=false"}).GetList()
        print(file_list[0]['title']) # should be the title of the file we just created
        file_id = file_list[0]['id'] # get the file ID 
        
        folder = drive.ListFile({'q': "title = 'something' and trashed=false"}).GetList()[0] # get the folder we just created
        file = drive.CreateFile({'title': "Notice.txt", 'parents': [{'id': folder['id']}]})
        file.Upload()
        
      #  stuff= ('Subject: ' '\n'+ self.Subject_line.text()) + ('\n''Created Date: ' '\n'+ self.Created_Line.text()) + ('\n''Due Date: ' '\n'+ self.DueDate_Line.text()) + ('\n''Assignments: ' '\n'+ self.Assignment_textbox.toPlainText()) +('\n''HomeWork: ' '\n'+ self.Homework_textbox.toPlainText()) +('Notes: ' '\n'+ self.Notes_Textbox.toPlainText()) + ('\n''Important Notice: ' '\n'+self.Notice_textbox.toPlainText())   
        # print(stuff)
# =============================================================================
#         x=qrcode.make(stuff)
#         x.save("stupid1.jpg")    
# =============================================================================

       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

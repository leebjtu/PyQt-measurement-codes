from PyQt6.QtWidgets import QWidget

class QSSTool:
 @staticmethod
 def setQss2Object(qss_file_name, obj: QWidget):
     with open(qss_file_name, 'r',encoding='UTF-8') as file:
         content = file.read()
         obj.setStyleSheet(content)
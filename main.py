import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QTextStream
from MainWindowUI import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

def load_stylesheet(filename):
    """加载并返回QSS样式文件内容"""
    file = QFile(filename)
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        return stream.readAll()
    return ""

if __name__=="__main__":
    app=QApplication(sys.argv)
    # 加载并应用样式表
    stylesheet = load_stylesheet("styles.qss")
    if stylesheet:
        app.setStyleSheet(stylesheet)

    mainWindow=MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
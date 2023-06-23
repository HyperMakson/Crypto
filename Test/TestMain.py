import sys
import os
from PyQt6 import QtWidgets
import TestMaket

class ExampleApp(QtWidgets.QMainWindow, TestMaket.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)
    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

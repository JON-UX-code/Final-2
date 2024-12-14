import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

def main():
    app = QApplication(sys.argv)


    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    MainWindow.show()


    sys.exit(app.exec())

if __name__ == "__main__":
    main()
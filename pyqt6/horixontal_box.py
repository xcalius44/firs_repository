import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(60)
        self.setWindowTitle("QHBoxLayout")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        name_label = QLabel("Нове ім'я користувача")
        name_edit = QLineEdit()
        name_edit.setClearButtonEnabled(True)
        name_edit.textEdited.connect(self.checkUserInput)
        self.accept_button = QPushButton("Підтвердити")
        self.accept_button.setEnabled(False)
        self.accept_button.clicked.connect(self.close)
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(name_label)
        main_h_box.addWidget(name_edit)
        main_h_box.addWidget(self.accept_button)
        self.setLayout(main_h_box)

    def checkUserInput(self, text):
        if len(text) > 0 and all(t.isalpha() or t.isdigit() for t in text):
            self.accept_button.setEnabled(True)
        else:
            self.accept_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

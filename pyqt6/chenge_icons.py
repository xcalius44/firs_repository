import sys
import random

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Change icons")
        self.setWindowIcon(QIcon("images/pyqt_logo.png"))
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        info_label = QLabel("Натисніть на кнопку та оберіть фрукт")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.images = (
            "images/1_apple.png",
            "images/2_pineapple.png",
            "images/3_watermelon.png",
            "images/4_banana.png",
        )

        self.icon_button = QPushButton()
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addWidget(self.icon_button)
        container = QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def changeButtonIcon(self):
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

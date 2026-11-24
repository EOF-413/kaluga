import random
import sys
from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 150)
        max_x = max(0, self.width() - diameter)
        max_y = max(0, self.height() - diameter)
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if not self.circles:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(255, 255, 0))
        painter.setPen(QColor(255, 255, 0))
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

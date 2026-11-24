import sqlite3
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Информация о кофе")
        self.resize(900, 450)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.load_data()

    def load_data(self):
        try:
            conn = sqlite3.connect("coffee.sqlite")
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            if not tables:
                raise ValueError("В базе данных нет таблиц.")
            table_name = tables[0][0]

            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            conn.close()

            headers = [
                "ID",
                "Название сорта",
                "Степень обжарки",
                "Молотый/в зернах",
                "Описание вкуса",
                "Цена",
                "Объем упаковки",
            ]

            self.table.setColumnCount(len(headers))
            self.table.setHorizontalHeaderLabels(headers)
            self.table.setRowCount(len(rows))

            for row_idx, row_data in enumerate(rows):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(row_idx, col_idx, item)

            self.table.resizeColumnsToContents()

        except sqlite3.Error as e:
            QMessageBox.critical(
                self, "Ошибка БД", f"Не удалось прочитать базу данных:\n{e}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())


import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget
)


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Task Manager")
        self.resize(400, 300)

        # Create widgets
        self.title = QLabel("My Task Manager")
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter a task...")

        self.add_button = QPushButton("Add")
        self.delete_button = QPushButton("Delete Selected Task")
        self.task_list = QListWidget()

        # Create layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        input_layout.addWidget(self.input)
        input_layout.addWidget(self.add_button)

        main_layout.addWidget(self.title)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(self.delete_button)

        self.setLayout(main_layout)

        # Connect signals to functions
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.input.returnPressed.connect(self.add_task)

    def add_task(self):
        task = self.input.text().strip()

        if task:
            self.task_list.addItem(task)
            self.input.clear()

    def delete_task(self):
        row = self.task_list.currentRow()

        if row >= 0:
            self.task_list.takeItem(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())

# PyQT6 doc for function reference
# https://www.riverbankcomputing.com/static/Docs/PyQt6/
# Use QT Designer
# uvx --from pyside6-essentials pyside6-designer
# if you run into error about application block on windows, run below instead
# go to smart app control and turn it OFF



import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class TextDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        # Load the window and widgets created in Qt Designer.
        ui_file = Path(__file__).with_name("test.ui")
        uic.loadUi(ui_file, self)

        # Run display_text when the user clicks the button.
        self.pushButton.clicked.connect(self.display_text)

    def display_text(self):
        # Read the input field and show its text in the label.
        self.label.setText(self.textEdit.toPlainText())


if __name__ == "__main__":
    # Create the Qt application and display the window.
    app = QApplication(sys.argv)
    window = TextDisplayApp()
    window.show()
    sys.exit(app.exec())
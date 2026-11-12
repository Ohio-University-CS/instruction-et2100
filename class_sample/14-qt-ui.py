# PyQT6 doc for function reference
# https://www.riverbankcomputing.com/static/Docs/PyQt6/
# Use QT Designer
# uvx --from pyside6-essentials pyside6-designer
# if you run into error about application block on windows, run below instead
# go to smart app control and turn it OFF


# use QT designer to design a application UI
# with a input that take people's text, 
# then a button to click in order to submit that input
# and a label somewhere says "done" when button clicked


# have 2 input box, one for username and one for password
# when click on button, it should display the username and password is correct or not
# (username: admin, password: admin)
# have 2 feedback text, where one display login status and one display username










import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class TextDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        # Load the window and widgets created in Qt Designer.
        ui_file = Path(__file__).with_name("class_demo.ui")
        uic.loadUi(ui_file, self)

        # Run display_text when the user clicks the button.
        self.submit_button.clicked.connect(self.display_text)

    def display_text(self):
        # Read the input field and show its text in the label.
        # self.feedback_text.setText("done")
        self.feedback_text.setText(self.username_input.text())


if __name__ == "__main__":
    # Create the Qt application and display the window.
    app = QApplication(sys.argv)
    window = TextDisplayApp()
    window.show()
    sys.exit(app.exec())
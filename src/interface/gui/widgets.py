from PyQt5.QtWidgets import QTextEdit, QPushButton, QLabel, QScrollArea, QWidget
from PyQt5.QtCore import Qt

class ThoughtInput(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("What’s on your mind?")
        self.setFixedHeight(100)

class SubmitButton(QPushButton):
    def __init__(self):
        super().__init__("Reflect")

class EchoLabel(QLabel):
    def __init__(self):
        super().__init__("EchoTwin will respond here...")
        self.setWordWrap(True)

class TimelineDisplay(QScrollArea):
    def __init__(self):
        super().__init__()
        self.content = QTextEdit()
        self.content.setReadOnly(True)
        self.content.setPlaceholderText("Your thoughts will appear here...")
        self.setWidget(self.content)
        self.setWidgetResizable(True)
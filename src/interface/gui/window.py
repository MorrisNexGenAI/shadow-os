import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from src.interface.gui.widgets import ThoughtInput, SubmitButton, EchoLabel, TimelineDisplay
from src.interface.gui.handlers import SubmitHandler

class ShadowOSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shadow OS: The Thought Chamber")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Widgets
        self.thought_input = ThoughtInput()
        self.submit_btn = SubmitButton()
        self.echo_label = EchoLabel()
        self.timeline = TimelineDisplay()

        # Add to layout
        layout.addWidget(self.thought_input)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.echo_label)
        layout.addWidget(self.timeline)

        # Connect handler
        self.handler = SubmitHandler(self.thought_input, self.echo_label, self.timeline)
        self.submit_btn.clicked.connect(self.handler.on_submit)

        # Style (dark theme)
        self.setStyleSheet("""
            QMainWindow { background-color: #2b2b2b; }
            QTextEdit, QLabel { 
                background-color: #3c3f41; 
                color: #d3d3d3; 
                border: 1px solid #555; 
                padding: 5px; 
            }
            QPushButton { 
                background-color: #4a4a4a; 
                color: #d3d3d3; 
                border: 1px solid #666; 
                padding: 5px; 
            }
            QPushButton:hover { background-color: #5a5a5a; }
        """)

def run_gui():
    app = QApplication(sys.argv)
    window = ShadowOSWindow()
    window.show()
    sys.exit(app.exec_())
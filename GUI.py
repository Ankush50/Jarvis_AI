from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtCore import Qt
from modules.command_handler import handle_command  # Ensure this returns a valid response
from modules.stt import listen  # Ensure this returns a valid text

class JarvisApp(QWidget):
    def __init__(self):
        super().__init__()
        self.dark_mode = True  # Default to dark mode
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("JARVIS AI Assistant")
        self.set_dark_mode()

        layout = QVBoxLayout()

        # AI Visual
        self.ai_visual = QLabel(self)
        self.ai_visual.setAlignment(Qt.AlignCenter)
        movie = QMovie("ai_visuals")  # Replace with the correct GIF file path
        if movie.isValid():  # Check if GIF is valid
            self.ai_visual.setMovie(movie)
            movie.start()
        else:
            self.ai_visual.setText("AI Visual Not Found")  # Display error message if GIF is invalid
        layout.addWidget(self.ai_visual)

        # Input Section
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Type your command here...")
        input_layout.addWidget(self.input_box)

        self.execute_button = QPushButton("Execute", self)
        self.execute_button.clicked.connect(self.execute_command)
        input_layout.addWidget(self.execute_button)
        layout.addLayout(input_layout)

        # Voice Command Button
        self.voice_button = QPushButton("Voice Command", self)
        self.voice_button.clicked.connect(self.execute_voice_command)
        layout.addWidget(self.voice_button)

        # Toggle Mode Button
        self.toggle_button = QPushButton("Switch to Light Mode", self)
        self.toggle_button.clicked.connect(self.toggle_mode)
        layout.addWidget(self.toggle_button)

        # Output Section
        self.output_box = QTextBrowser(self)
        layout.addWidget(self.output_box)

        self.setLayout(layout)

    def set_dark_mode(self):
        """Apply dark mode theme."""
        self.setStyleSheet("""
            QWidget {
                background-color: #2C2F33;
                color: #FFFFFF;
                font-family: Arial, sans-serif;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #7289DA;
                border-radius: 5px;
            }
            QPushButton {
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #7289DA, stop: 1 #99AAB5
                );
                border: none;
                padding: 10px;
                color: #FFFFFF;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #99AAB5, stop: 1 #7289DA
                );
            }
            QTextBrowser {
                background-color: #23272A;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
        """)

    def set_light_mode(self):
        """Apply light mode theme."""
        self.setStyleSheet("""
            QWidget {
                background-color: #F7F7F7;
                color: #000000;
                font-family: Arial, sans-serif;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #5D5D5D;
                border-radius: 5px;
            }
            QPushButton {
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #5D5D5D, stop: 1 #A0A0A0
                );
                border: none;
                padding: 10px;
                color: #FFFFFF;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #A0A0A0, stop: 1 #5D5D5D
                );
            }
            QTextBrowser {
                background-color: #FFFFFF;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
        """)

    def toggle_mode(self):
        """Toggle between dark and light mode."""
        if self.dark_mode:
            self.set_light_mode()
            self.toggle_button.setText("Switch to Dark Mode")
        else:
            self.set_dark_mode()
            self.toggle_button.setText("Switch to Light Mode")
        self.dark_mode = not self.dark_mode

    def execute_command(self):
        command = self.input_box.text()
        self.output_box.append(f"You: {command}")
        response = handle_command(command)
        if response is None:  # Ensure no "None" is displayed
            response = "I'm sorry, I didn't understand that."
        self.display_ai_response(response)
        self.input_box.clear()

    def execute_voice_command(self):
        command = listen()  # Use your STT module to capture voice
        self.output_box.append(f"You (voice): {command}")
        response = handle_command(command)
        if response is None:  # Ensure no "None" is displayed
            response = "I'm sorry, I didn't understand that."
        self.display_ai_response(response)

    def display_ai_response(self, response):
        """Show AI's response on the GUI."""
        self.output_box.append(f"JARVIS: {response}")


if __name__ == "__main__":
    app = QApplication([])

    # Set application-wide font for a modern look
    font = QFont("Arial", 10)
    app.setFont(font)

    jarvis_app = JarvisApp()
    jarvis_app.show()
    app.exec_()

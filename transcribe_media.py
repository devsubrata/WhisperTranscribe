import sys
import os
import whisper
import warnings

from PyQt6.QtGui import QCursor, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)

# Suppress specific warnings
warnings.filterwarnings(
    "ignore", message="FP16 is not supported on CPU; using FP32 instead")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transcribe")
        self.file_path = ""

        default_dir = os.path.join(os.path.expanduser("~"), "Desktop")
        self.input_dir = default_dir
        self.ouput_dir = default_dir

        layout = QVBoxLayout()

        button1 = QPushButton("Open media file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)

        self.button2 = QPushButton("Transcribe")
        self.button2.clicked.connect(self.transcript_file)
        layout.addWidget(self.button2)

        button3 = QPushButton("Set input folder")
        button3.clicked.connect(self.set_input_directory)
        layout.addWidget(button3)

        output_row = QHBoxLayout()
        button4 = QPushButton("Set output folder")
        button4.clicked.connect(self.set_output_directory)
        output_row.addWidget(button4)
        button5 = QPushButton("Open output folder")
        button5.clicked.connect(self.open_output_directory)
        output_row.addWidget(button5)
        layout.addLayout(output_row)

        [self.style_btn(btn) for btn in [button1, self.button2, button3, button4, button5]]

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def get_filename(self):
        FILE_FILTERS = [
            "MP3 Files (*.mp3)",
            "WAV Files (*.wav)",
            "FLAC Files (*.flac)",
            "OGG Files (*.ogg)",
            "M4A Files (*.m4a)",
            "AAC Files (*.aac)",
            "WMA Files (*.wma)",
            "OPUS Files (*.opus)",
            "MP4 Video Files (*.mp4)",
            "MKV Video Files (*.mkv)",
            "AVI Video Files (*.avi)",
            "MOV Video Files (*.mov)",
            "WMV Video Files (*.wmv)",
            "FLV Video Files (*.flv)",
            "WEBM Video Files (*.webm)",
        ]
        caption = "Open a audio or video file"
        initial_filter = FILE_FILTERS[0]
        filters = ";;".join(FILE_FILTERS)

        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            directory=self.input_dir,
            filter=filters,
            initialFilter=initial_filter,
        )

        self.file_path = filename

    def transcript_file(self):
        
        if (not self.file_path):
            self.show_dialog("No file opened!", "Please open a file",
                                QMessageBox.Icon.Warning)
            return
        
        self.button2.setEnabled(False)

        try:
            model = whisper.load_model("base")
            result = model.transcribe(self.file_path)

            output_file_name = f"{os.path.splitext(os.path.basename(self.file_path))[0]}.txt"
            output_file = os.path.join(self.ouput_dir, output_file_name)

            with open(output_file, "w") as file:
                file.write(result['text'])

            self.show_dialog("Transcribed!", f"Transcription saved to\n {self.ouput_dir}",
                            QMessageBox.Icon.Information)
            
        except Exception as exp:
            self.show_dialog("Transcription Failed!",
                                f"Error: {str(exp)}", QMessageBox.Icon.Critical)

        finally:
            self.button2.setEnabled(True)

    def style_btn(self, btn):
        btn.setFixedHeight(50)
        btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def show_dialog(self, title, message, icon):
        dialog = QMessageBox(self)
        dialog.setWindowTitle(title)
        dialog.setStyleSheet(
            "QLabel { font-size: 15px; color: blue;}"
        )
        dialog.setText(message)
        dialog.setIcon(icon)
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()

    def set_input_directory(self):
        self.input_dir = QFileDialog.getExistingDirectory(
            self, "Select a input directory", self.input_dir)

    def set_output_directory(self):
        self.ouput_dir = QFileDialog.getExistingDirectory(
            self, "Select a output directory", self.ouput_dir)
        
    def open_output_directory(self):
        os.startfile(self.ouput_dir)

app = QApplication(sys.argv)

def load_stylesheet(file_path):
    with open(file_path, "r") as file:
        return file.read()

stylesheet = load_stylesheet(os.path.join(
    os.path.dirname(__file__), 'styles.qss'))
app.setStyleSheet(stylesheet)

window = MainWindow()
window.show()

app.exec()

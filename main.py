import os
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QLabel, QVBoxLayout, QPushButton


def calculate_directory_size(directory_path, label):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
            label.setText("Total size: " + str(round(total_size / (1024 * 1024 * 1024), 2)) + " GB) ||" + str(
                round(total_size / (1024 * 1024), 2)) + " MB, || "
                          + str(total_size) + " - bytes || ")
            QApplication.processEvents()
    return total_size


def main():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    window.setMinimumWidth(900)
    window.setLayout(layout)

    progress_bar = QProgressBar(window)
    progress_bar.setMaximum(100)
    progress_bar.setMinimum(0)

    directory_path = "D:\Steam"

    label = QLabel(window)
    label.setGeometry(30, 70, 300, 25)

    button = QPushButton("Calculate Directory Size")
    button.clicked.connect(lambda: perform_directory_calculation(directory_path, label, progress_bar))

    layout.addWidget(progress_bar)
    layout.addWidget(button)
    layout.addWidget(label)

    window.show()
    app.exec_()


def perform_directory_calculation(directory_path, label, progress_bar):
    current_size = 0
    f=open("data.txt", "w")
    total_size = calculate_directory_size(directory_path, label)
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            label.setText(filename)
            f.write(str(os.path.getsize(filepath))+" ~|~ "+filepath+"\n")
            current_size += os.path.getsize(filepath)
            progress_percent = int((current_size / total_size) * 100)
            progress_bar.setValue(progress_percent)
            QApplication.processEvents()
    f.close()
main()
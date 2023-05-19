import os
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QLabel

def calculate_directory_size(directory_path, label):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
            label.setText("Total size: " + str(round(total_size/(1024*1024*1024), 2)) + " GB) ||" + str(round(total_size/(1024*1024), 2)) + " MB, || "
                          + str(total_size) + " - bytes || ")
            QApplication.processEvents()
    return total_size

def main():
    app = QApplication([])
    window = QWidget()
    progress_bar = QProgressBar(window)
    progress_bar.setGeometry(30, 40, 200, 25)
    directory_path = "D:\Steam"#"D:/MAIN"
    progress_bar.setMaximum(100)
    progress_bar.setMinimum(0)
    current_size = 0
    label = QLabel(window)
    label.setGeometry(30, 70, 300, 25)
    window.show()
    total_size = calculate_directory_size(directory_path, label)
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            label.setText(filepath)
            # process file here
            current_size += os.path.getsize(filepath)
            progress_percent = int((current_size / total_size) * 100)
            progress_bar.setValue(progress_percent)
            QApplication.processEvents()
    app.exec_()

main()
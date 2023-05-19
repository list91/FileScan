import os
import datetime
import random
import time

from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton


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
    window.setMaximumHeight(900)
    window.setLayout(layout)

    progress_bar = QProgressBar(window)
    progress_bar.setMaximum(100)
    progress_bar.setMinimum(0)

    directory_path = "D:\MAIN\РАБОЧИЙ СТОЛ(все подряд)\LABORANT\img"

    labelProgress = QLabel(window)
    labelSearchResults = QLabel(window)
    labelSearchResults.setGeometry(30, 110, 300, 25)
    labelProgress.setGeometry(30, 70, 300, 25)

    button_layout = QHBoxLayout()

    button = QPushButton("Set an example")
    button.clicked.connect(lambda: perform_directory_calculation(directory_path, labelProgress, progress_bar, labelDt))

    button2 = QPushButton("Compare")
    button2.clicked.connect(lambda: perform_directory_compare(directory_path, labelSearchResults))

    layout2 = QVBoxLayout()
    layout2.addStretch()
    labelDt = QLabel(window)
    layout2.addWidget(labelDt)

    button_layout.addWidget(button)
    button_layout.addWidget(button2)

    layout.addWidget(progress_bar)
    layout.addLayout(button_layout)
    layout.addWidget(labelProgress)
    layout.addWidget(labelSearchResults)
    layout.addLayout(layout2)

    window.show()
    app.exec_()


def perform_directory_calculation(directory_path, label, progress_bar, labelDt):
    current_size = 0
    # data = {}
    date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f = open("data.txt", "w")
    f.write(date+"\n")
    total_size = calculate_directory_size(directory_path, label)
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            size = os.path.getsize(filepath)
            label.setText(filename)
            # data[filepath] = size
            f.write(str(size) + " ~|~ " + filepath + "\n")
            current_size += os.path.getsize(filepath)
            progress_percent = int((current_size / total_size) * 100)
            progress_bar.setValue(progress_percent)
            QApplication.processEvents()
    f.close()
    fr = open("data.txt", "r")
    labelDt.setText("The last example: " + fr.readlines()[0])
    fr.close()

def perform_directory_compare(directory_path, labelSearchResults):
    labelSearchResults.clear()
    timeStart=time.time()
    spinner = ["-", "\\", "|", "/"]
    historiFile_lines = open("data.txt", "r").readlines()
    data = {}
    historiFile_linesData=historiFile_lines[1:]
    for line in historiFile_linesData:
        elements = line.split(" ~|~ ")
        data[elements[1][:-1]] = elements[0]
    for dirpath, dirnames, filenames in os.walk(directory_path):
        tic=0

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            size = os.path.getsize(filepath)

            if filepath in data and data[filepath] == str(size):
                None

            elif filepath in data and data[filepath] != size:
                current_text = labelSearchResults.text()
                labelSearchResults.setText(current_text + "\n {MODIFIED} " + filepath)

            else:
                current_text = labelSearchResults.text()
                labelSearchResults.setText(current_text + "\n {NEW} " + filepath)
                # labelSearchResults.setText(spinner[tic%len(spinner)])
                # tic+=1
                # labelSearchResults.append("no differences were found")
                # label.setText(filename)
                # data[filepath] = size
    current_text = labelSearchResults.text()
    timeEnd = time.time()
    labelSearchResults.setText(current_text + "\n {FINISHED} "+str(int(timeStart-timeEnd))+"sec.")


main()
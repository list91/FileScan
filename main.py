import os
import datetime
import time
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QTextDocument, QBrush, QColor
from PyQt5.QtCore import Qt
tic = 0
tic2 = 0

def calculate_directory_size(directory_path, label):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except Exception as e:
                print(e)
                print(filepath+"\n\n")
            label.setText(f"Total size: {round(total_size / (1024 * 1024 * 1024), 2)} GB) ||{str(round(total_size / (1024 * 1024), 2))} MB, || {total_size} - bytes || ")
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
    directory_path = "C:\\"

    labelProgress = QLabel(window)
    labelSearchResults = QLabel(window)
    labelSearchResults.setGeometry(30, 110, 300, 25)
    labelProgress.setGeometry(30, 70, 300, 25)

    button_layout = QHBoxLayout()
    button = QPushButton("Set an example")
    button.clicked.connect(lambda: calculation_and_save_data(directory_path, labelProgress, progress_bar, labelDt, labelSearchResults))
    button2 = QPushButton("Compare")
    button2.clicked.connect(lambda: compare_items(directory_path, labelSearchResults, labelProgress))
    # button2.clicked.connect(lambda: perform_directory_compare(directory_path, labelSearchResults))

    layout2 = QVBoxLayout()
    layout2.addStretch()
    labelDt = QLabel(window)

    labelProgress.setStyleSheet("background-color: #eae698")
    labelSearchResults.setStyleSheet("background-color: #b798ea")
    labelDt.setStyleSheet("background-color: #ffc7bd")

    layout2.addWidget(labelDt)
    button_layout.addWidget(button)
    button_layout.addWidget(button2)

    layout.addWidget(progress_bar)
    layout.addLayout(button_layout)
    layout.addWidget(labelProgress)
    layout.addWidget(labelSearchResults)
    layout.addLayout(layout2)

    if os.path.isfile("data.txt"):
        f = open("data.txt", "r", encoding="utf-8")
        labelDt.setText(f.readlines()[0][:-1])
        f.close()

    window.show()
    app.exec_()

def calculation_and_save_data(directory_path, label, progress_bar, labelDt, labelSearchResults):
    current_size = 0
    total_size = calculate_directory_size(directory_path, label)
    # calculate_directory_sizes(directory_path, label)
    date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    file = open("folder_sizes.txt", "w", encoding="utf-8")
    # for dirpath, dirnames, filenames in os.walk(directory_path):
        # total_sizeFolder = sum([os.path.getsize(os.path.join(dirpath, file)) for file in filenames])
        # file.write(f"{total_sizeFolder} ~|~ {dirpath}\n")
        # label.setText(f"{dirpath} ~|~ {total_sizeFolder}\n")
        # QApplication.processEvents()
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(date+ " :: " + directory_path + "\n")
        for dirpath, dirnames, filenames in os.walk(directory_path):
            try:
                total_sizeFolder = sum([os.path.getsize(os.path.join(dirpath, file)) for file in filenames])
                file.write(f"{total_sizeFolder} ~|~ {dirpath}\n")
                label.setText(dirpath)#
                QApplication.processEvents()
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    size = os.path.getsize(filepath)
                    labelSearchResults.setText(filename)#
                    QApplication.processEvents()
                    f.write(f"{size} ~|~ {filepath}\n")
                    current_size += size
                    progress_percent = int((current_size / total_size) * 100)
                    progress_bar.setValue(progress_percent)
                    QApplication.processEvents()
            except Exception as e:
                progress_bar.setValue(progress_percent)
                print("-----------------\n\n")
                print(e)

    with open("data.txt", "r", encoding="utf-8") as fr:
        labelDt.setText(f"The last example: {fr.readlines()[0]}")
    label.setText("")
    labelSearchResults.setText("END")
    progress_bar.format()

def compare_items(directory_path, labelSearchResults, label):
    btn2_FoldersCOMPARE(directory_path, labelSearchResults, label)
    # btn_FilesCOMPARE(directory_path, labelSearchResults, label)
    current_text = labelSearchResults.text() + "\n"
    labelSearchResults.setText(current_text+"\n"+"{END}")
def btn_FilesCOMPARE(directory_path, labelSearchResults, label):
    # labelSearchResults.clear()
    # timeStart = time.time()



    # historiFile = open("folder_sizes.txt", "r", encoding="utf-8")
    # historiFile_lines = historiFile.readlines()
    # dataF = {}
    # for line in historiFile_lines:
    #     elements = line.split(" ~|~ ")
    #     dataF[elements[1][:-1]] = elements[0]


    # spinner = ["-", "\\", "|", "/"]
    historiFile = open("data.txt", "r", encoding="utf-8")
    historiFile_lines = historiFile.readlines()[1:]
    data = {line.split(" ~|~ ")[1][:-1]: line.split(" ~|~ ")[0] for line in historiFile_lines}
    n=0
    for dirpath, dirnames, filenames in os.walk(directory_path):
    #     total_size = sum([os.path.getsize(os.path.join(dirpath, file)) for file in filenames])
    #     if dirpath in data and data[dirpath] == str(total_size):
    #         continue
    #     current_text = labelSearchResults.text() + "\n"
    #     if dirpath not in data:
    #         current_text += f"{{NEW folder}} {dirpath}"
    #     else:
    #         current_text += f"{{MODIFIED folder}} {dirpath}"
    #     labelSearchResults.setText(current_text)
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if n % 2 == 0:
                labelSearchResults.setStyleSheet("color:red")
                # label.setText(dirpath+"\n"+filename)
                # QApplication.processEvents()
            else:
                labelSearchResults.setStyleSheet("color:blue")
            label.setText(dirpath + "\n" + filename)
            QApplication.processEvents()
            # labelSearchResults.setText(filepath)
            # QApplication.processEvents()
            n+=1
            try:
                size = os.path.getsize(filepath)
                if filepath in data and data[filepath] == str(size):
                    continue
                current_text = labelSearchResults.text() + "\n"
                if filepath not in data:
                    current_text += f"{{NEW file}} {filepath}"
                else:
                    current_text += f"{{MODIFIED file}} {filepath}"
                labelSearchResults.setText(current_text)
                QApplication.processEvents()
            except Exception as e:
                print(e)
                print("\n\n")
    # perform_directory_NOfiles_compare(directory_path, labelSearchResults)
    # labelSearchResults.setText(labelSearchResults.text() + f"\n\n {{FINISHED}} {int(time.time()-timeStart)} sec.")


def btn2_FoldersCOMPARE(directory_path, labelSearchResults, label):
    historiFile = open("folder_sizes.txt", "r", encoding="utf-8")
    historiFile_lines = historiFile.readlines()
    dataF = {}
    labelSearchResults.clear()
    for line in historiFile_lines:
        elements = line.split(" ~|~ ")
        dataF[elements[1][:-1]] = elements[0]
    filename = ''
    for dirpath, dirnames, filenames in os.walk(directory_path):
        label.setText(dirpath + "\n" + filename)
        QApplication.processEvents()
        total_size = sum([os.path.getsize(os.path.join(dirpath, file)) for file in filenames])
        if dirpath in dataF and dataF[dirpath] == str(total_size):
            continue
        current_text = labelSearchResults.text() + "\n"
        if dirpath not in dataF:
            current_text += f"{{NEW folder}} {dirpath}"
        else:
            current_text += f"{{MODIFIED folder}} {dirpath}"
        for filename in filenames:
            label.setText(dirpath+"\n"+filename)
            QApplication.processEvents()
            filepath = os.path.join(dirpath, filename)
            size = os.path.getsize(filepath)
            if filepath in dataF and dataF[filepath] == str(size):
                continue
            current_text = labelSearchResults.text() + "\n"
            if filepath not in dataF:
                current_text += f"{{NEW file}} {filepath}"
            else:
                current_text += f"{{MODIFIED file}} {filepath}"
            labelSearchResults.setText(current_text)
            QApplication.processEvents()

            # QApplication.processEvents()
        # QApplication.processEvents()
    # labelSearchResults.setText(current_text+"\n\n")
    # perform_directory_NOfiles_compare(directory_path, labelSearchResults)
    # labelSearchResults.setText(labelSearchResults.text() + f"\n\n {{FINISHED}} {int(time.time() - timeStart)} sec.")


def perform_directory_NOfiles_compare(directory_path, labelSearchResults):
    with open("folder_sizes.txt", "r", encoding="utf-8") as historiFile:
        historiFile_lines = historiFile.readlines()
        data = {line.split(" ~|~ ")[1][:-1]: line.split(" ~|~ ")[0] for line in historiFile_lines}

    for dirpath, dirnames, filenames in os.walk(directory_path):
        total_size = sum([os.path.getsize(os.path.join(dirpath, file)) for file in filenames])
        if dirpath in data and data[dirpath] == str(total_size):
            continue
        current_text = labelSearchResults.text() + "\n"
        if dirpath not in data:
            current_text += f"{{NEW folder}} {dirpath}"
        else:
            current_text += f"{{MODIFIED folder}} {dirpath}"
        labelSearchResults.setText(current_text)


def calculate_directory_sizes(directory_path, label):
    with open("folder_sizes.txt", "w", encoding="utf-8") as file:
        for dirpath, dirnames, filenames in os.walk(directory_path):
            total_size = sum([os.path.getsize(os.path.join(dirpath, file)) for file in filenames])
            file.write(f"{total_size} ~|~ {dirpath}\n")
            label.setText(f"{dirpath} ~|~ {total_size}\n")
            QApplication.processEvents()


if __name__ == '__main__':
    main()
"""разобраться пошагово с работой кнопки1 и кнопки2, прогресбар не до конца доходит,
потом разукрась интерфейс (вроде)"""
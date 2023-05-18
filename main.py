from PyQt5 import QtWidgets, QtGui, QtCore


class ProgressBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File System Change Scanner")
        self.progress = QtWidgets.QProgressBar()

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start_progressbar)

        self.stop_button = QtWidgets.QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_progressbar)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.progress)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

    def start_progressbar(self):
        self.progress.setRange(0, 100)
        self.progress.setValue(0)

        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self)

    def timerEvent(self, event):
        if self.progress.value() >= 100:
            self.timer.stop()
            return

        value = self.progress.value() + 1
        self.progress.setValue(value)

    def stop_progressbar(self):
        if hasattr(self, 'timer'):
            self.timer.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProgressBar()
    widget.show()
    app.exec_()
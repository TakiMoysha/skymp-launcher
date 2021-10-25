import sys
import asyncio
import time

from PyQt5.QtWidgets import QApplication, QProgressBar, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QFrame, QPushButton

from quamash import QEventLoop, QThreadExecutor

class ProgressBar(QMainWindow):
    def __init__(self, loop):
        super(ProgressBar, self).__init__()

        self.loop = loop

        self.setMinimumSize(640, 480)

        self.central_frame = QFrame()

        self.v_box_layout = QVBoxLayout(self.central_frame)

        self.progress = QProgressBar()
        self.progress.setRange(0, 99)

        self.start_button = QPushButton()
        self.start_button.setText('Button start')
        self.start_button.clicked.connect(lambda: self.onStartClick())

        self.wait_button = QPushButton()
        self.wait_button.setText('Button wait')
        self.wait_button.clicked.connect(lambda: self.onWaitClick())

        self.v_box_layout.addWidget(self.progress)
        self.v_box_layout.addWidget(self.start_button)
        self.v_box_layout.addWidget(self.wait_button)

        self.setCentralWidget(self.central_frame)

        self.show()

    async def master(self):
        print(loop.is_running())
        await self.first_50()
        with QThreadExecutor(1) as exec:
            await loop.run_in_executor(exec, self.last_50)
        print('ready!')


    def updateValue(self, val):
        self.progress.setValue(val)
        print(0, str(val))


    async def first_50(self):
        for i in range(50):
            self.updateValue(i)
            await asyncio.sleep(.1)

    async def last_50(self):
        for i in range(50, 100):
            self.updateValue(i)
            await asyncio.sleep(.1)


    def onStartClick(self):
        print("start")
        self.loop.create_task(self.master())
        self.loop.start()
        # loop.run_until_complete()


    def onWaitClick(self):
        print("wait")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = ProgressBar(loop)

    with loop:
        loop.run_forever()
    # sys.exit(app.exec())
# from tempfile import TemporaryDirectory TODO: use tempfiles
from pathlib import Path

from PyQt5 import QtWidgets, QtCore, QtWebEngine, QtGui
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, pyqtSlot, QObject
from PyQt5.QtWebChannel import QWebChannel

from src.utils import get_location
from src.config import logger
from src.marker import Marker


DEFAULT_PATH = Path(__file__).parent
MAP_FILE = 'html/map.html'


class MapView(QWebEngineView):

    def __init__(self, zoom=13):
        super().__init__()

        self.markers = []
        self.default_zoom = zoom
        self.load(QUrl.fromLocalFile(str(DEFAULT_PATH / MAP_FILE)))

    def add_marker(self, location):

        marker = Marker(location)
        logger.info(f'New {marker}')

        self.page().runJavaScript(
            f"add_marker({marker.lat}, {marker.lon}, '{marker.popup}');"
        )
        self.markers.append(marker)

    def move_to(self, location):
        lat, lon = location.latitude, location.longitude
        logger.info(f"Moving to ({lat}, {lon})")
        self.page().runJavaScript(f'move_to({lat}, {lon});')


class MapWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Map Interactive')

        # map
        self.view = MapView()

        # locate button
        self.locate_btn = QtWidgets.QPushButton('Locate')
        self.locate_btn.clicked.connect(self.locate_clicked)

        # input line
        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText('Enter location')

        # configure layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self.view)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.locate_btn)

    def process_input(self):
        text = self.input.text()
        location = get_location(text)
        self.view.add_marker(location)
        self.view.move_to(location)

    def locate_clicked(self):
        logger.debug('Locate button clicked')
        self.process_input()

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            logger.debug('Enter pressed')
            self.process_input()

        else:
            super().keyPressEvent(qKeyEvent)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = MapWidget()

    w.show()
    app.exec_()

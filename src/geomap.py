from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl, pyqtSlot, QObject
from PyQt5.QtWebChannel import QWebChannel

from src.config import logger
from src.marker import Marker, Locator


DEFAULT_PATH = Path(__file__).parent
MAP_FILE = 'html/map.html'


class CallHandler(QObject):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    @pyqtSlot()
    def test(self):
        print('call received')

    @pyqtSlot(float, float)
    def locate(self, lat, lon):
        logger.debug(f'Clicked at ({lat}, {lon})')
        location = self.parent.locator.from_coordinates(lat, lon)
        self.parent.add_marker(location)


class MapView(QWebEngineView):

    def __init__(self, zoom=13):
        super().__init__()
        self.locator = Locator()

        self.markers = []
        self.default_zoom = zoom
        self.channel = QWebChannel()
        self.handler = CallHandler(self)
        self.channel.registerObject('handler', self.handler)
        self.page().setWebChannel(self.channel)
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
        logger.info(f'Trying to find "{text}"')
        location = self.view.locator.from_query(text)
        self.view.add_marker(location)
        self.view.move_to(location)

    def locate_clicked(self):
        logger.debug('Locate button clicked')
        self.process_input()

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == Qt.Key_Return:
            logger.debug('Enter pressed')
            self.process_input()

        else:
            super().keyPressEvent(qKeyEvent)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = MapWidget()

    w.show()
    app.exec_()

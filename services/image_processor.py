from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

def scaleImage(img, width, height):
    qim = ImageQt(img).copy()
    pixmap = QPixmap.fromImage(qim)
    scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)

    return scaled_pixmap
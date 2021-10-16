import sys
import os
import qrc_resources
import widgets.cognitive_service_file_upload as UICognitiveServiceFileUploadForm
import widgets.content_tab as UIContentTab

from qt_material import apply_stylesheet
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QCheckBox, QWidget, QMainWindow, QMenuBar, QMenu, QToolBar, QAction
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowIcon(QIcon(resource_path('resources/images/logo.png')))
        self.setWindowTitle("Face")
        self.resize(1200, 800)

        # Create an outer layout
        outerLayout = QVBoxLayout()
        
        topLayout = QVBoxLayout()
        topLayout.addWidget(UICognitiveServiceFileUploadForm.CognitiveServiceFileUpload(self))

        optionsLayout = QVBoxLayout()
        self.chkIsPrintStatisticsOnImage = QCheckBox("Print Statistics on Image")
        optionsLayout.addWidget(self.chkIsPrintStatisticsOnImage)
        optionsLayout.addStretch()

        tabsLayout = QVBoxLayout()
        tabsLayout.addWidget(UIContentTab.ContentTab(self))
        tabsLayout.addStretch()

        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        outerLayout.addLayout(tabsLayout)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        # Set the layout on the application's window
        wid.setLayout(outerLayout)

        self._createActions()
        self._createMenuBar()
        self._createToolBars()    

    def updateEmotionChart(self, faces):
        self.emotionChart.displayChart(faces)

    def _createActions(self):
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help") 
        self.setMenuBar(menuBar)

    def _createToolBars(self):
        mainToolBar = QToolBar("Main", self)
        mainToolBar.addAction(QAction(QIcon(":home.svg"), "&Home", self))
        mainToolBar.addAction(QAction(QIcon(":history.svg"), "H&istory", self))
        mainToolBar.addAction(QAction(QIcon(":windows.svg"), "&Microsoft Store", self))
        mainToolBar.addAction(QAction(QIcon(":question-circle.svg"), "&About Us", self))
        self.addToolBar(Qt.LeftToolBarArea, mainToolBar)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    apply_stylesheet(app, theme='dark_blue.xml')

    win.show()
    sys.exit(app.exec_())
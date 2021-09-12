import widgets.emotion_chart as UIEmotionChart

from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget, QLabel

class ContentTab(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super(ContentTab, self).__init__(*args, **kwargs)

        self.parent = parent

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        self.layout.addWidget(self.tabs)
        self.layout.addStretch()
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Analysed Photo")
        self.tabs.addTab(self.tab2,"Statistics")
        
        # Create Tab 01
        self.tab1.layout = QVBoxLayout()
        self.parent.mainImage = QLabel(self.parent)
        self.tab1.layout.addWidget(self.parent.mainImage)
        self.tab1.setLayout(self.tab1.layout)

        # Create Tab 02
        self.tab2.layout = QVBoxLayout()
        self.parent.emotionChart = UIEmotionChart.EmotionChart(self.parent)
        self.tab2.layout.addWidget(self.parent.emotionChart)
        self.tab2.setLayout(self.tab2.layout)
        
        self.setLayout(self.layout)
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis

class EmotionChart(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super(EmotionChart, self).__init__(*args, **kwargs)

        self.parent = parent
      
        self.chartview = None

        self.layout = QVBoxLayout()  
        self.setLayout(self.layout)
    
    def displayChart(self, faces):
        #create barseries
        set0 = QBarSet("Happiness")
        set1 = QBarSet("Sadness")
        set2 = QBarSet("Neutral")
        set3 = QBarSet("Anger")
        set4 = QBarSet("Surprise")
 
        categories = []
        i = 0
        for face in faces:
            detected_attributes = face.face_attributes.as_dict()
            i = i+1
            categories.append('Face ' + str(i))

            if 'emotion' in detected_attributes.keys():
                for emotion_name in detected_attributes['emotion']:
                    if emotion_name == 'happiness':
                        set0.append(detected_attributes['emotion'][emotion_name])
                    elif emotion_name == 'sadness':
                        set1.append(detected_attributes['emotion'][emotion_name])
                    elif emotion_name == 'neutral':
                        set2.append(detected_attributes['emotion'][emotion_name])
                    elif emotion_name == 'anger':
                        set3.append(detected_attributes['emotion'][emotion_name])
                    elif emotion_name == 'surprise':
                        set4.append(detected_attributes['emotion'][emotion_name])
 
        #we want to create percent bar series
        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)
 
        #create chart and add the series in the chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Emotion Chart")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeLight) 
 
        #create axis for the chart 
        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        if self.chartview != None:
            self.layout.removeWidget(self.chartview)

        self.chartview = QChartView(chart)
        self.layout.addWidget(self.chartview)
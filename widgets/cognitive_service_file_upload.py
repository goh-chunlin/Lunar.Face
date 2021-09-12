import os
import services.cognitive as cognitive
import services.image_processor as image_processor

from PyQt5.QtWidgets import QHBoxLayout, QFormLayout, QPushButton, QLineEdit, QWidget, QFileDialog, QMessageBox


class CognitiveServiceFileUpload(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super(CognitiveServiceFileUpload, self).__init__(*args, **kwargs)

        self.parent = parent

        layout = QFormLayout()
        
        self.txtCognitiveServiceEndpoint = QLineEdit()
        self.txtCognitiveServiceKey = QLineEdit()
        self.txtCognitiveServiceKey.setEchoMode(QLineEdit.Password)

        self.txtCognitiveServiceEndpoint.setText(os.getenv('AZURE_COGNITIVE_SERVICE_ENDPOINT', ''))
        self.txtCognitiveServiceKey.setText(os.getenv('AZURE_COGNITIVE_SERVICE_KEY', ''))

        layout.addRow("Cognitive Service Endpoint:", self.txtCognitiveServiceEndpoint)
        layout.addRow("Cognitive Service Key:", self.txtCognitiveServiceKey)
        
        self.txtFileDirectory = QLineEdit()
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.txtFileDirectory)
        btnBrowseImage = QPushButton("Browse...")
        btnBrowseImage.clicked.connect(self.launchBrowseImageDialog)
        hlayout.addWidget(btnBrowseImage)
        layout.addRow("Selected File:", hlayout)

        self.setLayout(layout)
    
    def launchBrowseImageDialog(self):
        file_filter = 'Images (*.png *.bmp *.jpg)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Images (*.png *.bmp *.jpg)'
        )
        
        image_directory = response[0].strip()

        self.txtFileDirectory.setText('')

        if not image_directory:
            QMessageBox.critical(self, 'File Not Specified', \
                'Please choose a valid image file.')
        else:
            self.txtFileDirectory.setText(image_directory)
            self.processImage(image_directory)

    def processImage(self, image_path):

        cog_key = self.txtCognitiveServiceKey.text().strip()
        cog_endpoint = self.txtCognitiveServiceEndpoint.text().strip()

        if not cog_key or not cog_endpoint:
            QMessageBox.critical(self, 'Azure Cognitive Service Credential Invalid', \
                'Please enter a valid Cognitive Service endpoint and key from the Azure Portal.')
        else:
            is_printing_statistics = self.parent.chkIsPrintStatisticsOnImage.isChecked()
            cognitive_result = cognitive.cognitive(image_path, cog_key, cog_endpoint, is_printing_statistics)

            img = cognitive_result[0]
            
            pixmap = image_processor.scaleImage(img, 1100, 600)
            
            self.parent.mainImage.setPixmap(pixmap)
            self.parent.updateEmotionChart(cognitive_result[1])
# Lunar.Face

<div align="center">
    <img src="https://gclstorage.blob.core.windows.net/images/Lunar.Face-banner.png" />
</div>

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Donate](https://img.shields.io/badge/$-donate-ff69b4.svg)](https://www.buymeacoffee.com/chunlin)

A desktop application with facial recognition embedded. It's built with [PyQt5](https://build-system.fman.io/pyqt5-tutorial) and using [Azure Cognitive Service Face API](https://azure.microsoft.com/en-us/services/cognitive-services/face/).

## Local Development and Use ##
1. Checkout the codes to a working directory;
2. Create a virtual environment in the working directory, execute the following command: \
   `python3 -m venv venv`
3. Activate the virtual environment on Windows, run: \
   `call venv/scripts/activate.bat` \
   On Mac and Linux, use: \
   `source venv/bin/activate`
4. Create Cognitive Service on the Azure Portal and set its API key and endpoint in the environment variables;
   ```
    SET AZURE_COGNITIVE_SERVICE_KEY=...
    SET AZURE_COGNITIVE_SERVICE_ENDPOINT=...
   ```
   Note: The reason of setting the key and endpoint in the environment variables is to auto fill them into the app. You can choose not to set them in the environment but instead, manually key them to the app for every launch of the app;
5. Browse an image with real human face;
6. Enjoy the result.

## Demo ##

<img src="https://gclstorage.blob.core.windows.net/images/Lunar.Face-screenshot1.png" />

<img src="https://gclstorage.blob.core.windows.net/images/Lunar.Face-screenshot2.png" />

## Important Packages ##
- [PyQt5](https://pypi.org/project/PyQt5/);
- [matplotlib](https://pypi.org/project/matplotlib/);
- [Microsoft Azure Cognitive Services Face Client Library](https://pypi.org/project/azure-cognitiveservices-vision-face/);
- [PyQtChart](https://pypi.org/project/PyQtChart/);
- [Qt-Material](https://pypi.org/project/qt-material/).

## License ##

This library is distributed under the GPL-3.0 License found in the [LICENSE](./LICENSE) file.
from abc import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver(metaclass = ABCMeta):
    @abstractmethod
    def set_driver():
        pass
    

class ChromeDriver(WebDriver):
    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # feeds a test pattern to getUserMedia() instead of live camera input.
        # chrome_options.add_argument('--use-fake-device-for-media-stream')
        
        # avoids the need to grant camera/microphone permissions.
        chrome_options.add_argument('--use-fake-ui-for-media-stream')
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver
    
"""
운전면허증 인증 자동화
"""
import time
from driver import ChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import KYC
import Const

KYC.connect(Const.TEST_SITE_URL)
print('=== KYC connect ===')

KYC.clickIdCardMode()
print('=== KYC clickIdCardMode ===')

KYC.enterPrivacyInfo()
print('=== KYC enterPrivacyInfo ===')

KYC.selectDriversLicense()
print('=== KYC selectDriversLicense ===')

KYC.uploadDriversLicenseFile()
print('=== KYC uploadDriversLicenseFile ===')

KYC.verifyIdCardInfo()
print('=== KYC verifyIdCardInfo ===')

print('=== TEST SUCCESS ===')

time.sleep(1000)
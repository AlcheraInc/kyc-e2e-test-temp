"""
운전면허증 인증 자동화
"""
import time
import KYC
import Const

KYC.connect(Const.TEST_SITE_URL)
print('=== KYC connect ===')

KYC.clickIdCardMode()
print('=== KYC clickIdCardMode ===')

KYC.enterPrivacyInfo()
print('=== KYC enterPrivacyInfo ===')

KYC.selectTypeOfId()
print('=== KYC selectDriversLicense ===')

KYC.uploadIdImageFile()
print('=== KYC uploadDriversLicenseFile ===')

KYC.verifyEnteredIdInfo()
print('=== KYC verifyIdCardInfo ===')

print('=== TEST SUCCESS ===')

time.sleep(1000)
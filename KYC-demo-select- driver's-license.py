"""
운전면허증 인증 자동화
"""
import time
import KYC
import Const

KYC.connect(Const.TEST_SITE_URL)
KYC.visualLog('=== KYC connect ===')

KYC.clickIdCardMode()
KYC.visualLog('=== KYC clickIdCardMode ===')

KYC.enterPrivacyInfo()
KYC.visualLog('=== KYC enterPrivacyInfo ===')

KYC.selectTypeOfId()
KYC.visualLog('=== KYC selectDriversLicense ===')

KYC.uploadIdImageFile()
KYC.visualLog('=== KYC uploadDriversLicenseFile ===')

KYC.verifyEnteredIdInfo()
KYC.visualLog('=== KYC verifyIdCardInfo ===')

KYC.visualLog('=== TEST SUCCESS ===')

time.sleep(1000)
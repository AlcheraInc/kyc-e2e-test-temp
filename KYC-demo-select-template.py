import KYC
import logging

try :
    """
    신분증 인증 테스트
    """
    KYC.testIdCardMode()
    # KYC.testIdCard_DriversLicenseMode()
    # KYC.testIdCard_PassportMode()
    # KYC.testIdCard_foreignPassportMode()
    # KYC.testIdCard_alienRegistrationMode()

    """
    신분증 인증 | 얼굴확인 테스트
    """
    KYC.testFaceIdMode()

    """
    신분증 인증 | 얼굴확인(라이브니스) 테스트
    """
    KYC.testFaceIdLivenessMode()

    """
    신분증 인증 | 얼굴확인(라이브니스) 테스트 | 계좌 인증
    """
    KYC.testFaceIdLivenessAccountMode()
    
    """
    계좌 인증
    """
    KYC.testAccountMode()

    """
    신분증 인증 | 계좌 인증
    """
    KYC.testIdCardAccountMode()

    """
    신분증 인증 | 얼굴확인 | 계좌 인증
    """
    KYC.testFaceIdAccountMode()

except Exception as e:
    logging.error(e.msg)

KYC.openLogFile()

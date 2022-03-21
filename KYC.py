# -*- coding: utf-8 -*-
import logging
import string
import Const
import os
import sys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (TimeoutException, NoSuchElementException)
from datetime import datetime
from driver import ChromeDriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
if not os.path.exists('./logs'): os.makedirs('./logs')

logFileName = datetime.now().strftime('%Y_%m_%d_%H_%M.log')
file_handler = logging.FileHandler('./logs/' + logFileName)
formatter = logging.Formatter('%(asctime)s - [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# 크롬 브라우저 객체
driver = ChromeDriver().set_driver()

def testIdCardMode(funcOp = 2, idKindOp = 2):
    """
    주민등록증 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    connect(Const.TEST_SITE_URL)
    
    clickTestMode(funcOp)
    visualLog('KYC click Id Card Mode')

    enterPrivacyInfo(idKindOp)
    visualLog('KYC enter Privacy Info')

    selectTypeOfId(idKindOp)
    visualLog('KYC select ID Card')

    uploadIdImageFile(idKindOp)
    visualLog('KYC upload ID Card Image File')

    verifyEnteredIdInfo(idKindOp)
    visualLog('KYC verify Id Card Info')
    
    logResultToFile(sys._getframe().f_code.co_name)
    
    
def testIdCard_DriversLicenseMode(funcOp = 2, idKindOp = 3):
    """
    운전면허증 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    connect(Const.TEST_SITE_URL)

    clickTestMode(funcOp)
    visualLog('KYC click Drivers License Mode')

    enterPrivacyInfo(idKindOp)
    visualLog('KYC enter Privacy Info')

    selectTypeOfId(idKindOp)
    visualLog('KYC select Drivers License')

    uploadIdImageFile(idKindOp)
    visualLog('KYC upload Drivers License File')

    verifyEnteredIdInfo(idKindOp)
    visualLog('KYC verify Drivers License Info')
    
    logResultToFile(sys._getframe().f_code.co_name)

def testIdCard_PassportMode(funcOp = 2, idKindOp = 4):
    """
    한국 여권 검사 자동화 테스트    
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    connect(Const.TEST_SITE_URL)

    clickTestMode(funcOp)
    visualLog('KYC click Passport Mode')

    enterPrivacyInfo(idKindOp)
    visualLog('KYC enter Privacy Info')

    selectTypeOfId(idKindOp)
    visualLog('KYC select Passport')

    uploadIdImageFile(idKindOp)
    visualLog('KYC upload Passport File')

    verifyEnteredIdInfo(idKindOp)
    visualLog('KYC verify Passport Info')
    
    logResultToFile(sys._getframe().f_code.co_name)
    

def testIdCard_foreignPassportMode(funcOp = 2, idKindOp = 5):
    """
    외국 여권 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    connect(Const.TEST_SITE_URL)
    
    clickTestMode(funcOp)
    visualLog('KYC click Foreign Passport Mode')

    enterPrivacyInfo(idKindOp)
    visualLog('KYC enter Privacy Info')

    selectTypeOfId(idKindOp)
    visualLog('KYC select Foreign Passport')

    uploadIdImageFile(idKindOp)
    visualLog('KYC upload Foreign Passport File')

    verifyEnteredIdInfo(idKindOp)
    visualLog('KYC verify Foreign Passport Info')
    
    logResultToFile(sys._getframe().f_code.co_name)
    

def testIdCard_alienRegistrationMode(funcOp = 2, idKindOp = 6):
    """
    외국인등록증 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    connect(Const.TEST_SITE_URL)

    clickTestMode(funcOp)
    visualLog('KYC click Alien Registration Mode')

    enterPrivacyInfo(idKindOp)
    visualLog('KYC enter Privacy Info')

    selectTypeOfId(idKindOp)
    visualLog('KYC select Alien Registration')

    uploadIdImageFile(idKindOp)
    visualLog('KYC upload Alien Registration File')

    verifyEnteredIdInfo(idKindOp)
    visualLog('KYC verify Alien Registration Info')
    
    logResultToFile(sys._getframe().f_code.co_name)


def testFaceIdMode(funcOp = 3, idKindOp = 2):
    """
    신분증 인증 | 얼굴확인 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    testIdCardMode(3,2)
    
    # 얼굴 촬영 버튼 클릭
    faceShootBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, Const.TAKE_SELFIE_XPATH)
        )
    )
    faceShootBtn.click()
    
    # because chrome_options.add_argument('--use-fake-ui-for-media-stream')
    logger.info('Access Camera Auth Alert Pass.')
    
    # Execute JavaScript 예시
    # driver.execute_script("alert('[KYC Auto Test] 얼굴을 인식해주세요.')")
    # # Alert 확인을 누를 때까지 대기
    # WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(alert_is_not_present())
    
    # '화면 영역 안으로 얼굴을 맞춰주세요.' 얼굴인식 화면이 사라질때까지 기다리는 코드.
    WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(
        EC.invisibility_of_element(
            (By.XPATH, Const.FACE_RECOGNITION_TEXT_XPATH)
        )
    )
    
    # 이거는 마지막 성공화면이 뜰때까지 기다리는 코드.
    # '본인 인증 완료'
    WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, Const.COMPLETED_CERFIFICATION_TEXT_XPATH), 
            Const.COMPLETED_CERFIFICATION_TEXT
        )
    )
    
    # 성공 여부 체크
    result = None
    successText = driver.find_element(By.XPATH, Const.COMPLETED_CERFIFICATION_TEXT_XPATH)
    if successText.text == Const.COMPLETED_CERFIFICATION_TEXT:
        result = Const.SUCCESS
    else:
        logger.info('unexcepted message: ' + successText.text)
        result = Const.FAILED
    
    logResultToFile(sys._getframe().f_code.co_name)


def testFaceIdLivenessMode(funcOp = 4, idKindOp = 2):
    """
    신분증 인증 | 얼굴확인 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    testIdCardMode(4,2)
    
    # 얼굴 촬영 버튼 클릭
    faceShootBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, Const.TAKE_SELFIE_XPATH)
        )
    )
    faceShootBtn.click()
    
    # because chrome_options.add_argument('--use-fake-ui-for-media-stream')
    logger.info('Camera auth alert passed.')
    
    # Execute JavaScript 예시
    # driver.execute_script("alert('[KYC Auto Test] 얼굴을 인식해주세요.')")
    # # Alert 확인을 누를 때까지 대기
    # WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(alert_is_not_present())
    
    # '화면 영역 안으로 얼굴을 맞춰주세요.' 얼굴인식 화면이 사라질때까지 기다리는 코드.
    WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(
        EC.invisibility_of_element(
            (By.XPATH, Const.FACE_RECOGNITION_TEXT_XPATH)
        )
    )
    
    try:
        # 이거는 마지막 성공화면이 뜰때까지 기다리는 코드.
        # '본인 인증 완료'
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, Const.COMPLETED_CERFIFICATION_TEXT_XPATH), 
                Const.COMPLETED_CERFIFICATION_TEXT
            )
        )
        
        # 성공 여부 체크
        result = None
        successText = driver.find_element(By.XPATH, Const.COMPLETED_CERFIFICATION_TEXT_XPATH)
        if successText.text == Const.COMPLETED_CERFIFICATION_TEXT:
            result = Const.SUCCESS
        else:
            logger.info('unexcepted message: ' + successText.text)
            result = Const.FAILED
            
    except (TimeoutException):
        # 성공 메시지를 찾지 못하면 실패로 간주하고 진행
        try:
            # '얼굴 인증 실패'
            failText = driver.find_element(By.XPATH, Const.FAILED_CERFIFICATION_TEXT_XPATH)
            if failText.text == Const.FAILED_CERFIFICATION_TEXT:
                errorCode = driver.find_element(By.XPATH, Const.FAILED_CERFIFICATION_ERROR_CODE_XPATH)
                logger.info(errorCode.text)
                result = Const.FAILED
        
        except (Exception):
            # '얼굴 감지 실패'
            vCardErrorTitle = driver.find_element(By.XPATH, Const.FAILED_CERFIFICATION_VCARD_ERROR_CODE_TITLE_XPATH)
            vCardErrorcode = driver.find_element(By.XPATH, Const.FAILED_CERFIFICATION_VCARD_ERROR_CODE_XPATH)
            logger.error(vCardErrorTitle.text + ": " + vCardErrorcode.text)
            result = Const.FAILED
        
    logResultToFile(sys._getframe().f_code.co_name)
    
def testAccountMode(funcOp = 6, idKindOp = 2):
    """
    신분증 인증 | 얼굴확인 검사 자동화 테스트
    
    인증 기능 funcOp
        2: 신분증 인증
        3: 신분증 인증 | 얼굴확인 
        4: 신분증 인증 | 얼굴확인(+라이브니스)
        5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
        6: 계좌 인증
        7: 신분증 인증 | 계좌 인증
        8: 신분증 인증 | 얼굴확인 | 계좌 인증
        
    신분증 종류 idKindOp
        2: 주민등록증
        3: 운전면허증
        4: 한국 여권
        5: 외국 여권
        6: 외국인등록증
    """
    
    connect(Const.TEST_SITE_URL)
    
    clickTestMode(funcOp)
    visualLog('KYC click Account Mode')

    enterPrivacyInfo(idKindOp)
    visualLog('KYC enter Privacy Info')
    
    # 계좌 입력 버튼 클릭
    enterAccountBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, Const.ENTER_ACCOUNT_BUTTON_XPATH)
        )
    )
    enterAccountBtn.click()

    # 계좌인증 화면이 뜰때까지 기다리는 코드.
    WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, Const.VERIFICATION_ACCOUNT_TEXT_XPATH), 
                Const.VERIFICATION_ACCOUNT_TEXT
            )
        )
    
    # 은행/증권사 선택 로직
    # 은행이 Default 이므로, 입력한 BANK_NAME 을 은행명 목록과 비교하고,
    # 은행명이 아닌경우 증권사명 목록과 비교하여 정보를 입력하는 로직.
    bankNStockSelectBtn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, Const.SELECT_BANK_N_STOCK_XPATH)
        )
    )
    bankNStockSelectBtn.click()
    banklist = driver.find_elements(By.XPATH, Const.BANK_LIST_ITEM_XPATH)
    
    visualLog(f'banklist length is {len(banklist)}')
    bankItem = isContainText(Const.BANK_NAME, banklist)
    
    if bankItem:
        bankItem.click()
    else:
        driver.find_element(By.XPATH, Const.STOCK_TAB_XPATH).click()
        stocklist = driver.find_elements(By.XPATH, Const.BANK_LIST_ITEM_XPATH)
        # 은행 목록을 얻은 후, 증권사 탭을 눌러, 증권사 목록을 얻을 때, 
        # list[은행 목록 수 + 증권사 목록 수] 되어 반환되는 듯한 현상으로 인해 필터링하는 코드.
        stocklist = [stock for stock in stocklist if stock.text != '']
        
        visualLog(f'stocklist length is {len(stocklist)}')
        stockItem = isContainText(Const.BANK_NAME, stocklist)
        
        if stockItem:
            stockItem.click()
        else:
            raise Exception(Const.BANK_NAME + '은 은행명/증권사명 목록에 없습니다. 다시 확인 후 값을 수정하고 시도해주세요.')
            
    # 이 방식은 안됨
    # driver.execute_script("arguments[0].innerHTML = ' KB국민 '", bankNStockSelectBtn)
    
    # 계좌번호 입력
    nameTextField = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Const.ENTER_ACCOUNT_NUMBER_XPATH)))
    nameTextField.send_keys(Const.ACCOUNT_NUMBER)
    
    
    oneWonSendBtn = driver.find_element(By.XPATH, Const.SEND_ONE_WON_BUTTON_XPATH)
    oneWonSendBtn.click()
    
    # 5분 내로 인증 번호 4자리 입력하는 로직 구현.
    
    print()

    
def connect(url):
    """
    # MAIN 페이지
    """
    
    visualLog(sys._getframe().f_code.co_name)
    
    # 페이지 가져오기 (접속)
    driver.get(url)
    logger.info(url)

    # 화면 크기 지정
    # Windows Xbox Record로 녹화하려면 창 크기 변경 후, 녹화를 시작해야 한다.
    driver.set_window_rect(0, 0, 1000, 1000)  # 특정 좌표(x,y)와 크기(width,height)로 변경

    # Debug Window 설정 여부 버튼
    postMsgToggleBtn = driver.find_element(
        By.XPATH, Const.POST_MSG_TOGGLE_BUTTON_XPATH)
    postMsgToggleBtn.click()

    # 개인정보 옵션 체크박스
    privacyOpCheckBtn = driver.find_element(
        By.XPATH, Const.PRIVACY_OPTION_CHECK_XPATH)
    privacyOpCheckBtn.click()


def clickTestMode(funcOp):
    """
    2: 신분증 인증
    3: 신분증 인증 | 얼굴확인 
    4: 신분증 인증 | 얼굴확인(+라이브니스)
    5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
    6: 계좌 인증
    7: 신분증 인증 | 계좌 인증
    8: 신분증 인증 | 얼굴확인 | 계좌 인증
    """
    
    if driver:
        xPath = {
        2: r'//*[@id="logic-options"]/ul/li[1]/img',
        3: r'//*[@id="logic-options"]/ul/li[2]/img',
        4: r'//*[@id="logic-options"]/ul/li[3]/img',
        5: r'//*[@id="logic-options"]/ul/li[4]/img',
        6: r'//*[@id="logic-options"]/ul/li[5]/img',
        7: r'//*[@id="logic-options"]/ul/li[6]/img',
        8: r'//*[@id="logic-options"]/ul/li[7]/img'
        }.get(funcOp, "없는 메뉴")
        
        # 테스트할 기능 버튼
        targetBtn = driver.find_element(By.XPATH, xPath)
        targetBtn.click()

    else:
        logger.info('Please call connect() first.')

    func = {
        2: '신분증 인증',
        3: '신분증 인증 | 얼굴확인',
        4: '신분증 인증 | 얼굴확인(+라이브니스)',
        5: '신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증',
        6: '계좌 인증',
        7: '신분증 인증 | 계좌 인증',
        8: '신분증 인증 | 얼굴확인 | 계좌 인증'
        }.get(funcOp, "없는 메뉴")
    
    logger.info(f'선택한 메뉴는 {func} 입니다.')


def enterPrivacyInfo(idKindOp):
    """
    # 개인정보 입력 페이지
    """
    
    if driver:
        # 개인정보 입력 페이지는 iframe 으로 옮겨서 검사해야 코드로 접근이 가능함
        kycIframe = driver.find_element(By.CSS_SELECTOR, 'iframe')

        if kycIframe:
            iframeId = kycIframe.get_attribute('id')

            if(iframeId == Const.KYC_IFRAME_TEXT):
                driver.switch_to.frame(kycIframe)

                # driver.implicitly_wait(5)  # 묵시적 대기, 활성화를 주어진 시간만큼까지 기다린다.
                # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
                nameTextField = WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(EC.element_to_be_clickable((By.XPATH, getNameInputXPath(idKindOp))))
                nameTextField.send_keys(getUserName(idKindOp))
                
                phoneTextField = driver.find_element(By.XPATH, getPhoneInputXPath(idKindOp))
                phoneTextField.send_keys(Const.USER_PHONE)

                birthTextField = driver.find_element(By.XPATH, getBirthInputXPath(idKindOp))
                birthTextField.send_keys(getUserBirth(idKindOp))

                emailTextField = driver.find_element(By.XPATH, getEmailInputXPath(idKindOp))
                emailTextField.send_keys(Const.USER_EMAIL)

                # 다음 버튼 클릭
                nextBtn = driver.find_element(By.XPATH, Const.NEXT_BUTTON_XPATH)
                nextBtn.click()
            
            else:
                logger.info('The iframe id is incorrect. Expected: "kyc_iframe" Actual: ', iframeId)

    else:
        logger.info('Please call connect() first.')


def selectTypeOfId(idKindOp):
    """
    # 신분증 메뉴 선택 페이지
    """
    
    if driver:
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
        choiceIdBtn = WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(EC.element_to_be_clickable((By.XPATH, getSelectTypeOfIdXPath(idKindOp))))
        # choiceIdBtn = driver.find_element(By.XPATH, getSelectTypeOfIdXPath(idKindOp))
        choiceIdBtn.click()
        
        nextBtn = driver.find_element(By.XPATH, Const.SELECT_COMPLETE_BUTTON_XPATH)
        nextBtn.click()

    else:
        logger.info('Please call connect() first.')


def uploadIdImageFile(idKindOp):
    """
    # 신분증 사진 업로드 페이지
    """
    
    if driver:
        #UPLOAD_IMAGE_BUTTON_XPATH 는 input type file 로 따로 잡아서 사용
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(getIdImageFilePath(idKindOp))
        
        submitIdBtn = driver.find_element(By.XPATH, Const.SUBMIT_ID_BUTTON_XPATH)
        submitIdBtn.click()
        
        driver.switch_to.active_element
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
        submitBtn = WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(EC.element_to_be_clickable((By.XPATH, Const.SUBMIT_BUTTON_XPATH)))
        submitBtn.click()
    else:
        logger.info('Please call connect() first.')


def verifyEnteredIdInfo(idKindOp):
    """
    # 개인정보 확인 페이지
    """
    
    try:
        if driver:
            # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
            nextBtn = WebDriverWait(driver, Const.TIMEOUT_ONE_MINUTE).until(EC.element_to_be_clickable((By.XPATH, getVerifyIdInfoPageNextBtnXPath(idKindOp))))
            nextBtn.click()
            
            byTxt = By.CLASS_NAME
            targetTxt = 'v-card'
            
            # v-card 가 표시되면 진행 중 오류가 발생한 것으로 간주.
            if existsElement(byTxt, targetTxt):
                raise Exception(driver.find_element(byTxt, targetTxt))
        else:
            raise Exception('Please call connect() first.')
    
    except Exception as e:
        if e.args.__len__() > 0 and isinstance(e.args[0], WebElement):
            logger.error(str(e.args[0].text))
        else :
            logger.error(str(e))
        
        raise e


def getNameInputXPath(funcOpNum):
    xPath = {
        2: r'//*[@id="app"]/div[1]/div/div[4]/div/input',
        3: r'//*[@id="app"]/div[1]/div/div[4]/div/input',
        4: r'//*[@id="app"]/div[1]/div/div[4]/div/input',
        5: r'//*[@id="app"]/div[1]/div/div[4]/div/input',
        6: r'//*[@id="app"]/div[1]/div/div[4]/div/input'
        }.get(funcOpNum, "없는 메뉴")
    
    return xPath


def getPhoneInputXPath(funcOpNum):
    xPath = {
        2: r'//*[@id="app"]/div[1]/div/div[6]/div/input',
        3: r'//*[@id="app"]/div[1]/div/div[6]/div/input',
        4: r'//*[@id="app"]/div[1]/div/div[6]/div/input',
        5: r'//*[@id="app"]/div[1]/div/div[6]/div/input',
        6: r'//*[@id="app"]/div[1]/div/div[6]/div/input'
        }.get(funcOpNum, "없는 메뉴")
    
    return xPath


def getBirthInputXPath(funcOpNum):
    xPath = {
        2: r'//*[@id="app"]/div[1]/div/div[8]/div/input',
        3: r'//*[@id="app"]/div[1]/div/div[8]/div/input',
        4: r'//*[@id="app"]/div[1]/div/div[8]/div/input',
        5: r'//*[@id="app"]/div[1]/div/div[8]/div/input',
        6: r'//*[@id="app"]/div[1]/div/div[8]/div/input'
        }.get(funcOpNum, "없는 메뉴")
    
    return xPath


def getEmailInputXPath(funcOpNum):
    xPath = {
        2: r'//*[@id="app"]/div/div/div[10]/div/input', 
        3: r'//*[@id="app"]/div/div/div[10]/div/input', 
        4: r'//*[@id="app"]/div/div/div[10]/div/input',
        5: r'//*[@id="app"]/div/div/div[10]/div/input',
        6: r'//*[@id="app"]/div/div/div[10]/div/input'
        }.get(funcOpNum, "없는 메뉴")
    
    return xPath


def getSelectTypeOfIdXPath(idKindOpNum):
    """
    신분증 종류 번호 [2 ~ 6]
    2: 주민등록증
    3: 운전면허증
    4: 한국 여권
    5: 외국 여권
    6: 외국인등록증
    """
    
    xPath = {
        2: r'//*[@id="app"]/div[1]/div/div/div[5]',
        3: r'//*[@id="app"]/div[1]/div/div/div[6]',
        4: r'//*[@id="app"]/div[1]/div/div/div[7]',
        5: r'//*[@id="app"]/div[1]/div/div/div[8]',
        6: r'//*[@id="app"]/div[1]/div/div/div[9]'
        }.get(idKindOpNum, "없는 메뉴")

    func = {
        2: '주민등록증',
        3: '운전면허증',
        4: '한국 여권',
        5: '외국 여권',
        6: '외국인등록증'
        }.get(idKindOpNum, "없는 메뉴")
    
    logger.info(f'선택한 신분증 종류는 {func} 입니다.')
    
    return xPath


def getIdImageFilePath(idKindOpNum):
    filePath = {
        2: 'C:\\idCard.jpg',
        3: 'C:\\driversLicense.jpg',
        4: 'C:\\passPort.jpg',
        5: 'C:\\foreignPassPort.jpg',
        6: 'C:\\alienRegistrationCard.jpg'
        }.get(idKindOpNum, "없는 메뉴")
    
    return filePath

def getVerifyIdInfoPageNextBtnXPath(idKindOpNum):
    """
    신분증 정보 확인 페이지
    """
    
    xPath = {
        2: r'//*[@id="app"]/div[1]/div/div[12]/div[2]',
        3: r'//*[@id="app"]/div[1]/div/div[14]/div[2]',
        4: r'//*[@id="app"]/div[1]/div/div[16]/div[2]',
        5: r'//*[@id="app"]/div[1]/div/div[14]/div[2]',
        6: r'//*[@id="app"]/div[1]/div/div[12]/div[2]'
        }.get(idKindOpNum, "없는 메뉴")
    
    return xPath


def getUserName(funcOpNum):
    xPath = {
        2: Const.USER_NAME,
        3: Const.USER_NAME,
        4: Const.PASSPORT_USER_NAME,
        5: Const.FOREIGN_USER_NAME,
        6: Const.REGISTERED_FOREIGN_USER_NAME
        }.get(funcOpNum, "없는 메뉴")
    
    return xPath


def getUserBirth(funcOpNum):
    xPath = {
        2: Const.USER_BIRTH,
        3: Const.USER_BIRTH,
        4: Const.PASSPORT_USER_BIRTH,
        5: Const.FOREIGN_USER_BIRTH,
        6: Const.REGISTERED_FOREIGN_USER_BIRTH
        }.get(funcOpNum, "없는 메뉴")
    
    return xPath

def visualLog(contents):
    """
    로그 파일에서 눈에 잘 띄게 contents를 남기는 함수\n
    ────\n
    connect\n
    ────\n

    Args:
        contents (str): 로그 파일에 작성될 내용
    """
    
    horizontalChr = '─'
    horizontalStr = ''
    
    for i in range(len(contents)):
        horizontalStr += horizontalChr

    logger.info(horizontalChr + horizontalStr + horizontalChr)
    logger.info(contents)
    logger.info(horizontalChr + horizontalStr + horizontalChr)


def logResultToFile(funcName, loggingStartWord = '"review_result"'):
    """
    : 한줄로 전체 내용이 넘어오는 review_result 파싱 결과를
    : 다음과 같이 User Readerable한 형태로 로그파일에 추가

    Args:
        funcName (str): 호출하는 함수명을 입력받기 위해 sys._getframe().f_code.co_name 을 입력하여 사용.
        loggingStartWord (str, optional): 기록을 시작할 위치를 나타내는 문자열.
        : Defaults to '"review_result"'. ex) 'WORD'
        : 문자열을 변경할때는 apostrophe 내부에 작성해야 한다.
    
    Result:
        "review_result":{"id":578
        "request_time":"2022-03-10T04:12:10.699Z"
        "name":"사용자명"
        "phone_number":"사용자번호"
        "birthday":"생년월일"
        "result_type":1
        "result_email":1
        "result_sms":2
        "module":{"id_card_ocr":true
        "id_card_verification":true
        "face_authentication":false
        "account_verification":false
        "liveness":false}
        "id_card":{"modified":false
        "verified":true
        "id_card_image":"/9j/4AAQSkZJRgABAQEAYABgAAD//gA+Q1JFQVRPUj...생략
        "id_crop_image":null
        "original_ocr_data":"{\"idType\":\"1\"
        \"userName\":\"사용자명\"
        \"juminNo1\":\"주민등록번호 앞자리\"
        \"juminNo2\":\"주민등록번호 뒷자리\"
        \"_juminNo2\":\"2******\"
        \"issueDate\":\"발급일자\"
        \"transaction_id\":\"125978368062297a9ca145e1646885532\"}"
        "modified_ocr_data":null
        "is_manual_input":false
        "is_uploaded":true
        "id_card_origin":"/9j/4AAQSkZJRgABAQAAAQABAAD/4gIoSUNDX1BST...생략
        "face_check":null
        "account":null}
        "api_response":{"result_code":"N100"
        "result_message":"결과 메시지"}
        "result":"성공 여부"}"
    """
    try:
        # 'goog:loggingPrefs'
        prefName = 'browser'
        
        logger.info(prefName + ': Logging start.')
        resultTargetWord = '"result":'
        result = ''
        
        # 너무 빨리 얻어와서 값이 없는 경우 대비하는 코드
        while True:
            perf = driver.get_log(prefName)
            if len(perf) > 2: break
        
        for p in perf:
            # Readerable한 형태로 만들기 위한 replace 순서가 있음
            strLog = p['message'].replace(',"', ',\n"').replace('\\"', '"').replace('\\\\', '\\')
            
            if loggingStartWord in strLog:
                splited = strLog[
                    strLog.index(loggingStartWord):
                                ].split(",")
                for x in splited:
                    for y in x.split(","):
                        if resultTargetWord in y:
                            # 수행 결과 단어를 필터하기 위한 split 코드
                            result = y[len(resultTargetWord) + 1:len(y) - 3]
                        logger.info(y)
                        
        visualLog(funcName + ' ' + result)
                            
    except (Exception)as e:
        logger.info(prefName + ': Empty.')

def existsElement(by: By, target: string):
    try:
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((by, target)))
    
    except (TimeoutException, NoSuchElementException) as e:
        return False
    
    return True

def isContainText(target: string, list):
    """
    target 문자열을 포함하는 text attribute를 가지는 항목이 
    list element 중에 존재하는 지 검사한다.

    Args:
        target (string): 검사할 문자열
        list (Any): 'text' attribute를 가지는 element list

    Returns:
        list에 target 문자열이 포함되어 있는 element, 아닌 경우 False
    """
    for item in list:
        if hasattr(item,'text'):
            if target in item.text:
                return item
        else:
            logger.error(target + ' : comparison target has no "text" attribute.')
            break
    
    return False
            

class alert_is_not_present(object):
    """ 
    Expect an alert to not to be present.
    usage: WebDriverWait(driver, 1).until(alert_is_not_present())
    """
    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True
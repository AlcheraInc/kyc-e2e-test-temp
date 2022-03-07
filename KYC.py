import logging
import string
import Const
import os
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
    logging.info('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.info('=== KYC click Id Card Mode ===')

    enterPrivacyInfo(idKindOp)
    logging.info('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.info('=== KYC select ID Card ===')

    uploadIdImageFile(idKindOp)
    logging.info('=== KYC upload ID Card Image File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.info('=== KYC verify Id Card Info ===')
     
    perf = driver.get_log('driver')
    # perf type is List, p type is Dict
    for p in perf:
        if 'review_result' in p['message']:
            logging.info(
                p['message']
                .replace('\\"', '"')
                .replace(',"', ',\n"')
            )
            break

    logging.info('==============================')
    logging.info('=== testIdCardMode SUCCESS ===')
    logging.info('==============================')
    
    
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
    logging.info('=== KYC connect ===')    

    clickTestMode(funcOp)
    logging.info('=== KYC click Drivers License Mode ===')

    enterPrivacyInfo(idKindOp)
    logging.info('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.info('=== KYC select Drivers License ===')

    uploadIdImageFile(idKindOp)
    logging.info('=== KYC upload Drivers License File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.info('=== KYC verify Drivers License Info ===')

    logging.info('=============================================')
    logging.info('=== testIdCard_DriversLicenseMode SUCCESS ===')
    logging.info('=============================================')

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
    logging.info('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.info('=== KYC click Passport Mode ===')

    enterPrivacyInfo(idKindOp)
    logging.info('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.info('=== KYC select Passport ===')

    uploadIdImageFile(idKindOp)
    logging.info('=== KYC upload Passport File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.info('=== KYC verify Passport Info ===')

    logging.info('=======================================')
    logging.info('=== testIdCard_PassportMode SUCCESS ===')
    logging.info('=======================================')
    

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
    logging.info('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.info('=== KYC click Foreign Passport Mode ===')

    enterPrivacyInfo(idKindOp)
    logging.info('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.info('=== KYC select Foreign Passport ===')

    uploadIdImageFile(idKindOp)
    logging.info('=== KYC upload Foreign Passport File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.info('=== KYC verify Foreign Passport Info ===')

    logging.info('==============================================')
    logging.info('=== testIdCard_foreignPassportMode SUCCESS ===')
    logging.info('==============================================')
    

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
    logging.info('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.info('=== KYC click Alien Registration Mode ===')

    enterPrivacyInfo(idKindOp)
    logging.info('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.info('=== KYC select Alien Registration ===')

    uploadIdImageFile(idKindOp)
    logging.info('=== KYC upload Alien Registration File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.info('=== KYC verify Alien Registration Info ===')

    logging.info('================================================')
    logging.info('=== testIdCard_alienRegistrationMode SUCCESS ===')
    logging.info('================================================')


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
    
    logging.info('==============================')
    logging.info('=== testFaceIdMode ' + result + ' ===')
    logging.info('==============================')


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
            vCardErrorTitle = driver.find_element(By.XPATH, Const.FAILED_CERFIFICATION_ERROR_CODE_VCARD_TITLE_XPATH)
            vCardErrorcode = driver.find_element(By.XPATH, Const.FAILED_CERFIFICATION_VCARD_ERROR_CODE_XPATH)
            logger.error(vCardErrorTitle.text + ": " + vCardErrorcode.text)
            result = Const.FAILED
        
    logging.info('==============================')
    logging.info('=== testFaceIdMode ' + result + ' ===')
    logging.info('==============================')
    
def connect(url):
    """
    # MAIN 페이지
    """
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
        logging.info('Please call connect() first.')

    func = {
        2: '신분증 인증',
        3: '신분증 인증 | 얼굴확인',
        4: '신분증 인증 | 얼굴확인(+라이브니스)',
        5: '신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증',
        6: '계좌 인증',
        7: '신분증 인증 | 계좌 인증',
        8: '신분증 인증 | 얼굴확인 | 계좌 인증'
        }.get(funcOp, "없는 메뉴")
    
    logging.info(f'선택한 메뉴는 {func} 입니다.')


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
                nameTextField = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, getNameInputXPath(idKindOp))))
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
                logging.info('The iframe id is incorrect. Expected: "kyc_iframe" Actual: ', iframeId)

    else:
        logging.info('Please call connect() first.')


def selectTypeOfId(idKindOp):
    """
    # 신분증 메뉴 선택 페이지
    """
    
    if driver:
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
        choiceIdBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, getSelectTypeOfIdXPath(idKindOp))))
        # choiceIdBtn = driver.find_element(By.XPATH, getSelectTypeOfIdXPath(idKindOp))
        choiceIdBtn.click()
        
        nextBtn = driver.find_element(By.XPATH, Const.SELECT_COMPLETE_BUTTON_XPATH)
        nextBtn.click()

    else:
        logging.info('Please call connect() first.')


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
        submitBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, Const.SUBMIT_BUTTON_XPATH)))
        submitBtn.click()
    else:
        logging.info('Please call connect() first.')


def verifyEnteredIdInfo(idKindOp):
    """
    # 개인정보 확인 페이지
    """
    
    try:
        if driver:
            # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
            nextBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, getVerifyIdInfoPageNextBtnXPath(idKindOp))))
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
    
    logging.info(f'선택한 신분증 종류는 {func} 입니다.')
    
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

def existsElement(by: By, target: string):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, target)))
    
    except (TimeoutException, NoSuchElementException) as e:
        return False
    
    return True


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
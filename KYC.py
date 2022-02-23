import logging
from driver import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Const

logging.basicConfig(level=logging.DEBUG, format="'%(asctime)s - [%(filename)s:%(lineno)d][KYC LOG] %(message)s'") 

# 크롬 브라우저 객체
driver = ChromeDriver().set_driver()

"""
주민등록증 검사 자동화 테스트
"""
def testIdCardMode():
    
    # 인증 기능 번호 [2 ~ 8]
    funcOp = 2
    # 신분증 종류 번호 [2 ~ 6]
    idKindOp = 2
    
    connect(Const.TEST_SITE_URL)
    logging.debug('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.debug('=== KYC click Id Card Mode ===')

    enterPrivacyInfo(funcOp)
    logging.debug('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.debug('=== KYC select ID Card ===')

    uploadIdImageFile(idKindOp)
    logging.debug('=== KYC upload ID Card Image File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.debug('=== KYC verify Id Card Info ===')
    
"""
운전면허증 검사 자동화 테스트
"""
def testIdCard_DriversLicenseMode():
    
    # 인증 기능 번호 [2 ~ 8]
    funcOp = 2
    # 신분증 종류 번호 [2 ~ 6]
    idKindOp = 3
    
    connect(Const.TEST_SITE_URL)
    logging.debug('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.debug('=== KYC click Drivers License Mode ===')

    enterPrivacyInfo(funcOp)
    logging.debug('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.debug('=== KYC select Drivers License ===')

    uploadIdImageFile(idKindOp)
    logging.debug('=== KYC upload Drivers License File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.debug('=== KYC verify Drivers License Info ===')

"""
한국 여권 검사 자동화 테스트
"""
def testIdCard_PassportMode():
    
    # 인증 기능 번호 [2 ~ 8]
    funcOp = 2
    # 신분증 종류 번호 [2 ~ 6]
    idKindOp = 4
    
    connect(Const.TEST_SITE_URL)
    logging.debug('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.debug('=== KYC click Passport Mode ===')

    enterPrivacyInfo(funcOp)
    logging.debug('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.debug('=== KYC select Passport ===')

    uploadIdImageFile(idKindOp)
    logging.debug('=== KYC upload Passport File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.debug('=== KYC verify Passport Info ===')
    

"""
외국 여권 검사 자동화 테스트
"""
def testIdCard_foreignPassportMode():
    
    # 인증 기능 번호 [2 ~ 8]
    funcOp = 2
    # 신분증 종류 번호 [2 ~ 6]
    idKindOp = 5
    
    connect(Const.TEST_SITE_URL)
    logging.debug('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.debug('=== KYC click Foreign Passport Mode ===')

    enterPrivacyInfo(funcOp)
    logging.debug('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.debug('=== KYC select Foreign Passport ===')

    uploadIdImageFile(idKindOp)
    logging.debug('=== KYC upload Foreign Passport File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.debug('=== KYC verify Foreign Passport Info ===')
    

"""
외국인등록증 검사 자동화 테스트
"""
def testIdCard_alienRegistrationMode():
    
    # 인증 기능 번호 [2 ~ 8]
    funcOp = 2
    # 신분증 종류 번호 [2 ~ 6]
    idKindOp = 6
    
    connect(Const.TEST_SITE_URL)
    logging.debug('=== KYC connect ===')

    clickTestMode(funcOp)
    logging.debug('=== KYC click Alien Registration Mode ===')

    enterPrivacyInfo(funcOp)
    logging.debug('=== KYC enter Privacy Info ===')

    selectTypeOfId(idKindOp)
    logging.debug('=== KYC select Alien Registration ===')

    uploadIdImageFile(idKindOp)
    logging.debug('=== KYC upload Alien Registration File ===')

    verifyEnteredIdInfo(idKindOp)
    logging.debug('=== KYC verify Alien Registration Info ===')
    

"""
# MAIN 페이지
"""
def connect(url):
    # 페이지 가져오기 (접속)
    driver.get(url)

    # 화면 크기 지정
    driver.set_window_rect(0, 0, 1680, 990)  # 특정 좌표(x,y)와 크기(width,height)로 변경

    # Debug Window 설정 여부 버튼
    postMsgToggleBtn = driver.find_element(
        By.XPATH, Const.POST_MSG_TOGGLE_BUTTON_XPATH)
    postMsgToggleBtn.click()

    # 개인정보 옵션 체크박스
    privacyOpCheckBtn = driver.find_element(
        By.XPATH, Const.PRIVACY_OPTION_CHECK_XPATH)
    privacyOpCheckBtn.click()


"""
2: 신분증 인증
3: 신분증 인증 | 얼굴확인 
4: 신분증 인증 | 얼굴확인(+라이브니스)
5: 신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증
6: 계좌 인증
7: 신분증 인증 | 계좌 인증
8: 신분증 인증 | 얼굴확인 | 계좌 인증
"""
def clickTestMode(funcOp):
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
        logging.debug('Please call connect() first.')

    func = {
        2: '신분증 인증',
        3: '신분증 인증 | 얼굴확인',
        4: '신분증 인증 | 얼굴확인(+라이브니스)',
        5: '신분증 인증 | 얼굴확인(+라이브니스) | 계좌 인증',
        6: '계좌 인증',
        7: '신분증 인증 | 계좌 인증',
        8: '신분증 인증 | 얼굴확인 | 계좌 인증'
        }.get(funcOp, "없는 메뉴")
    
    logging.debug(f'선택한 메뉴는 {func} 입니다.')


"""
# 개인정보 입력 페이지
"""
def enterPrivacyInfo(funcOp):
    if driver:
        # 개인정보 입력 페이지는 iframe 으로 옮겨서 검사해야 코드로 접근이 가능함
        kycIframe = driver.find_element(By.CSS_SELECTOR, 'iframe')

        if kycIframe:
            iframeId = kycIframe.get_attribute('id')

            if(iframeId == Const.KYC_IFRAME_TEXT):
                driver.switch_to.frame(kycIframe)

                # driver.implicitly_wait(5)  # 묵시적 대기, 활성화를 주어진 시간만큼까지 기다린다.
                # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
                nameTextField = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, getNameInputXPath(funcOp))))
                nameTextField.send_keys(Const.USER_NAME)

                phoneTextField = driver.find_element(By.XPATH, getPhoneInputXPath(funcOp))
                phoneTextField.send_keys(Const.USER_PHONE)

                birthTextField = driver.find_element(By.XPATH, getBirthInputXPath(funcOp))
                birthTextField.send_keys(Const.USER_BIRTH)

                emailTextField = driver.find_element(By.XPATH, getEmailInputXPath(funcOp))
                emailTextField.send_keys(Const.USER_EMAIL)

                # 다음 버튼 클릭
                nextBtn = driver.find_element(By.XPATH, Const.NEXT_BUTTON_XPATH)
                nextBtn.click()
            
            else:
                logging.debug('The iframe id is incorrect. Expected: "kyc_iframe" Actual: ', iframeId)

    else:
        logging.debug('Please call connect() first.')


"""
# 신분증 메뉴 선택 페이지
"""
def selectTypeOfId(idKindOp):
    if driver:
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
        choiceIdBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, getSelectTypeOfIdXPath(idKindOp))))
        # choiceIdBtn = driver.find_element(By.XPATH, getSelectTypeOfIdXPath(idKindOp))
        choiceIdBtn.click()
        
        nextBtn = driver.find_element(By.XPATH, Const.SELECT_COMPLETE_BUTTON_XPATH)
        nextBtn.click()

    else:
        logging.debug('Please call connect() first.')


"""
# 신분증 사진 업로드 페이지
"""
def uploadIdImageFile(idKindOp):
    if driver:
        #UPLOAD_IMAGE_BUTTON_XPATH 는 input type file 로 따로 잡아서 사용
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(getIdImageFilePath(idKindOp))
        
        submitIdBtn = driver.find_element(By.XPATH, Const.SUBMIT_ID_BUTTON_XPATH)
        submitIdBtn.click()
        
        element = driver.switch_to.active_element
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
        submitBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, Const.SUBMIT_BUTTON_XPATH)))
        submitBtn.click()
    else:
        logging.debug('Please call connect() first.')


"""
# 개인정보 확인 페이지
"""
def verifyEnteredIdInfo(idKindOp):
    if driver:
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 주어진 시간만큼 기다린다.
        nextBtn = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, getVerifyIdInfoPageNextBtnXPath(idKindOp))))
        nextBtn.click()
    else:
        logging.debug('Please call connect(getNameInputXPath(funcOpNum)) first.')


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


"""
신분증 종류 번호 [2 ~ 6]
2: 주민등록증
3: 운전면허증
4: 한국 여권
5: 외국 여권
6: 외국인등록증
"""
def getSelectTypeOfIdXPath(idKindOpNum):
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
    
    logging.debug(f'선택한 신분증 종류는 {func} 입니다.')
    
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

"""
신분증 정보 확인 페이지
"""
def getVerifyIdInfoPageNextBtnXPath(idKindOpNum):
    xPath = {
        2: r'//*[@id="app"]/div[1]/div/div[12]/div[2]',
        3: r'//*[@id="app"]/div[1]/div/div[14]/div[2]',
        4: r'//*[@id="app"]/div[1]/div/div[16]/div[2]',
        5: r'//*[@id="app"]/div[1]/div/div[18]/div[2]',
        6: r'//*[@id="app"]/div[1]/div/div[20]/div[2]'
        }.get(idKindOpNum, "없는 메뉴")
    
    return xPath





# def switch(funcOpNum):
#     function = {2: "신분증 인증", 3: "신분증 인증 & 얼굴확인",
#                 4: "신분증 인증 & 얼굴확인(+라이브니스)"}.get(funcOpNum, "없는 메뉴")
#     logging.debug(f'선택한 메뉴는 {function} 입니다.')

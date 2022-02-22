"""
운전면허증 인증 자동화
"""

import time
from xml.dom.minidom import Element
from driver import ChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import WebDriverWait
import Const


TEST_SITE_URL = Const.TEST_SITE_URL

# 인증 종류 선택 페이지
POST_MSG_TOGGLE_BUTTON_XPATH = Const.POST_MSG_TOGGLE_BUTTON_XPATH
PRIVACY_OPTION_CHECK_XPATH   = Const.PRIVACY_OPTION_CHECK_XPATH
# 신분증 인증
CERTIFICATE_ID_BUTTON_XPATH  = Const.CERTIFICATE_ID_BUTTON_XPATH

# 정보 입력 페이지
NAME_INPUT_XPATH             = Const.NAME_INPUT_XPATH
PHONE_INPUT_XPATH            = Const.PHONE_INPUT_XPATH
BIRTHDAY_INPUT_XPATH         = Const.BIRTHDAY_INPUT_XPATH
EMAIL_INPUT_XPATH            = Const.EMAIL_INPUT_XPATH
NEXT_BUTTON_XPATH            = Const.NEXT_BUTTON_XPATH

#신분증 선택 페이지
DRIVERS_LICENSE_BUTTON_XPATH = Const.DRIVERS_LICENSE_BUTTON_XPATH
SELECT_COMPLETE_BUTTON_XPATH = Const.SELECT_COMPLETE_BUTTON_XPATH

#신분증 제출 페이지
# UPLOAD_IMAGE_BUTTON_XPATH  = Const.UPLOAD_IMAGE_BUTTON_XPATH
SUBMIT_ID_BUTTON_XPATH       = Const.SUBMIT_ID_BUTTON_XPATH
LICENSE_FILE_PATH            = Const.LICENSE_FILE_PATH
SUBMIT_BUTTON_XPATH          = Const.SUBMIT_BUTTON_XPATH

#신분증 정보 확인 페이지
ID_INFO_CHECK_PAGE_NEXT_BUTTON_XPATH = Const.ID_INFO_CHECK_PAGE_NEXT_BUTTON_XPATH


driver = ChromeDriver().set_driver()
# 페이지 가져오기 (접속)
driver.get(TEST_SITE_URL)
        
# 화면 크기 지정
# driver.fullscreen_window() # 전체화면 모드로 변경
# driver.maximize_window() # 최대 창 크기로 변경
driver.set_window_rect(0, 0, 1680, 990)  # 특정 좌표(x,y)와 크기(width,height)로 변경

###################################################################################
# MAIN 페이지
###################################################################################

# Debug Window 설정 여부 버튼
postMsgToggleBtn = driver.find_element(By.XPATH, POST_MSG_TOGGLE_BUTTON_XPATH)
postMsgToggleBtn.click()

# 개인정보 옵션 체크박스
privacyOpCheckBtn = driver.find_element(By.XPATH, PRIVACY_OPTION_CHECK_XPATH)
privacyOpCheckBtn.click()

# 신분증 인증 버튼
certiIdBtn = driver.find_element(By.XPATH, CERTIFICATE_ID_BUTTON_XPATH)
certiIdBtn.click()

# 개인정보 입력 페이지는 iframe 으로 옮겨서 검사해야 코드로 접근이 가능함
kycIframe = driver.find_element(By.CSS_SELECTOR, 'iframe')

if kycIframe:
    iframeId = kycIframe.get_attribute('id')

    if(iframeId == Const.KYC_IFRAME_TEXT):
        driver.switch_to.frame(kycIframe)

        driver.implicitly_wait(5) # 묵시적 대기, 활성화를 최대 5초까지 기다린다.

        ###################################################################################
        # 개인정보 입력 페이지
        ###################################################################################
        
        nameTextField = driver.find_element(By.XPATH, NAME_INPUT_XPATH)
        nameTextField.send_keys(Const.DRIVER_NAME)

        phoneTextField = driver.find_element(By.XPATH, PHONE_INPUT_XPATH)
        phoneTextField.send_keys(Const.DRIVER_PHONE)

        birthTextField = driver.find_element(By.XPATH, BIRTHDAY_INPUT_XPATH)
        birthTextField.send_keys(Const.DRIVER_BIRTH)

        emailTextField = driver.find_element(By.XPATH, EMAIL_INPUT_XPATH)
        emailTextField.send_keys(Const.DRIVER_EMAIL)

        # 다음 버튼 클릭
        nextBtn = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
        nextBtn.click()
        
        ###################################################################################
        # 신분증 선택 페이지
        ###################################################################################
        
        driversLicenseBtn = driver.find_element(By.XPATH, DRIVERS_LICENSE_BUTTON_XPATH)
        driversLicenseBtn.click()
        
        nextBtn = driver.find_element(By.XPATH, SELECT_COMPLETE_BUTTON_XPATH)
        nextBtn.click()
        
        ###################################################################################
        # 신분증 제출 페이지
        ###################################################################################        
        
        #UPLOAD_IMAGE_BUTTON_XPATH 는 input type file 로 따로 잡아서 사용
        driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(LICENSE_FILE_PATH)
        
        submitIdBtn = driver.find_element(By.XPATH, SUBMIT_ID_BUTTON_XPATH)
        submitIdBtn.click()
        
        element = driver.switch_to.active_element
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 최대 5초 기다린다.
        submitBtn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, SUBMIT_BUTTON_XPATH)))
        submitBtn.click()

        ###################################################################################
        # 신분증 정보 확인 페이지
        ###################################################################################
        
        # EC.element_to_be_clickable - 해당 Element가 클릭 가능할 때까지 최대 5초 기다린다.
        nextBtn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ID_INFO_CHECK_PAGE_NEXT_BUTTON_XPATH)))
        nextBtn.click()
        

        time.sleep(1000)

    else:
        print('The iframe id is incorrect. Expected: "kyc_iframe" Actual: ', iframeId)
"""
운전면허증 인증 자동화
"""

import time
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
PRIVACY_OPTION_CHECK_XPATH = Const.PRIVACY_OPTION_CHECK_XPATH
# 신분증 인증 버튼
CERTIFICATE_ID_BUTTON_XPATH = Const.CERTIFICATE_ID_BUTTON_XPATH

# 운전면허증 정보 입력 페이지
NAME_INPUT_XPATH = Const.NAME_INPUT_XPATH
PHONE_INPUT_XPATH = Const.PHONE_INPUT_XPATH
BIRTHDAY_INPUT_XPATH = Const.BIRTHDAY_INPUT_XPATH
EMAIL_INPUT_XPATH = Const.EMAIL_INPUT_XPATH


driver = ChromeDriver().set_driver()
# 페이지 가져오기 (접속)
driver.get(TEST_SITE_URL)

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
kycIframe = driver.find_element_by_css_selector('iframe')

if kycIframe:
    iframeId = kycIframe.get_attribute('id')

    if(iframeId == Const.KYC_IFRAME_TEXT):
        driver.switch_to.frame(kycIframe)

        driver.implicitly_wait(5) # 묵시적 대기, 활성화를 최대 5초까지 기다린다.

        # 개인정보 입력 페이지
        nameTextField = driver.find_element(By.XPATH, NAME_INPUT_XPATH)
        nameTextField.send_keys(Const.DRIVER_NAME)

        phoneTextField = driver.find_element(By.XPATH, PHONE_INPUT_XPATH)
        phoneTextField.send_keys(Const.DRIVER_PHONE)

        birthTextField = driver.find_element(By.XPATH, BIRTHDAY_INPUT_XPATH)
        birthTextField.send_keys(Const.DRIVER_BIRTH)

        emailTextField = driver.find_element(By.XPATH, EMAIL_INPUT_XPATH)
        emailTextField.send_keys(Const.DRIVER_EMAIL)


        # 화면 크기 지정
        # driver.fullscreen_window() # 전체화면 모드로 변경
        # driver.maximize_window() # 최대 창 크기로 변경
        driver.set_window_rect(0, 0, 1680, 990)  # 특정 좌표(x,y)와 크기(width,height)로 변경

        time.sleep(1000)

    else:
        print('The iframe id is incorrect. Expected: "kyc_iframe" Actual: ', iframeId)
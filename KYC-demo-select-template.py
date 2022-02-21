import time
from driver import ChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


TEST_SITE_URL = 'https://kyc-demo-stg.useb.co.kr/'
POST_MSG_TOGGLE_BUTTON_XPATH = '//div[@id=\'customer_start_ui\']/div[2]/label/span'
PRIVACY_OPTION_CHECK_XPATH = '(//img[@alt=\'check\'])[2]'

driver = ChromeDriver().set_driver()
# 페이지 가져오기 (접속)
driver.get(TEST_SITE_URL)
# driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

# 화면 크기 지정
# driver.fullscreen_window() # 전체화면 모드로 변경
# driver.maximize_window() # 최대 창 크기로 변경
driver.set_window_rect(0,0,1680,990) # 특정 좌표(x,y)와 크기(width,height)로 변경

# Debug Window 설정 여부 버튼
postMsgToggleBtn = driver.find_element(By.XPATH, POST_MSG_TOGGLE_BUTTON_XPATH)
postMsgToggleBtn.click()

# 개인정보 옵션 체크박스
privacyOpCheckBtn = driver.find_element(By.XPATH, PRIVACY_OPTION_CHECK_XPATH)
privacyOpCheckBtn.click()


time.sleep(1000)
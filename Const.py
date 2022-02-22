TEST_SITE_URL   = 'https://kyc-demo-stg.useb.co.kr/'
KYC_IFRAME_TEXT = 'kyc_iframe'

# 인증 종류 선택 페이지
POST_MSG_TOGGLE_BUTTON_XPATH    = '//div[@id=\'customer_start_ui\']/div[2]/label/span'
PRIVACY_OPTION_CHECK_XPATH      = '(//img[@alt=\'check\'])[2]'
# 신분증 인증 버튼
CERTIFICATE_ID_BUTTON_XPATH = '//div[@id=\'logic-options\']/ul/li/img'

# 개인정보 입력 페이지
NAME_INPUT_XPATH             = '//div[@id="app"]/div/div/div[4]/div/input'
PHONE_INPUT_XPATH            = '//div[@id=\'app\']/div/div/div[6]/div/input'
BIRTHDAY_INPUT_XPATH         = '//div[@id=\'app\']/div/div/div[8]/div/input'
EMAIL_INPUT_XPATH            = '//div[@id=\'app\']/div/div/div[10]/div/input'
NEXT_BUTTON_XPATH            = '//div[@id=\'app\']/div/div/div[12]/div[2]'

# 신분증 선택 페이지
DRIVERS_LICENSE_BUTTON_XPATH = '//*[@id="app"]/div[1]/div/div/div[6]'
SELECT_COMPLETE_BUTTON_XPATH = '//*[@id="app"]/div[1]/div/div/div[11]/div[2]'

# 신분증 제출 페이지
#UPLOAD_IMAGE_BUTTON_XPATH 는 input type file 로 따로 잡아서 사용
SUBMIT_ID_BUTTON_XPATH       = '//*[@id="app"]/div[1]/div/div[1]/div[7]/div[2]'
LICENSE_FILE_PATH            = 'C:\driversLicense.jpg'
SUBMIT_BUTTON_XPATH          = '//*[@id="app"]/div[7]/div/div/div/div[4]/div[2]'

#신분증 정보 확인 페이지
ID_INFO_CHECK_PAGE_NEXT_BUTTON_XPATH = '//*[@id="app"]/div[1]/div/div[14]/div[2]'

"""
Input Value
"""
DRIVER_NAME     = '김범준'
DRIVER_PHONE    = '01027018838'
DRIVER_BIRTH    = '1990-02-13'
DRIVER_EMAIL    = 'bj.kim@alcherainc.com'

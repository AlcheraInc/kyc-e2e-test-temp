TEST_SITE_URL   = 'https://kyc-demo-stg.useb.co.kr/'
KYC_IFRAME_TEXT = 'kyc_iframe'

# 인증 종류 선택 페이지
POST_MSG_TOGGLE_BUTTON_XPATH    = '//div[@id="customer_start_ui"]/div[2]/label/span'
PRIVACY_OPTION_CHECK_XPATH      = '(//img[@alt="check"])[2]'

# 개인정보 입력 페이지
NEXT_BUTTON_XPATH            = '//div[@id="app"]/div/div/div[12]/div[2]'

# 신분증 선택 페이지
SELECT_COMPLETE_BUTTON_XPATH = '//*[@id="app"]/div[1]/div/div/div[11]/div[2]'

# 신분증 제출 페이지
#UPLOAD_IMAGE_BUTTON_XPATH 는 input type file 로 따로 잡아서 사용
SUBMIT_ID_BUTTON_XPATH       = '//*[@id="app"]/div[1]/div/div[1]/div[7]/div[2]'
SUBMIT_BUTTON_XPATH          = '//*[@id="app"]/div[7]/div/div/div/div[4]/div[2]'

# 얼굴 인증 페이지
TAKE_SELFIE_XPATH                  = '//*[@id="app"]/div[1]/div/div/div[6]/div[2]'
FACE_RECOGNITION_TEXT_XPATH        = '//*[@id="app"]/div[1]/div/div[1]/div[2]/div'
COMPLETED_CERFIFICATION_TEXT_XPATH = '//*[@id="app"]/div[1]/div/div/div[2]'
COMPLETED_CERFIFICATION_TEXT       = '본인 인증 완료'
FAILED_CERFIFICATION_TEXT_XPATH    = '//*[@id="app"]/div[1]/div/div[4]/div[2]/div[1]'
FAILED_CERFIFICATION_TEXT          = '얼굴 인증 실패'

# 얼굴 인증 실패 에러 코드
FAILED_CERFIFICATION_ERROR_CODE_XPATH               = '//*[@id="app"]/div[1]/div/div[4]/div[2]/div[3]'
# 얼굴 감지 실패 에러 Title
FAILED_CERFIFICATION_VCARD_ERROR_CODE_TITLE_XPATH   = '//*[@id="app"]/div[7]/div/div/div/div[1]/div'
# 얼굴 감지 실패 에러 코드
FAILED_CERFIFICATION_VCARD_ERROR_CODE_XPATH         = '//*[@id="app"]/div[7]/div/div/div/div[3]'

# 계좌 인증 페이지
ENTER_ACCOUNT_BUTTON_XPATH          = '//*[@id="app"]/div[1]/div/div[6]/button[2]'
VERIFICATION_ACCOUNT_TEXT_XPATH     = '//*[@id="app"]/div[1]/div/div[1]'
VERIFICATION_ACCOUNT_TEXT           = '계좌인증'
SELECT_BANK_N_STOCK_XPATH           = '//*[@id="app"]/div[1]/div/div[3]/button/span'
ENTER_ACCOUNT_NUMBER_XPATH          = '//*[@id="app"]/div[1]/div/div[3]/div[2]/div/input'
SEND_ONE_WON_BUTTON_XPATH           = '//*[@id="app"]/div[1]/div/div[3]/div[3]'
BANK_LIST_ITEM_XPATH                = '//*[@class="bank-list-item"]'
STOCK_TAB_XPATH                     = '//*[@id="app"]/div[7]/div/div/div[2]/div[1]/div/div[2]/div/div[3]'
은행목록XPATH = '//*[@id="app"]/div[7]/div/div/div[2]/div[2]/div/div[1]/div/ul'
증권사목록XPATH = '//*[@id="app"]/div[7]/div/div/div[2]/div[2]/div/div[2]/div/ul'

TIMEOUT_ONE_MINUTE           = 60
SUCCESS                      = 'SUCCESS'
FAILED                       = 'FAILED'

"""
Input Value
"""
USER_NAME                     = '김범준'
USER_BIRTH                    = '1990-02-13'
# USER_NAME                     = '안유리'
# USER_BIRTH                    = '1990-07-22'
PASSPORT_USER_NAME            = '양동현'
PASSPORT_USER_BIRTH           = '1984-11-23'
FOREIGN_USER_NAME             = 'TAE JOHNNY'
FOREIGN_USER_BIRTH            = '1993-01-27'
REGISTERED_FOREIGN_USER_NAME  = 'SOHN SEONG KYU'
REGISTERED_FOREIGN_USER_BIRTH = '1993-10-19'
USER_PHONE                    = '01027018838'
USER_EMAIL                    = 'bj.kim@alcherainc.com'

# NH 농협
# 우리
# 신한
# KB국민
# 하나
# 씨티
# IBK기업
# 케이뱅크
# 카카오뱅크
# 새마을
# 부산
# 경남
# 광주
# 전북
# 신협
# SC제일
# KDB산업
# 대구
# 제주
# 우체국
# 수협
# 저축
# 산림
BANK_NAME                     = '국민'
ACCOUNT_NUMBER                = '03160204206637'
# How to setup
git clone https://github.com/qa-BeomJun/KYC_Selenium.git

# PreSetup 
C:\idCard.jpg
C:\driversLicense.jpg
C:\passPort.jpg
C:\foreignPassPort.jpg
C:\alienRegistrationCard.jpg

C드라이브에 각 신분증 이미지를 준비해야 합니다.

# How to run
KYC-demo-select-template.py 파일에 테스트하려는 모드를 작성한 뒤 Ctrl + F5 로 수행
설치경로/logs 폴더에 수행 결과가 로그 파일로 남음

### ChromeDriver
설치된 Chrome 브라우저의 내장 Driver를 사용하도록 작성되어 있으니, 별도로 다운로드할 필요가 없습니다.

# Solution
selenium 관련 lib를 찾지 못할 시
: Ctrl + Shift + P -> Python: Select Interpreter 메뉴에서 Recommended 버전 확인 및 변경

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Chrome WebDriver를 초기화
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)

driver.get("https://gw.jointree.co.kr/")
# 로그인 정보 입력
driver.find_element(By.ID, "UI_ID").send_keys("22301118")  # id 필드에 ID 입력
driver.find_element(By.ID, "UI_PASSWORD").send_keys("990927")  # pw 필드에 패스워드 입력

# 로그인 버튼 클릭
login_button = driver.find_element(By.XPATH, '//button[contains(@class, "btn")]')
login_button.click()

driver.implicitly_wait(5)
# holidayList 페이지로 이동 후 데이터 가져오기
driver.get("https://gw.jointree.co.kr/schedule/holidayList")
# 적절한 대기 시간 추가 (이 부분은 필요에 따라 조정해야 할 수 있습니다)
# 일부 웹페이지는 로딩이 완료되지 않은 상태에서 데이터를 가져오므로, 충분한 대기 시간을 주어야 합니다.
# 예시로 5초간 대기하도록 설정
driver.get("https://gw.jointree.co.kr/schedule/holidayList")
time.sleep(3)
# 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
annual_text = soup.select_one("body > div#wrap > div#container > div.contents > p.annual-text")

if annual_text:
    print(annual_text.text)
else:
    print("해당하는 정보를 찾을 수 없습니다.")

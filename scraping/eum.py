from selenium import webdriver
from selenium.webdriver.support.ui import Select

# SELECT 엘리먼트를 위한 라이브러리 로드

driver = webdriver.Chrome("./chromedriver")
# 크롬을 통해서 스크랩핑 진행. 크롬드라이버 로딩
driver.get("http://www.eum.go.kr/web/am/amMain.jsp")


# work1: 전라남도 고흥군 고흥읍 남계리 본번 45 부번 1 지역의 공시지가 출력

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="selSido"]'))
sidoSelect.select_by_visible_text("전라남도")
driver.implicitly_wait(1)
# 상기코드는 드라이버가 1초동안 대기

siSelect = Select(driver.find_element_by_xpath('//*[@id="selSgg"]'))
siSelect.select_by_visible_text("고흥군")
driver.implicitly_wait(1)

dongSelect = Select(driver.find_element_by_xpath('//*[@id="selUmd"]'))
dongSelect.select_by_visible_text("고흥읍")
driver.implicitly_wait(1)

selSelect = Select(driver.find_element_by_xpath('//*[@id="selRi"]'))
selSelect.select_by_visible_text("남계리")
driver.implicitly_wait(1)


bonbun = driver.find_element_by_name("bobn")
bonbun.send_keys("45")
driver.implicitly_wait(1)

bubun = driver.find_element_by_name("bubn")
bubun.send_keys("1")
driver.implicitly_wait(1)

button = driver.find_element_by_xpath("""//*[@id="frm"]/fieldset/div[3]/p""")
button.click()

tableget = driver.find_element_by_xpath("""//*[@id="appoint"]/div[2]/table/tbody""")
rowInTable = tableget.find_elements_by_tag_name("tr")

row = rowInTable[2]
money = row.find_elements_by_tag_name("td")[0]
print(money.text)

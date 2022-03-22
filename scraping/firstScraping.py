from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
# 크롬을 통해서 스크랩핑 진행. 크롬드라이버 로딩

driver.get(
    "https://www.boannews.com/media/view.asp?idx=105552"
)
title = driver.find_element_by_xpath("""//*[@id="news_content"]/b""")
# titleFromClassName = driver.find_element_by_class_name("news_title02")
print(title.text)
# print(titleFromClassName.text)

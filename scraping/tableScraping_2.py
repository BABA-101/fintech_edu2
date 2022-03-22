from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
# 크롬을 통해서 스크랩핑 진행. 크롬드라이버 로딩

driver.get("https://home.sch.ac.kr/sch/06/010100.jsp")
tablebody = driver.find_element_by_xpath('//*[@id="contents_wrap"]/div/div[1]/table/tbody')

rowInTable = tablebody.find_elements_by_tag_name("tr")  

for index, row in enumerate(rowInTable):
    print(index + 1)
    titleAndSinger = row.find_elements_by_tag_name("td")[1]
    print(titleAndSinger.text)

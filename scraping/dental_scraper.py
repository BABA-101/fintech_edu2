# from selenium import webdriver
# import re

# driver = webdriver.Chrome("./chromedriver")
# # 크롬을 통해서 스크랩핑 진행. 크롬드라이버 로딩


# def rePlaceData(value):
#     numbers = re.findall("\d+", value)
#     result = ""
#     for i in numbers:
#         decodeNumber = i
#         result += decodeNumber
#     return result


# # work 2
# # AIA 생명 치아보험 견적 페이지에서 보장 내역과 보험료를 가져와서 비교
# def getAIADate(name, birth, gender):
#     driver.get(
#         "https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#"
#     )
#     driver.implicitly_wait(1)

#     if gender == 0:
#         # 남자를 클릭
#         malebutton = driver.find_element_by_xpath(
#             '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/label/div/div[2]/svg/g/image'
#         )
#         malebutton.click()
#         driver.implicitly_wait(1)
#     else:
#         # 여자 버튼 클릭
#         femalebutton = driver.find_element_by_xpath(
#             """//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/label/div/div[1]/svg/g/image"""
#         )
#         femalebutton.click()
#         driver.implicitly_wait(1)

#     both = driver.find_element_by_xpath('//*[@id="aia644363719"]')
#     both.send_keys(birth)
#     driver.implicitly_wait(1)

#     culButton = driver.find_element_by_xpath('//*[@id="btn806817556"]')
#     culButton.click()

#     money = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]').text
#     print(money)


from selenium import webdriver
import re


def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i
        result += decodedNumber
    return result


def getAIAData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "AIA",
        'price': 0,
        'contents': []
    }
    driver.implicitly_wait(3)
    driver.get(
        'https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    driver.implicitly_wait(3)
    textBox = driver.find_element_by_xpath('//*[@id="aia644363719"]')
    textBox.send_keys("19"+birth)
    if gender == 1:
        femaleBtn = driver.find_element_by_xpath(
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        femaleBtn.click()
    else:
        maleBtn = driver.find_element_by_xpath(
            '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        maleBtn.click()
    resultBtn = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    resultBtn.click()
    driver.implicitly_wait(3)

    htmlResult = driver.find_element_by_xpath(
        '//*[@id="premium-by-timespan-value"]').text
    resultValue = rePlaceData(htmlResult)
    print(resultValue)
    
    scrapingResult['price'] = resultValue
    tableBody = driver.find_element_by_xpath(
        '//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element_by_tag_name('tbody')
    driver.find_element_by_xpath(
        '//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements_by_tag_name('td')[0].text)
            contentsList.append(value.find_elements_by_tag_name('td')[
                                0].text)
    scrapingResult['contents'] = contentsList
    return scrapingResult




def getLinaData(name, birth, gender):
    driver = webdriver.Chrome('./chromedriver')
    scrapingResult = {
        'company': "라이나",
        'price': 0,
        'contents': []
    }
    driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')
    textBox = driver.find_element_by_xpath('//*[@id="birthday"]')
    textBox.send_keys(birth)
    if gender == 1:
        femaleBtn = driver.find_element_by_xpath('//*[@id="main_btn_female"]')
        femaleBtn.click()
    else:
        maleBtn = driver.find_element_by_xpath('//*[@id="main_btn_male"]')
        maleBtn.click()
    resultBtn = driver.find_element_by_xpath(
        '//*[@id="btn_direct_dental_cal"]')
    resultBtn.click()
    driver.implicitly_wait(3)

    htmlResult = driver.find_element_by_xpath(
        '//*[@id="contents"]/div[2]/div[2]/div[2]/div/table/tbody[1]/tr[1]/td[2]/strong').text
    resultValue = rePlaceData(htmlResult)
    scrapingResult['price'] = resultValue
    driver.implicitly_wait(2)
    detailBtn = driver.find_element_by_xpath('//*[@id="openLayerplanPonA2"]')
    detailBtn.click()
    driver.implicitly_wait(2)

    tableBody = driver.find_element_by_xpath(
        '//*[@id="planPonA2"]/div/div[2]/div/div/table[1]').find_element_by_tag_name('tbody')
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []
    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements_by_tag_name('th')[0].text)
            contentsList.append(value.find_elements_by_tag_name('th')[
                                0].text)
    scrapingResult['contents'] = contentsList
    return scrapingResult
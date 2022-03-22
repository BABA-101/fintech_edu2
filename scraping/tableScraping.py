from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
# 크롬을 통해서 스크랩핑 진행. 크롬드라이버 로딩

driver.get("https://www.melon.com/chart/index.htm")
tablebody = driver.find_element_by_xpath('//*[@id="frm"]/div/table/tbody')
# 차트 테이블 전체를 통으로 불러옴   '//*[@id="frm"]/div' 아니니까 조심하기. ㄹㅇ 테이블 불러올거니까 데이터 있는 태그 찾아서 정확히 불러오기.
rowInTable = tablebody.find_elements_by_tag_name("tr")  # 여러개니까 elements라는걸 기억
# 반복적으로 되어있는 <tr>들이라는 엘리먼트들이 배열 평태로.. rowIntable로 들어감.
# top.100이니까 100개가 있겠지

for index, row in enumerate(rowInTable):
    print(index + 1)
    # 제목만 가지고오고싶어서.. 보니까 어? 6번째 <td>에 제목+가수 적혀있네
    titleAndSinger = row.find_elements_by_tag_name("td")[5]
    print(titleAndSinger.text)

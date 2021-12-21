from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dv = webdriver.Chrome()
dv.get("http://www.naver.com")

elem = dv.find_element_by_name("query")
elem.send_keys("맞춤법 검사기")
elem.send_keys(Keys.RETURN)

elem = dv.find_element_by_name("txt_gray")
elem.send_keys("안녕하세요")
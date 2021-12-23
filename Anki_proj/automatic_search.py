from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException
from time import sleep


class AutomaticSearch:
    DRIVER_PATH = 'C:\\Users\\jeony\\OneDrive\\바탕 화면\\Python\\Anki_proj\\chromedriver.exe'

    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome(self.DRIVER_PATH, options=self.options)
        self.word = ''

    def set_word(self, word):
        self.word = word

    def get_word(self):
        try:
            self.driver.get(url='https://en.dict.naver.com/#/main')

            search_box = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.NAME, 'query')))
            search_box.send_keys(self.word)
            search_box.send_keys(Keys.RETURN)

            objs = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(
                (By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[1]/a/strong')))
            for obj in objs:
                obj.click()

            pronounce_area = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'entry_pronounce')))
            pronounce = pronounce_area[0].text

            mean_area = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, 'mean_tray')))
            meaning = mean_area[0].text

            string = f'{self.word}\n{pronounce}\n{meaning}\n'
            return string

        except InvalidSessionIdException as e:
            print(e.msg)

        finally:
            sleep(2)
            self.driver.close()


if __name__ == '__main__':
    word = 'woman'
    ChromeDriver = AutomaticSearch()
    ChromeDriver.set_word(word)
    meaning = ChromeDriver.get_word()
    print(meaning)

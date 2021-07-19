from selenium import webdriver
from time import sleep
from screat import pw


class instBot:

    def __init__(self, UserName, pw):
        self.driver = webdriver.Chrome(r'C:\Users\NAZBEEN_MULTIMEDIA\Documents\python_project\Python_Automation\chromedriver.exe')
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
        .send_keys(UserName)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
        .click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
        sleep(4)


    def followers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")\
            .click()
        self.driver.find_element_by_css_selector ("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a")\
            .click()
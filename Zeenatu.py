from selenium import webdriver

print('*' * 57)

print('  ================* Whatsapp *========================')
print('  ================* Automation *======================')

print('*' * 57)


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
name = input("Search Name Here :  ")
message = input("Enter Your Message Here :  ")



class Automation:
    def SendMsg(self): 
        Searchbar = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        Searchbar.clear()
        Searchbar.send_keys(name)
        Searchbar.click()

    def sendImg(self):
        message = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
        message.clear()
        message.send_keys(message)
        message.click()


A1 = Automation()
A1.SendMsg()
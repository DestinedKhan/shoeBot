import time
from selenium import webdriver
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains

class shoeBot:


    def __init__(self, sneaker_url):
        #Check

        
        self.sneaker_url = sneaker_url
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Liam\Documents\chromedriver.exe')
        self.driver.implicitly_wait(3)


    def getPrice(self):
        self.driver.get(self.sneaker_url)
        price = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[1]/div[1]')
        t = int(price.get_attribute('innerHTML').strip('$'))
        return t


    def getDate(self):
        YEAR = 2020
        self.driver.get(self.sneaker_url)
        date = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/aside/div/div[1]/div[2]/div')
        day = date.get_attribute('innerHTML').strip('Available')


        #Want to format it as YYYY-MM-DD
        txt = day.split()
        d = txt[0]
        p = txt[0].split('/')
        d = str(YEAR)+'-'+str(p[0])+'-'+str(p[1])        
        
        return d


    def buyButton(self):
        self.driver.get(self.sneaker_url)
        
        self.driver.execute_script("window.scrollTo(0,window.scrollY+300)")        
        shoesize = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[4]/form/div[1]/fieldset/div/div[7]/label')
        ActionChains(self.driver).move_to_element(shoesize).click(shoesize).perform()
        
        
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[4]/form/div[2]/div/div/button[1]').click()
        self.driver.implicitly_wait(1.5)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/div/button[2]').click()




        


    def checkout1(self, fname, lname, addy, email, phone, city, state, zipcode):
        #Could make it wait until and then do it
        waitF(self, self.driver)
        while(not waitF(self, self.driver)):
            print("Waiting")
            break
        
        self.driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(fname)
        self.driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lname)
        #Doing the address manually, gonna be harder but fuck it the other way is too inconsistent
        #Need the
        self.driver.find_element_by_xpath('//*[@id="addressSuggestionOptOut"]').click()
        self.driver.find_element_by_xpath('//*[@id="address1"]').send_keys(addy)
        self.driver.find_element_by_xpath('//*[@id="city"]').send_keys(city)
        self.driver.find_element_by_xpath('//*[@id="state"]').send_keys("OH")
        self.driver.find_element_by_xpath('//*[@id="postalCode"]').send_keys(zipcode)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="phoneNumber"]').send_keys(phone)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div/div/main/section[2]/div/div[2]/form/div/div/div/div[2]/button').click()

def waitF(self, driver):
    try:
        driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[2]/div/div/div[4]/form/div[1]/fieldset/div/div[7]/label')
        return False
    except StaleElementReferenceException:
        return True

        
def main():

    fname = "FirstName"
    lname = "LastName"
    addy = "123 Washington Avenue"
    email = "samplemail@gmail.com"
    phone = 123456789
    city = "Columbus"
    state = "Ohio"
    zipcode = 00000
    
    url = 'https://www.nike.com/t/jordan-zoom-92-mens-shoe-HGMsj5/CK9183-100'
    bot = shoeBot(url)
    

    #Logistics of finding the release date is taken care of as well as price(maybe)
    #Was a lot more to be done between the two and I didn't even know it
    #Need to implement the whole buying portion
    bot.buyButton()
    bot.checkout1(fname, lname, addy, email, phone, city, state, zipcode)
        
    
    
    

main()

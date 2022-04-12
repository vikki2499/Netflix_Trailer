from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(path)

#Maximize_Window
driver.maximize_window()

#Open Lucifer Page in Netflix
netflix_trailer = "https://www.netflix.com/in/title/80057918"
driver.get(netflix_trailer)
time.sleep(2)

#Title
print("Title: ",driver.find_element(by = By.CLASS_NAME, value = "title-title").text)
#Description
print("Description: ",driver.find_element(by = By.CLASS_NAME, value = "title-info-synopsis").text)
#Starring
print("Starring: ",driver.find_element(by = By.CLASS_NAME, value = "title-data-info-item-list").text)

#Play_Season-6_Trailer
play_trailer = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section[2]/div[2]/ul/li[1]/div/button/span[1]")
play_trailer.click()



time.sleep(140)

#Close the browser
driver.quit()

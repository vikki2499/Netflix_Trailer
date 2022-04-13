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

driver.implicitly_wait(30)

duration = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div[3]/div/div[4]/div/div[1]/div/div[1]/div/div/div[3]")

total_time = int(duration.get_attribute("aria-valuemax"))


#Hover on the video(Play Stream) for the whole time
count = 0
flag = False
while True:

    current_time = int(duration.get_attribute("aria-valuenow"))
    
    if current_time == total_time - 1:
     print("Video was played using Automation")
     flag = True
     break
    time.sleep(1)
    count += 1
    if count == total_time*2:
      break

if not flag:
  print("Video didn't play")

time.sleep(300)

#Close the browser
driver.quit()


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
#driver = webdriver.Chrome("C:\Users\lenovo\Desktop\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get("https://www.google.com/")

# html locaters
sleep(5)
input = driver.find_element(By.NAME,'q')
input.send_keys("kodlamaio")  #ilgili elemente yazar
searchButton = driver.find_element(By.NAME,"btnk")
sleep(2)
searchButton.click()
sleep(2)
firstResult  = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult.click()

listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama.io sitesinde şu anda {len(listOfCourses)} adet kurs var.")

while True:
    continue

# 2


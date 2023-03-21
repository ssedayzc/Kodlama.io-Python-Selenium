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
firstResult  = driver.find_element(By.XPATH,)
print(input)


while True:
    continue


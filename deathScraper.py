# c:/Program Files/Anaconda3/Scripts/activate"
# "python.pythonPath": "c:\\Program Files\\Anaconda3\\python.exe",

# pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>
# pip install selenium
# pip install webdriver-manager
# pip install chromedriver-binary-auto
# https://pypi.org/project/chromedriver-binary/

# echo %PATH% ~ windows 
# setx PATH "%PATH%;C:\Users\..\app.exe 


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_binary  # Adds chromedriver binary to path
import time
import keyboard

options = Options()

prefs = {"download.default_dictionary" : "C\\Users\\DKMiller\\Downloads\\", 'download.prompt_for_download': False }

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
url = 'https://wonder.cdc.gov/ucd-icd10.html'

driver.get(url)

# click agree button 
agree_button = driver.find_element(By.NAME, 'action-I Agree')
driver.execute_script('arguments[0].click();', agree_button)

driver.find_element(By.XPATH, "//select[@name='B_1']/optgroup[@label='Year and Month']/option[text()='Year']".format(1)).click()

driver.find_element(By.XPATH, "//select[@name='B_1']/optgroup[@label='Year and Month']/option[text()='Month']".format(1)).click()

# hit send
send_button = driver.find_element(By.NAME, "action-Send")
driver.execute_script("arguments[0].click();", send_button)

time.sleep(5)

# hit export button
export_button = driver.find_element(By.NAME, "action-Export")
driver.execute_script("arguments[0].click();", export_button)

time.sleep(1)

keyboard.press('enter')

time.sleep(30)

print('complete')

driver.quit()


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

class Wonder:

    def __init__(self, filepath):
        
        self.filepath = filepath

        self.options = Options()

        self.prefs = {"download.default_dictionary" : self.filepath }

        self.options.add_experimental_option("prefs", self.prefs)

        self.url = 'https://wonder.cdc.gov/mcd-icd10-provisional.html'

        self.driver = webdriver.Chrome(options=self.options)

        self.driver.get(self.url)

    def deathDataset_yr_st_co(self):

        # click agree button 
        agree_button = self.driver.find_element(By.NAME, 'action-I Agree')
        self.driver.execute_script('arguments[0].click();', agree_button)

        #select year, state, county 
        self.driver.find_element(By.XPATH, "//select[@name='B_1']/optgroup[@label='Year and Month']/option[text()='Year']".format(1)).click()

        self.driver.find_element(By.XPATH, "//select[@name='B_2']/optgroup[@label='Residence Location']/option[text()='Residence State']".format(1)).click()
        self.driver.find_element(By.XPATH, "//select[@name='B_3']/optgroup[@label='Residence Location']/option[text()='Residence County']".format(1)).click()

        # hit send
        send_button = self.driver.find_element(By.NAME, "action-Send")
        self.driver.execute_script("arguments[0].click();", send_button)

        time.sleep(120)

        # hit export button
        export_button = self.driver.find_element(By.NAME, "action-Export")
        self.driver.execute_script("arguments[0].click();", export_button)

        time.sleep(30)

        keyboard.press('enter')

        time.sleep(30)

        print('Download Complete')

        self.driver.quit()


        def deathDataset_yr_mo(self):
    
        # click agree button 
        agree_button = self.driver.find_element(By.NAME, 'action-I Agree')
        self.driver.execute_script('arguments[0].click();', agree_button)

        #select year, month
        self.driver.find_element(By.XPATH, "//select[@name='B_1']/optgroup[@label='Year and Month']/option[text()='Year']".format(1)).click()
        self.driver.find_element(By.XPATH, "//select[@name='B_2']/optgroup[@label='Year and Month']/option[text()='Month']".format(1)).click()

        # hit send
        send_button = self.driver.find_element(By.NAME, "action-Send")
        self.driver.execute_script("arguments[0].click();", send_button)

        time.sleep(120)

        # hit export button
        export_button = self.driver.find_element(By.NAME, "action-Export")
        self.driver.execute_script("arguments[0].click();", export_button)

        time.sleep(30)

        keyboard.press('enter')

        time.sleep(30)

        print('Download Complete')

        self.driver.quit()

# Provisional Mortality Statistics, 2018 through Last Current Week
data = Wonder('C\\Users\\DKMiller\\Downloads\\')
data.deathDataset_yr_mo()
data.deathDataset_yr_st_co()


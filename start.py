from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

now = datetime.now()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')   
public = ["10"]
current_time = now.strftime("%H:%M:%S")
print(" ============================= TIME NOW ===========================")
print(" TIME = ", current_time)
print("===================================================================")
while public[0] == "10":
    driver = webdriver.Chrome(executable_path="/data/getIP-public-indihome/chromedriver",chrome_options=chrome_options)
    driver.get("http://192.168.100.1/")
    username = driver.find_elements(By.ID,"txt_Username")
    password = driver.find_elements(By.ID,"txt_Password")
    username[0].send_keys("Support") #ADD USERNAME IN STRING
    password[0].send_keys("theworldinyourhand") #ADD PASSWORD IN STRING
    val_username = username[0].get_attribute('value')
    val_password = password[0].get_attribute('value')
    # print("\n\n")
    # print("===================== INI VALUE LOGIN =======================")
    # print(val_username,val_password)
    # print("=============================================================")
    login = driver.find_elements(By.ID,'loginbutton')
    login[0].click()
    ##################### INFO IP ADDRESS
    infoIP = driver.get("http://192.168.100.1/html/ssmp/smartontinfo/smatontinfo.asp")
    ip = driver.find_elements(By.ID,"internetipv4")
    for i in ip:
        print("\n\n")
        print("================== GET IP ADDRES ROUTER =====================")
        public = i.text.split(".")
        print(" =============== IP ,",i.text)
        if(public[0] != "10"):
            print("IP ANDA SUDAH PUBLIC = ",i.text)
            print("=============================================================")
            driver.get("http://192.168.100.1/index.asp")
            logout = driver.find_elements(By.ID,'headerLogoutText')
            logout[0].click()
            print("================== LOGOUT")
            print("\n\n")
            driver.close()
        else:
            #################### RESTART AREA
            try:
                detail = driver.get("http://192.168.100.1/html/ssmp/accoutcfg/ontmngt.asp")
                restart = driver.find_elements(By.ID,"btnReboot")
                print("\n\n")
                print("================== BUTTON RESTART DETECT ====================")
                print(restart[0].get_attribute('value'))
                print("=============================================================")
                restart[0].click()
                print("=1")
                alert = driver.switch_to.alert
                print("=2")
                alert.accept()
                print("=3")
                print("=============================================================")
                print("======================= REBOOT ROUTER =======================")
                driver.close()
                print("=============================================================")
                time.sleep(100)
            except BaseException as err:
                print(err)
                pass
            

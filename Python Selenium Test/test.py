from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

# WinDriverPath  = r"chromedriver_win32/chromedriver.exe"
# LinuxDriverPath = r"chromedriver_linux64/chromedriver"
# driver = webdriver.Chrome(WinDriverPath,options=options)

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)

driver.get("https://www.python.org")

print('\n')
print("demo testing...")
print('#'*50)
print(driver.title)
print('#'*50)
print("[ DONE ]")
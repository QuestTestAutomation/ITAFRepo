from selenium import webdriver

#browser = webdriver.Firefox()

browser = webdriver.Chrome(executable_path='c:\\Drivers\\chromedriver.exe')
#browser = webdriver.Firefox(executable_path='c:\\Drivers\\geckodriver.exe')
browser.get('http://www.google.com/')
browser.get('http://www.erail.in/')
browser.save_screenshot("C:\\Users\\SANUMOLU\Documents\\files\\screenie.png")
browser.quit()
print("Hello world")
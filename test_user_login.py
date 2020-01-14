from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.keys import Keys
from requests.cookies import RequestsCookieJar

#browser=webdriver.PhantomJS(executable_path='D:/software/phantomjs-2.1.1-windows/bin/phantomjs')
#browser.get("http://jwxt.sdaeu.edu.cn/jwweb/home.aspx")
#为了验证，暂时不用无界

#chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument("--proxy-server=http://127.0.0.1:8080")
#给chrome设置代理

#browser = webdriver.Chrome(chrome_options = chromeOptions)
browser = webdriver.Chrome()
browser.get('http://jwxt.sdaeu.edu.cn/jwweb/home.aspx')
#打开chrome

time.sleep(2)
browser.switch_to_frame('frm_login')
#跳转表单

browser.find_element_by_id("txt_sdertfgsadscxcadsads").click()
jpg=browser.find_element_by_id('imgCode')
img_src=jpg.get_attribute("src")
#print(img_src)
#拿到验证码url

#在这里应该使用browser的ASP.NET_SessionId的值
cookie_bro = browser.get_cookies()
#获取browser的cookie字典
#print(cookie_bro)

cookie1=cookie_bro[0]['value']
print("\n当前cookie为： "+cookie1)

headers1={
	'Host':'jwxt.sdaeu.edu.cn',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
	'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
	'Referer':'http://jwxt.sdaeu.edu.cn/jwweb/_data/login_home.aspx',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cookie':'myCookie=;'+'ASP.NET_SessionId='+cookie1,
	'Connection':'close'
}

#proxy1={"http":"http://127.0.0.1:8080"}
#r=requests.get(img_src,headers=headers1,proxies=proxy1)
#requests代理

r=requests.get(img_src,headers=headers1)
img_content=r.content
print("[*]正在下载验证码...\n")
with open('check.jpg','wb') as f:
	f.write(img_content)

#把对应的“学号”和“密码”换成自己的
browser.find_element_by_id("txt_asmcdefsddsd").send_keys("学号")
browser.find_element_by_id("txt_asmcdefsddsd").send_keys(Keys.TAB)
browser.find_element_by_id("txt_pewerwedsdfsdff").send_keys("密码")

#没有识别功能手动输入
code = input("[*]请输入验证码: ")
browser.find_element_by_id("txt_sdertfgsadscxcadsads").send_keys(code)
browser.find_element_by_id("btn_login").click()

#browser.close()
#关闭浏览器

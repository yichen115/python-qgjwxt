from selenium import webdriver
import requests
import time
import getpass
import pyfiglet
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def menu():
	#功能菜单！
	banner = pyfiglet.figlet_format("sdaeu-jwxt")
	print(banner)
	print("\n欢迎使用山东农业工程学院教务系统辅助脚本！")
	print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
	while True:
		print("\n====== ★功能菜单★ ======\n")
		print("0、看 logo 输入：0")
		print("1、成绩查询 输入：1")
		print("2、校历查看 输入：2")
		print("3、课表查询 输入：3")
		print("4、退出脚本 输入：4")
		gnxz=input("\n[jwxt]等待输入:")
		if gnxz=='0':
			print(banner)
		if gnxz=='1':
			cjcx()
		if gnxz=='2':
			ckxl()
		if gnxz=='3':
			kbcx()
		if gnxz=='4':
			browser.quit()
			break

def kbcx():
	url=url0+"/znpk/Pri_StuSel.aspx"
	browser.get(url)
	time.sleep(2)
	while True:
		print("\n====== 欢迎使用课表查询功能 ======\n")
		xnxq = Select(browser.find_element_by_name('Sel_XNXQ'))
		print('请输入需要查看的学年学期：2019第一学期：20190，第二学期：20191')
		print('退出功能请输入：q')
		year=input("\n[jwxt]等待输入：")
		if year=='q':
			url=url0+"/MAINFRM.aspx"
			browser.get(url)
			break
		else:
			xnxq.select_by_value(year)
			browser.find_element_by_id("rad_gs1").click()
			browser.find_element_by_name("btnSearch").click()
			time.sleep(6)
			browser.save_screenshot('课表.png')

def ckxl():
	url=url0+"/_data/index_lookxl.aspx"
	browser.get(url)
	time.sleep(2)
	while True:
		print("\n====== 欢迎使用校历查看功能 ======\n")
		xlxn = Select(browser.find_element_by_name('sel_xnxq'))
		print('请输入需要查看的学年：2019-2020为2019')
		print('退出功能请输入：q')
		year=input("\n[jwxt]等待输入：")
		if year=='q':
			url=url0+"/MAINFRM.aspx"
			browser.get(url)
			break
		else:
			year=year+'0'
			xlxn.select_by_value(year)
			browser.find_element_by_class_name("but20").click()
			time.sleep(6)
			browser.save_screenshot('校历.png')

def cjcx():

	url=url0+"/xscj/Stu_MyScore.aspx"
	browser.get(url)
	time.sleep(2)
	
	while True:
		print("\n========== 欢迎使用成绩查询功能 ==========\n")
		print("需要选择以下参数：")
		print("入学以来请输入：rxylcjcx")
		print("学年成绩请输入：xncjcx")
		print("学期成绩请输入：xqcjcx")
		print("退出功能请输入：q")
		ckcj=input("\n[jwxt]等待输入:")
		
		if ckcj=='rxylcjcx':
			#入学以来成绩
			browser.find_element_by_xpath('//*[@id="SelXNXQ_0"]').click()
			print("\n原始成绩请输入:ys，有效成绩请输入:yx")
			cjlx=input("[jwxt]等待输入:")
			if cjlx=='ys':
				browser.find_element_by_id("ys_sj").click()
				browser.find_element_by_name("btn_search").click()
				time.sleep(6)
				browser.save_screenshot('入学以来原始成绩.png')
			elif cjlx=='yx':
				browser.find_element_by_id("yx_sj").click()
				browser.find_element_by_name("btn_search").click()
				time.sleep(6)
				browser.save_screenshot('入学以来有效成绩.png')

		elif ckcj=='xncjcx':
			#学年查成绩
			browser.find_element_by_id("SelXNXQ_1").click()
			xnxz = Select(browser.find_element_by_name('sel_xn'))
			year=input("[jwxt]请输入学年，例：2018-2019输入2018：")
			xnxz.select_by_value(year)
			print("\n原始成绩请输入:ys，有效成绩请输入:yx")
			cjlx=input("[jwxt]等待输入:")
			if cjlx=='ys':
				browser.find_element_by_id("ys_sj").click()
				browser.find_element_by_name("btn_search").click()
				time.sleep(6)
				browser.save_screenshot('学年有效成绩.png')
			elif cjlx=='yx':
				browser.find_element_by_id("yx_sj").click()
				browser.find_element_by_name("btn_search").click()
				time.sleep(6)
				browser.save_screenshot('学年原始成绩.png')

		elif ckcj=='xqcjcx':
			#按照学期查成绩
			browser.find_element_by_id("SelXNXQ_2").click()
			xnxz = Select(browser.find_element_by_name('sel_xn'))
			year=input("\n[jwxt]请先输入学年，例：2018-2019输入2018：")
			xnxz.select_by_value(year)
			xqxz = Select(browser.find_element_by_id('sel_xq'))
			xueqi=input("\n[jwxt]第一学期输:0，第二学期输:1：")
			xqxz.select_by_value(xueqi)
			print("\n原始成绩请输入:ys，有效成绩请输入:yx")
			cjlx=input("[jwxt]等待输入:")
			if cjlx=='ys':
				browser.find_element_by_id("ys_sj").click()
				browser.find_element_by_name("btn_search").click()
				time.sleep(6)
				browser.save_screenshot('学期原始成绩.png')
			elif cjlx=='yx':
				browser.find_element_by_id("yx_sj").click()
				browser.find_element_by_name("btn_search").click()
				time.sleep(6)
				browser.save_screenshot('学期有效成绩.png')

		elif ckcj=='q':
			url=url0+"/MAINFRM.aspx"
			browser.get(url)
			break

def login():
	
	browser.switch_to.frame('frm_login')
	#跳转表单
	
	jpg=browser.find_element_by_id('imgCode')
	img_src=jpg.get_attribute("src")

	#拿到验证码url
	print("\n[*]正在获取cookie...")
	#在这里应该使用browser的ASP.NET_SessionId的值

	cookie_bro = browser.get_cookies()
	#获取browser的cookie字典

	cookie1=cookie_bro[1]['value']
	print("\n[*]cookie获取成功！")
	headers1={
		'Cache-Control': 'no-cache',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1',
		'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
		'Referer':'http://jwxt.sdaeu.edu.cn/jwweb/_data/login_home.aspx',
		'Cookie':'myCookie=;'+'ASP.NET_SessionId='+cookie1,
		'Connection':'close',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,en,*',
		'Host':'jwxt.sdaeu.edu.cn'
	}

	r=requests.get(img_src,headers=headers1)
	img_content=r.content
	print("\n[*]正在下载验证码...")
	with open('check.jpg','wb') as f:
		f.write(img_content)
	
	time.sleep(1)
	print("\n[*]验证码下载完成！")
	code=input("\n[*]请输入验证码：")
	
	username=input("\n[*]请输入用户名：")
	password=getpass.getpass("\n[*]请输入密码：")

	browser.find_element_by_id("txt_asmcdefsddsd").send_keys(username)
	browser.find_element_by_id("txt_asmcdefsddsd").send_keys(Keys.TAB)
	browser.find_element_by_id("txt_pewerwedsdfsdff").send_keys(password)
	browser.find_element_by_id("txt_sdertfgsadscxcadsads").send_keys(code)
	browser.find_element_by_id("btn_login").click()
	time.sleep(1)
	print("\n=========== 登录成功 ===========\n")

if __name__ == '__main__':
	
	browser=webdriver.PhantomJS(executable_path='D:/software/phantomjs-2.1.1-windows/bin/phantomjs')
	url="http://jwxt.sdaeu.edu.cn"
	
	browser.get(url)
	
	time.sleep(2)
	url1=browser.current_url
	url0=url1[0:-10]
	
	login()
	menu()

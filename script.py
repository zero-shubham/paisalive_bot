import time
from selenium import webdriver

def main():
	selenium_web('http://www.paisalive.com/login.asp')
		


def selenium_web(url_lk):
	add_page_dict= {'1':'/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[4]/td/div/div[2]/center/a/img',
	'2':'/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[4]/td/div/div[2]/center/div/a/font/h1',
	'3':'/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr[4]/td/div/div[2]/center/a/h1',
	'4':'/html/body/div/div/div/table/tbody/tr/td[1]/div/form/div/div[1]/div/div/span'}
	browser=webdriver.Firefox()
	browser.get(url_lk)
	time.sleep(10)
	#user credentials
	user=browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[3]/input')
	user.send_keys('YOUR EMAIL')
	password=browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/form/table/tbody/tr[3]/td[2]/input')
	password.send_keys('PASSWORD')
	login=browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/form/table/tbody/tr[4]/td[2]/input')
	login.click()
	red_button1=browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td/a')
	red_button1.click()
	time.sleep(30)
	print(browser.window_handles[1])
	browser.switch_to_window(browser.window_handles[1])
	time.sleep(5)
	browser.close()
	time.sleep(5)
	browser.switch_to_window(browser.window_handles[0])
	browser.refresh()
	time.sleep(10)
	cash_button= browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div[2]/div/ul/li[1]/a')
	cash_button.click()
	time.sleep(5)
	c=9
	while(c<=14):
		str_lnk= '/html/body/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div[2]/table/tbody/tr['+str(c)+']/td[3]/a'
		add_button= browser.find_element_by_xpath(str_lnk)
		add_button.click()
		time.sleep(20)
		print(browser.window_handles[1])
		browser.switch_to_window(browser.window_handles[1])
		time.sleep(5)
		browser.refresh()
		print("debug")
		for q in range(1, 5):
			print('got in loop')
			try:
				add_page=browser.find_element_by_xpath(add_page_dict[str(q)])
				add_page.click()
				time.sleep(10)
			except:
				continue

		print(browser.window_handles)
		browser.switch_to_window(browser.window_handles[1])
		browser.close()
		browser.switch_to_window(browser.window_handles[1])
		browser.refresh()
		time.sleep(10)
		browser.refresh()
		time.sleep(10)
		browser.close()
		browser.switch_to_window(browser.window_handles[0])
		browser.refresh()
		time.sleep(20)

		c=c+1
	logout_btn=browser.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/ul/li[5]/a')
	logout_btn.click()
	browser.quit()


if __name__ == '__main__':
	main()

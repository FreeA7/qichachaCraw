from selenium import webdriver


class CookieHandle(object):

    def __init__(self, name, psw):
        self.cookie = {}
        self.name = name
        self.psw = psw

    def get_cookie(self):

        driver = webdriver.Chrome()
        driver.get('http://www.qichacha.com/')

        while 1:
            try:
                driver.find_element_by_xpath(
                    '/html/body/header/div/div[2]/a[2]').click()
                break
            except:
                continue

        while 1:
            try:
                name_input = driver.find_element_by_xpath(
                    '//*[@id="user_login_normal"]/div[1]/input')
                psw_input = driver.find_element_by_xpath(
                    '//*[@id="user_login_normal"]/div[2]/input')
                break
            except:
                continue

        name_input.send_keys(self.name)
        psw_input.send_keys(self.psw)

        while driver.current_url != 'http://www.qichacha.com/':
            pass

        for i in driver.get_cookies():
            self.cookie[i['name']] = i['value']
        driver.quit()

        return self.cookie

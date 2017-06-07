from selenium import webdriver
from urllib.parse import quote
from time import sleep
import os
import re

#############  读取企业名单  #############
p = re.compile('[^\t]+[\t|\n]')
f = open('output.txt', 'r')
count = 0
name_list = []
f_dic = {}
while 1: 
    count += 1
    line = f.readline()
    if line:
        list = p.findall(line)
        list = [i[:-1] for i in list]
        if list[-1] == '0':
            continue
        list = list[:-1]
        try:
            name_list.append(list[1])
            f_dic[list[1]] = list[0]
        except:
            name_list.append(list[0])
            f_dic[list[0]] = 'Null'
    else:
        break
f.close()

#############  断点继续删去已经读写  #############
sum = 0
if os.path.exists('output_have.txt'):
    f = open('output_have.txt', 'r')
else:
    f = open('output_have.txt', 'w')
    f.close()
    f = open('output_have.txt', 'r')
while 1:
    line = f.readline()
    if line:
        list = p.findall(line)
        list = [i[:-1] for i in list]
        sum += 1
        if len(list) == 2:
            name_list.remove(list[0])
        else:
            name_list.remove(list[1])
    else:
        break
f.close()


#############  进行登录  #############
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



name_input.send_keys('username')
psw_input.send_keys('password')

sleep(15)


#############  开始查询  #############
f = open('output_have.txt', 'a+')

for i in name_list:
    sum += 1
    driver.get('http://www.qichacha.com/search?key=' +
               quote(i.encode('utf-8')))
    # yzm_url =
    # 'http://www.qichacha.com/index_verify?type=companysearch&back=/search'
    if driver.current_url != 'http://www.qichacha.com/search?key=' + quote(i.encode('utf-8')):
        count = 0
        while driver.current_url != 'http://www.qichacha.com/search?key=' + quote(i.encode('utf-8')):
            sleep(5)
            count += 1
            if count == 2:
                driver.get('http://www.qichacha.com/search?key=' +
                           quote(i.encode('utf-8')))
                count = 0

    while 1:
        try:
            num = driver.find_element_by_xpath(
                '//*[@id="countOld"]/span[1]').text.replace(' ', '')
            break
        except:
            continue

    if num == '0':
        print('第' + str(sum) + '个企业是' + i + '，没有信息！')
        if f_dic[i] == 'Null':
            f.write('\t' + i + '\t0\n')
        else:
            f.write(f_dic[i] + '\t' + i + '\t0\n')
        f.flush()
    else:
        if re.sub('[（][\u4e00-\u9fa5]+[）]', '', driver.find_element_by_xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a').text.replace('(', '（').replace(')', '）').replace(' ', '')) == re.sub('[（][\u4e00-\u9fa5]+[）]', '', i.replace('(', '（').replace(')', '）').replace(' ', '')):
            handle = driver.current_window_handle
            driver.find_element_by_xpath(
                '//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a').click()
            handles = driver.window_handles
            while len(handles) == 1:
                handles = driver.window_handles
            for newhandle in handles:
                if newhandle != handle:
                    driver.switch_to_window(newhandle)
            count = 0
            while 1:
                try:
                    count += 1
                    zt = driver.find_element_by_xpath(
                        '//*[@id="Cominfo"]/table/tbody/tr[2]/td[4]').text.replace(' ', '')
                    break
                except:
                    if count == 5:
                        sleep(5)
                        driver.refresh()
                        count = 0
                    continue
            driver.close()
            driver.switch_to_window(handles[0])

            if '吊销' in zt or '注销' in zt:
                print('第' + str(sum) + '个企业是' + i + '，没有信息！')
                if f_dic[i] == 'Null':
                    f.write('\t' + i + '\t0\n')
                else:
                    f.write(f_dic[i] + '\t' + i + '\t0\n')
                f.flush()
            else:
                print('第' + str(sum) + '个企业是' + i + '，有相关信息！')
                if f_dic[i] == 'Null':
                    f.write('\t' + i + '\t1\n')
                else:
                    f.write(f_dic[i] + '\t' + i + '\t1\n')
                f.flush()

        else:
            print('第' + str(sum) + '个企业是' + i + '，没有信息！')
            if f_dic[i] == 'Null':
                f.write('\t' + i + '\t0\n')
            else:
                f.write(f_dic[i] + '\t' + i + '\t0\n')
            f.flush()

from selenium import webdriver
from urllib.parse import quote
from time import sleep
import re
import os

p = re.compile('[^\t]+[\t|\n]')
f = open('output_have.txt', 'r')
count = 0
name_list = []
f_dic = {}
while 1: 
    count += 1
    line = f.readline()
    if count == 1:
        continue
    if line:
        list = p.findall(line)
        target = list[-1][:1]
        list = list[:-1]
        list = [i[:-1] for i in list]
        try:
            name_list.append(list[1])
            f_dic[list[1]] = [target,list[0]]
        except:
            name_list.append(list[0])
            f_dic[list[0]] = [target,'']
    else:
        break
f.close()

sum = 0
count = 0
if os.path.exists('output_now.txt'):
    f = open('output_now.txt', 'r')
    while 1:
        count += 1
        line = f.readline()
        if line:
            if count == 1:
                continue
            list = p.findall(line)
            list = [i[:-1] for i in list]
            sum += 1
            name_list.remove(list[0])
        else:
            break
    f.close()
else:
    f = open('output_now.txt','w')
    f.write('企业名称\t组织机构代码\t统一社会信用代码\t注册号\t经营状态\t法定代表人\t注册资本\t公司类型\t成立日期\t营业期限\t登记机关\t核准日期\t公司规模\t所属行业\t英文名\t曾用名\t企业地址\t经营范围\t股东\t持股比例\t认缴出资额（万元）\t认缴出资日期\t股东类型\n')
    f.close()

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

f = open('output_now.txt','a+')

for i in name_list:
    sum += 1
    driver.get('http://www.qichacha.com/search?key=' +
               quote(i.encode('utf-8')))
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
            list_target = []
            list_gd = []
            count = 0
            while 1:
                try:
                    count += 1
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[1]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[1]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    # list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[2]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[2]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[3]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[3]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[4]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[4]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[5]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[5]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[6]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[6]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[7]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[7]/td[4]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[8]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[9]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                    list_target.append(driver.find_element_by_xpath('//*[@id="Cominfo"]/table/tbody/tr[10]/td[2]').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))

                    try:
                        gd_num = len(driver.find_element_by_xpath('//*[@id="Sockinfo"]/table/tbody').find_elements_by_tag_name('tr')) - 1
                    except:
                        gd_num = 0

                    for gd in range(5):
                        list_gd.append([])
                        for gd_inf in range(gd_num):
                            list_gd[gd].append(driver.find_element_by_xpath('//*[@id="Sockinfo"]/table/tbody/tr[' + str(gd_inf+2) + ']/td[' + str(gd+1) + ']').text.replace(' ','').replace('\t','').replace('\n','').replace('\r',''))
                        
                    
                    break
                except:
                    if count%20 == 0:
                        sleep(0.5)
                    if count == 100:
                        sleep(5)
                        driver.refresh()
                        count = 0
                    continue
            driver.close()
            driver.switch_to_window(handles[0])


            f.write(i + '\t' + f_dic[i][1] + '\t' + '\t'.join(list_target) + '\t')
            if len(list_gd) != 0:
                f.write(','.join(list_gd[0]) + '\t')
                f.write(','.join(list_gd[1]) + '\t')
                f.write(','.join(list_gd[2]) + '\t')
                f.write(','.join(list_gd[3]) + '\t')
                f.write(','.join(list_gd[4]) + '\n')
            f.flush()
            print('第' + str(sum) + '个企业是' + i + '，已经收集信息！')

        else:
            print('第' + str(sum) + '个企业是' + i + '，没有信息！')

from fileio import Fileio
from getcookie import CookieHandle
# from lxml import html
from bs4 import BeautifulSoup
import requests


def main():
    f = Fileio()
    name_list = f.get_name()
    c = CookieHandle('username', 'password')
    cookie = c.get_cookie()
    recongnize(name_list, cookie)


def recongnize(name_list, cookie):
    url = 'http://www.qichacha.com/search'
    output = {}
    s = requests.Session()
    r = s.get('http://www.qichacha.com/', cookies=cookie)
    # soup = BeautifulSoup(r.text, 'html.parser')
    # print (soup)
    # dsadas()

    for i in name_list:
        payload = {'key': i}
        r = s.get(url, params=payload)
        soup = BeautifulSoup(r.text, 'html.parser')
        print (soup)

        dsadas()

        # while 1:
        #     try:
        #         node = soup.find('span', id='countOld').find('span')
        #         break
        #     except:
        #         r = s.get(url, params=payload)
        #         print (r.text)
        #         soup = BeautifulSoup(r.text, 'html.parser')

        num = int(node.text.replace('\n', '').replace(' ', ''))
        if num == 0:
            output[i] = 0
        else:
            nodes = soup.find('table', class_='m_srchList').find(
                'tbody').find_all('tr')
            nodes = [k.find('a').text.replace(' ', '') for k in nodes]
            print(nodes)

        # tree = html.fromstring(r.text)
        # node = tree.xpath('//*[@id="countOld"]/span[1]')  # 返回节点对象
        # node = tree.xpath('//*[@id="countOld"]/span[1]/text()')  # 返回节点内容
        # print (node)
        # if node == []:
        #     print (r.text)

        # node = node[0][1:].replace(' ','')
        # if int(node) == 0:
        #     output[i] = 0
        # else:
        #     nodes = tree.xpath('//*[@id="searchlist"]/table/tbody/tr')
        #     for j in nodes:
        #         print (j.xpath('/td[2]/a/text()'))


if __name__ == '__main__':
    main()

# /html/body/html/body
# //*[@id="searchlist"]/table/tbody/tr[5]/td[2]/a

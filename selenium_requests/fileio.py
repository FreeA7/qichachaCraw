import re


class Fileio(object):

    def __init__(self):
        p = re.compile('[^\t]+[\t|\n]')
        f = open('在质检总局代码中心找不到对应记录的企业（共48112家）.txt', 'r')
        count = 0
        self.name_list = []
        while 1:
            count += 1
            line = f.readline()
            if count == 1:
                continue
            if line:
                list = p.findall(line)
                list = [i[:-1] for i in list]
                try:
                    self.name_list.append(list[1])
                except:
                    self.name_list.append(list[0])
            else:
                break

    def get_name(self):
        return self.name_list

import sqlite3
from time import sleep
import sys


import download_html
import html_analyze
from getRandom import getRandom
# from date.SQL import executeSQL

def executeSQL(*args):
    conn = sqlite3.connect("..\date\FourCornerCode.db")
    cursor = conn.cursor()
    if args.__len__()==2:
        re = cursor.execute(args[0], args[1])
        re=re.fetchall()
    elif args.__len__()==1:
        re=cursor.execute(args[0])
        re=re.fetchall()
    else:
        re=False
    conn.commit()
    cursor.close()
    conn.close()
    return re


class getFourCornerCode:

    def __init__(self):
        self.url_head="http://tool.httpcn.com/KangXi/So.asp?Tid=8&wd="

        self.download_html=download_html.HtmlDownloader()
        self.html_analyze=html_analyze.HtmlParser()


    def start(self,st=0):

        try:
            for i in range(st,100000):
                print("正在爬取第{}个数据...".format(i+1))
                url=self.url_head+str(i).zfill(5)
                html_content = self.download_html.download(url)
                if html_analyze==None:
                    return int(i)-1
                characters=self.html_analyze.parse(html_content)

                sql="INSERT INTO date VALUES (?,?)"
                for c in characters:
                    try:
                        pare=(c,i)
                        executeSQL(sql,pare)
                    except:
                        pass
                if i%50==0:
                    file = open("temp.txt", "w")
                    file.writelines(str(int(i)-2))
                    file.close()
                    sleep(getRandom(10,30))

                print("\n")
        except:
            return i
            # finally:
            #     file = open("temp.txt", "w")
            #     file.writelines(str(int(i)-2))
            #     file.close()



if __name__ == '__main__':
    if sys.argv.__len__()>1:
        st=int(sys.argv[1])
        if st==-1:
            # sql="delete from date"
            # executeSQL(sql)
            a = getFourCornerCode()
            st=a.start()
        elif st>-1:
            a=getFourCornerCode()
            st=a.start(st)
    else:
         file = open("temp.txt", "r")
         i = file.readlines()
         file.close()
         # print(int(str(i[0])))
         a = getFourCornerCode()
         st=a.start(int(i[0]))
    print(st)





    while st!=99999:
        file = open("temp.txt", "w")
        file.writelines(str(st))
        file.close()
        sleep(getRandom(10,30))
        a = getFourCornerCode()
        st = a.start(int(st))
        print(str(st))

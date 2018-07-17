# coding:utf-8
from bs4 import BeautifulSoup
import re
from urllib import parse

class HtmlParser(object):
    def parse(self,  html_content):
        print("正在分析页面....")

        soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")

        links = soup.find_all("a", href=re.compile(r"^\/Html\/KangXi\/[\d]{2}\/[\s\S]+\.shtml$"))
        characters = []
        for link in links:
            s=str(link).split("\">")[2][0]
            if s!="<":
                print("发现值：{}".format(s), end="\t")
                characters.append(s)
        return characters






# coding=utf-8

import scrapy
from bs4 import BeautifulSoup
from policy_pyspider.items import PolicyPyspiderItem


def contains(key, items):
    return key in items


class GovSpider(scrapy.Spider):
    name = "gov"
    allowed_domains = ["gov.cn"]
    govs = [
        "https://www.gov.cn/zhengce/zuixin/",
        "https://www.gov.cn/zhengce/wenjian/zhongyang/"
    ]
    mems = [
        "http://mem.gov.cn/gk/tzgg/bl/",
        "http://mem.gov.cn/gk/tzgg/tb/",
        "http://mem.gov.cn/gk/tzgg/yjbgg/",
        "http://mem.gov.cn/gk/tzgg/tz/",
        "http://mem.gov.cn/gk/tzgg/h/",
        "http://mem.gov.cn/gk/tzgg/yj/",
        "http://mem.gov.cn/gk/tzgg/qt/",
    ]
    statss = [
        "https://www.stats.gov.cn/sj/zxfb/"
    ]
    moes = [
        "http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1778/",
        "http://www.moe.gov.cn/jyb_xxgk/moe_1777/moe_1779/"
    ]

    start_urls = govs + mems + statss + moes

    def parse(self, response):
        if contains(response.url, self.govs):
            return self.parseGov(response)
        if contains(response.url, self.mems):
            return self.parseMem(response)
        if contains(response.url, self.statss):
            return self.parseStatss(response)
        if contains(response.url, self.moes):
            return self.parseMoe(response)
        pass

    def parseMem(self, response):
        res = []
        soup = BeautifulSoup(response.body, 'html.parser', fromEncoding="utf-8")
        container = soup.find('div', {'class': 'cont'})
        items = container.find_all('li')
        for item in items:
            i = PolicyPyspiderItem()
            i['name'] = item.find('a').text
            link = item.find('a').get('href')
            if link.startswith("../../"):
                i['link'] = "http://mem.gov.cn/gk/" + link[6: len(link)]
            else:
                i['link'] = link
            i['link'] = item.find('a').get('href')
            i['publishDate'] = item.find('a').find('span').text
            i['policyType'] = 'mem'
            i['reqeustURL'] = response.url
            res.append(i)
        return res
        pass

    def parseGov(self, response):
        res = []
        soup = BeautifulSoup(response.body, 'html.parser', fromEncoding="utf-8")
        container = soup.find('div', {'class': 'list list_1 list_2'})
        items = container.find_all('h4')
        for item in items:
            i = PolicyPyspiderItem()
            i['name'] = item.find('a').text.strip()
            link = item.find('a').get('href')
            if link.startswith("./"):
                i['link'] = response.url + link[2: len(link)]
            else:
                i['link'] = link
            i['publishDate'] = item.find('span').text.strip()
            i['policyType'] = 'gov'
            i['reqeustURL'] = response.url
            res.append(i)
        return res

    def parseStatss(self, response):
        res = []
        soup = BeautifulSoup(response.body, 'html.parser', fromEncoding="utf-8")
        container = soup.find('div', {'class': 'list-content'})
        items = container.find_all('li')
        for item in items:
            i = PolicyPyspiderItem()
            i['name'] = item.find('a').text.strip()
            link = item.find('a').get('href').strip()
            i['link'] = response.url + link[2: len(link)]
            i['publishDate'] = item.find('span').text.strip()
            i['policyType'] = 'statss'
            i['reqeustURL'] = response.url
            res.append(i)
        return res

    def parseMoe(self, response):
        res = []
        soup = BeautifulSoup(response.body, 'html.parser', fromEncoding="utf-8")
        print(soup)
        container = soup.find('div', {'class': 'moe-list'})
        print(container)
        items = container.find_all('li')
        for item in items:
            i = PolicyPyspiderItem()
            i['name'] = item.find('a').text.strip()
            i['link'] = item.find('a').get('href').strip()
            i['publishDate'] = item.find('span').text.strip()
            i['policyType'] = 'moe'
            i['reqeustURL'] = response.url
            res.append(i)
        return res

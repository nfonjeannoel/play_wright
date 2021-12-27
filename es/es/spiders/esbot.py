import scrapy
from playwright.sync_api import sync_playwright


def get_cookies():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www-oscaro-es.translate.goog/?_x_tr_sl=es&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sc")
        # try:
        #     title = page.wait_for_selector('.listnav h2 :attr(href)', timeout=30000)
        # except:
        #     print("error laoding")
        #     exit(-1)
        # title = page.query_selector(".listnav h2 :attr(href)")
        # print(title.inner_text())
        cookie_list = page.context.cookies()
        browser.close()
        return cookie_list
        # cookie_str = ""
        # for cookie in cookie_list:
        #     cookie_str += cookie['name'] + "=" + cookie['value'] + "; "
        # # print(title.inner_text())
        # return cookie_str


class EsbotSpider(scrapy.Spider):
    name = 'esbot'
    # start_urls = ['https://www.oscaro.es/piezas-de-motor-702538-c']

    def start_requests(self):
        cookies = get_cookies()
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache', 'pragma': 'no-cache', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        yield scrapy.Request(url='https://www.oscaro.es/piezas-de-motor-702538-c', cookies=cookies, headers=headers)

    def parse(self, response):
        print(response.status_code)


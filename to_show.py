import scrapy
from playwright.sync_api import sync_playwright


def get_cookies():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.oscaro.es")
        try:
            title = page.wait_for_selector('.listnav h2 ', timeout=30000)
        except:
            print("error laoding")
            exit(-1)
        # title = page.query_selector(".listnav h2 :attr(href)")
        print(title.inner_text())
        cookie_list = page.context.cookies()
        browser.close()
        print(cookie_list)
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
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'no-cache', 'pragma': 'no-cache','sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        yield scrapy.Request(url='https://www.oscaro.es', cookies=cookies, headers=headers)

    def parse(self, response):
        print(response.text)

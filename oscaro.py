from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www-oscaro-es.translate.goog/?_x_tr_sl=es&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sc")
        try:
            title = page.wait_for_selector('.listnav h2', timeout=30000)
        except:
            print("error laoding")
            exit(-1)
        print(title.inner_text())
        cookie_list = page.context.cookies()
        browser.close()
        print(cookie_list)
        # cookie_str = ""
        # for cookie in cookie_list:
        #     cookie_str += cookie['name'] + "=" + cookie['value'] + "; "
        # print(cookie_str)
        # return cookie_str


if __name__ == '__main__':
    main()

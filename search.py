from time import sleep
from clicknium import clicknium as cc, locator

tab = cc.chrome.attach_by_title_url(url="https://www.zhihu.com/*")
tab.goto("https://www.zhihu.com/search?type=content&q=clicknium")
tab.wait_appear(locator.chrome.zhihu.span_title)

for _ in range(10):
    tab.scroll(delta_y=5000)
    sleep(0.1)

elems = tab.find_elements(locator.chrome.zhihu.span_title)

for elem in elems:
    print(elem.get_text())
    print(elem.parent.get_property("href"))
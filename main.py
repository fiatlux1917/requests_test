import requests
import random
from lxml.html import fromstring

r = requests.post('https://webhook.site/6bb95ecf-3c59-4f4e-8b48-1cf4a310c01a')
print(r.text)

# функция создает список прокси
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return (list(proxies))


# def test_proxy(proxies):
#     url = 'https://webhook.site/6bb95ecf-3c59-4f4e-8b48-1cf4a310c01a'
#     for id, proxy in enumerate(proxies):
#         print("Request #%d" % id)
#         try:
#             response = requests.get(url, proxies={"http": proxy, "https": proxy})
#             print(response.json())
#
#             with open("proxy.txt", "a+") as px:
#                 px.write(proxy)
#                 px.write("\n")
#         except requests.exceptions.ProxyError:
#             print("Skipping: PROXY ERROR")
#         except:
#             print("Skipping: CONNECTION ERROR")

proxies = get_proxies()
print(proxies)
# print(test_proxy(proxies))

r = requests.post('https://webhook.site/6bb95ecf-3c59-4f4e-8b48-1cf4a310c01a', proxies={'http': '161.202.226.194:80'})
print(r.text)
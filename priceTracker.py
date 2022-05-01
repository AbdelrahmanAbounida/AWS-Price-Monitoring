import requests
from bs4 import BeautifulSoup

MOBILE_URL = 'https://www.amazon.de/-/en/Samsung-Galaxy-A52-Smartphone-128GB/dp/B08VZGJSY7?ref_=Oct_d_obs_d_3468301&pd_rd_w=aenyr&pf_rd_p=e1b6b65c-25f7-4c64-bdd9-678097739641&pf_rd_r=8VWFEGQFAMQRYFA8KN2X&pd_rd_r=4fef0caa-024e-4663-b5dd-8748b4297333&pd_rd_wg=oJZkx&pd_rd_i=B08VZGJSY7'


def getPrice(url):

    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find("span", {"class": "a-price-whole"}).get_text()

    return price


from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(cache_valid_range=10).install()))

pageCount = 1
i=1
result_list = {'id': [], 'name': [], 'href': [], 'price': [], 'promo':[], 'brand':[]}

url = 'https://online.metro-cc.ru/category/bezalkogolnye-napitki/napitki-105003'
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
html = driver.page_source
soup = bs(html, "html.parser")
pages = soup.find_all('a', class_='v-pagination__item catalog-paginate__item')
pageCount = len(pages)+1
while i <= pageCount:
    url = 'https://online.metro-cc.ru/category/bezalkogolnye-napitki/napitki-105003/?page='+str(i)
    driver.get(url)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    html = driver.page_source
    soup = bs(html, "html.parser")    
    contents = soup.find_all('div', class_='catalog-2-level-product-card product-card subcategory-or-type__products-item catalog--online offline-prices-sorting--best-level with-prices-drop')
    for element in contents:
        id = element['data-sku']
        name = element.select('.product-card-name__text')
        prod_card_name = element.find('a', class_='product-card-name')
        href = 'https://online.metro-cc.ru' + prod_card_name['href'] 
        price = ''
        promo = ''
        price_old = element.find('span', class_='product-price nowrap product-card-prices__old style--catalog-2-level-product-card-major-old catalog--online offline-prices-sorting--best-level')
        price_actual = element.find('span', class_='product-price nowrap product-card-prices__actual style--catalog-2-level-product-card-major-actual color--red catalog--online offline-prices-sorting--best-level')
        price_no_promo = element.find('span', class_='product-price nowrap product-card-prices__actual style--catalog-2-level-product-card-major-actual catalog--online offline-prices-sorting--best-level')
        if price_old:
            promo_rub = price_actual.select('.product-price__sum-rubles')
            promo = promo_rub[0].text
            promo_pen = price_actual.select('.product-price__sum-penny')
            if promo_pen:
                promo += promo_pen[0].text
            price_rub = price_old.select('.product-price__sum-rubles')
            price = price_rub[0].text
            price_pen = price_old.select('.product-price__sum-penny')
            if price_pen:
                price += price_pen[0].text   
        else:
            price_rub = price_no_promo.select('.product-price__sum-rubles')
            price = price_rub[0].text
            price_pen = price_no_promo.select('.product-price__sum-penny')
            if price_pen:
                price += price_pen[0].text            
        brand = ''
        if 'aziano' in name[0].text.lower():
            brand = 'aziano'
        elif 'cillout' in name[0].text.lower():
            brand = 'cillout'
        elif 'coca-cola' in name[0].text.lower():
            brand = 'coca-cola'
        elif 'cool cola' in name[0].text.lower():
            brand = 'cool cola'
        elif 'dr pepper' in name[0].text.lower():
            brand = 'dr pepper'
        elif 'evervess' in name[0].text.lower():
            brand = 'evervess'
        elif 'fancy' in name[0].text.lower():
            brand = 'fancy'
        elif 'fantola' in name[0].text.lower():
            brand = 'fantola'
        elif 'fresh bar' in name[0].text.lower():
            brand = 'fresh bar'
        elif 'frustyle' in name[0].text.lower():
            brand = 'frustyle'
        elif 'oshee' in name[0].text.lower():
            brand = 'oshee'
        elif 'pepsi' in name[0].text.lower():
            brand = 'pepsi'
        elif 'rich' in name[0].text.lower():
            brand = 'rich'
        elif 'rioba' in name[0].text.lower():
            brand = 'rioba'
        elif 'rocket' in name[0].text.lower():
            brand = 'rocket'
        elif 'star bar' in name[0].text.lower():
            brand = 'star bar'
        elif 'street' in name[0].text.lower():
            brand = 'streer'
        elif 'афанасий' in name[0].text.lower():
            brand = 'афанасий'
        elif 'вкусный' in name[0].text.lower():
            brand = 'вкусный' 
        elif 'ильинские лемонады' in name[0].text.lower():
            brand = 'ильинские лемонады'
        elif 'калиновъ лимонадъ' in name[0].text.lower():
            brand = 'калиновъ лимонадъ'
        elif 'крестьянский' in name[0].text.lower():
            brand = 'крестьянский'
        elif 'лидский' in name[0].text.lower():
            brand = 'лидский'
        elif 'любимая' in name[0].text.lower():
            brand = 'любимая'
        elif 'напитки из черноголовки' in name[0].text.lower():
            brand = 'напитки из черноголовки' 
        elif 'натахтари' in name[0].text.lower():
            brand = 'натахтари'
        elif 'никола' in name[0].text.lower():
            brand = 'никола'
        elif 'обломов' in name[0].text.lower():
            brand = 'обломов'
        elif 'очаково' in name[0].text.lower():
            brand = 'очаково'
        elif 'очаковский' in name[0].text.lower():
            brand = 'очаковский'     
        elif 'русский дар' in name[0].text.lower():
            brand = 'русский дар' 
        elif 'старые добрые традиции' in name[0].text.lower():
            brand = 'старые добрые традиции'
        elif 'хлебный край' in name[0].text.lower():
            brand = 'хлебный край'
        elif 'царские припасы' in name[0].text.lower():
            brand = 'царские припасы'
        elif 'черноголовка' in name[0].text.lower():
            brand = 'черноголовка'
        elif 'яхонт трапезный' in name[0].text.lower():
            brand = 'яхонт трапезный'             
            
        result_list['id'].append(id)
        result_list['name'].append(name[0].text.strip())
        result_list['href'].append(href)
        result_list['price'].append(price)
        result_list['promo'].append(promo)
        result_list['brand'].append(brand)
    i += 1

df = pd.DataFrame(data=result_list)
df.to_csv('metro.csv')

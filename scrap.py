from lxml import etree
from datetime import datetime
import time
from urllib.request import urlopen, Request
import io

# Get Date to Generate File Name
data_dt = datetime.now().strftime('%Y%m%d%H%M')
filename = "carsome_buycar_" + str(data_dt) + '.csv'

# Function for Requesting URL and XML Tree
def tree_fn(url):
    headers = {'User-agent': 'Mozilla/5.0'}
    request = Request(url, headers=headers or {})
    print("url :" + url)
    try:
        html = urlopen(request, timeout=50)
    except:
        html.getcode()
    htmlparser = etree.HTMLParser()
    tree = etree.parse(html, htmlparser)
    return tree

# Function For Handling HTML Data
def extract_data(ls):
    try:
        data = ls[0].strip()
    except:
        data = ''
    data = data.replace('\n', ' ')
    data = data.replace('  ', '')
    return data

# Main URL
url = 'https://www.carsome.my/buy-car'

# Get Total Page of Cars
tree = tree_fn(url)
num_of_page = int(extract_data(tree.xpath('//*[@id="mod-pagination"]/ul/li[position()=last()-1]/button/text()')))

# Writing CSV File
with io.open(filename, "w", encoding="utf-8") as f:
    print("START WRITING FILE")
    print("TOTAL "+ str(num_of_page) +" PAGES")
    headers = '"car_name"|"car_mileage"|"car_transmission"|"car_location"|"car_price"|"car_instalment_mth_amt"'
    f.write('')
    f.write(u'\ufeff')
    f.write(headers)

    # Get Information on Each Page
    for n in range(num_of_page):
        urldtl = 'https://www.carsome.my/buy-car?pageNo=' + str(n+1)
        tree = tree_fn(urldtl)

        # Get Number of Cars
        num_of_car = int(tree.xpath('count(//div[@class="list-card__item"])')) # should return <= 18
        print("PAGE " + str(n+1) + ", " + str(num_of_car) + " CARS")

        # Get All Information of Each Car
        for i in range(num_of_car):
            top_elememt = '//div[@class="list-card__item"][' + str(i + 1)

            # Get Field
            car_brand = extract_data(tree.xpath(top_elememt + ']/div/article/div/a/p[1]/text()'))
            car_model = extract_data(tree.xpath(top_elememt + ']/div/article/div/a/p[2]/text()'))
            car_name = car_brand + ' ' + car_model
            car_mileage = extract_data(tree.xpath(top_elememt + ']/div/article/div/div[2]/span[1]/text()'))
            car_transmission = extract_data(tree.xpath(top_elememt + ']/div/article/div/div[2]/span[2]/text()'))
            car_location = extract_data(tree.xpath(top_elememt + ']/div/article/div/div[2]/span[3]/text()'))
            car_price = extract_data(tree.xpath(top_elememt + ']/div/article/div/div[4]/div[1]/strong/text()'))
            car_inst_mth_amt = extract_data(tree.xpath(top_elememt + ']/div/article/div/div[4]/div[2]/div/div/span[1]/text()'))

            # Write Record
            f.write('\n"' + car_name + '"|"' + car_mileage + '"|"' + car_transmission + '"|"' + car_location + '"|"' + car_price + '"|"' + car_inst_mth_amt + '"')
        time.sleep(5)
f.close()

print("FINISHED WEB SCRAPING !!!")
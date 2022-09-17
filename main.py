import time
from datetime import datetime
import requests

has_new_products = False


def main(name):
    global has_new_products
    undesiredProducts = ["6633845489733", "4553091907653", "6639586607173", "4632437981253", "4632437620805",
                                    "4438226174021", "4347318534213", "6583673880645", "6583727063109", "4363187814469",
                                    "4363188338757", "4363188109381", "4363188043845", "4363188305989", "4363188437061",
                                    "4363188371525", "4634168754245"]
    desiredProducts = ["6708219150405", "6708218396741", "6708220264517", "6671605203013", "6708220592197"]
    url = "https://hydra-ccc.shop/collections/current"
    count = 0

    while not has_new_products:
        count += 1
        checkShop(url, desiredProducts)
        print(datetime.now(), count)
        time.sleep(60)


def checkShop(url, desiredProducts):
    html_text = requests.get(url).text

    available_product = getProductIDs(html_text)
    for product in available_product:
        if product in desiredProducts:
            notify(product)


def notify(productID):
    global has_new_products
    has_new_products = True
    print("new product with the ID: ", productID)
    webhookURL = "https://discord.com/api/webhooks/933921871508946954/RrFhtj4uRPMYrPrjz7wS_iW0n2wmcMMMMR_hoHg3qQsmeK1p-U3PZZpzkhL7dpOhvtzl"
    message = {"content": "Es gibts neuen Merch: " + productID + " <@264757326857240577> (:",
               "username": "Hydra-ccc Notifier",
               "avatar_url": "https://cdn.shopify.com/s/files/1/0047/2514/5669/files/hydra_logo_ver1_sw_WEB_1200x1200.png"}
    requests.post(url=webhookURL, data=message)


def getProductIDs(source):
    source = source.split(
        'class="grid__item grid-product grid-product--padded medium-up--one-third grid-product__hover-details"')
    source.pop(0)
    products = []
    for element in source:
        if not element.__contains__('class="grid-product__tag grid-product__tag--sold-out"'):
            products.append(element[43:56])
    return products


if __name__ == '__main__':
    main('PyCharm')

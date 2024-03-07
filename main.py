import requests
from bs4 import BeautifulSoup
import csv
import json

params = {
    ':authority': 'coral-app-37f7w.ondigitalocean.app',
    ':method': 'GET',
    ':path': '/',
    ':scheme': 'https',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ko;q=0.8,la;q=0.7',
    'If-None-Match': 'W/"37211-yzqBifOccfgl/NdiQVJPWeiZ6Sk"',
    'Origin': 'https://www.truffle.sa',
    'Referer': 'https://www.truffle.sa/',
    'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
response = requests.get('https://coral-app-37f7w.ondigitalocean.app/', params=params)
# f = open('credit cards.json')
# credit_cards_info = json.load(f)
credit_cards_info = response.json()
csv_file_name = "credit cards list.csv"
csv_file = open(csv_file_name, 'w', encoding='utf-8', newline='')
# f.close()
writer = csv.writer(csv_file)
#finding the correct key array
max_length = 0
correct_keys = []
for record in credit_cards_info['cardsList']:
    if max_length < len(record.keys()):
        max_length = len(record.keys())
        correct_keys = record.keys()

writer.writerow(correct_keys)
print(correct_keys)
row = dict.fromkeys(correct_keys, '')
# print("empty row", row)
for credit_card in credit_cards_info['cardsList']:
    # row = dict(credit_card)
    for key in correct_keys:
        if key in credit_card:
            if type(credit_card[key]) == dict:
                row[key] = credit_card[key]['url']
                # print(row[key])
            else:
                row[key] = credit_card[key]

    writer.writerow(row.values())
    # for (value, index) in credit_card.values():
    #     if type(value) == dict:
    #         credit_card.values[index] = value.url
    #         print(credit_card.values())
    # writer.writerow(credit_card.values())
    # print(credit_card.keys())
# print(credit_cards_info['cardsList'][0])
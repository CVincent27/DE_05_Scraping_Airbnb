import requests
from bs4 import BeautifulSoup
import re

# Récup des 20 premières pages du site
def get_all_pages():
    urls = []
    page_number = 1

    for i in range(20):
        i = f"https://fr.trustpilot.com/categories/electronics_technology?claimed=true&page={page_number}&subcategories=internet_software"
        page_number += 1
        urls.append(i)
    # print(urls)
    return urls
# print(r.status_code)

# Récup des infos des entreprises
def parse_companies():
    r = requests.get("https://fr.trustpilot.com/categories/electronics_technology?claimed=true&page=1&subcategories=internet_software")
    soup = BeautifulSoup(r.content, "html.parser")

    companies = soup.find_all('div', class_='paper_paper__EGeEb paper_outline__bqVmn card_card__yyGgu card_noPadding__OOiac styles_wrapper__Jg8fe')
    # print(len(companies))
    for companie in companies:
        name = companie.find('p').text
        website = companie.find('p', class_='typography_body-m__k2UI7 typography_appearance-subtle__PYOVM styles_websiteUrlDisplayed__lSw1A').text
        rating = companie.find('span', class_='typography_body-m__k2UI7 typography_appearance-subtle__PYOVM styles_trustScore__iURkS').text
        nbr_rating = companie.find('p', class_='typography_body-m__k2UI7 typography_appearance-subtle__PYOVM styles_ratingText__A2dmB').text
        clean_nbr_rating = re.sub(r"\|", " - ", nbr_rating)
        address = companie.find('div', class_='styles_metadataRow__WKWNi').text
        if not address:
            address = "Pas d'adresse"
        tag = companie.find('span', class_='typography_body-s__IqDta typography_appearance-default__t8iAq').text
        print(name, website, clean_nbr_rating, address, tag)

parse_companies()
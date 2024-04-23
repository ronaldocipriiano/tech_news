from time import sleep
from bs4 import BeautifulSoup
import requests


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    scrape = BeautifulSoup(html_content, "html.parser")
    news = scrape.find_all("article", class_="entry-preview")
    links = []

    for new in news:
        div = new.find("div", class_="post-inner")
        link = div.a["href"]
        links.append(link)

    print("Scraped links:", links)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError

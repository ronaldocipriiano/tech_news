from time import sleep
from bs4 import BeautifulSoup
import requests
from tech_news.database import create_news


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
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", class_="next page-numbers")

    if next_page:
        return next_page["href"]
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    news = {}

    news["url"] = soup.find("link", rel="canonical")["href"]
    news["title"] = soup.find("h1", class_="entry-title").text.strip()
    news["timestamp"] = soup.find("li", class_="meta-date").text.strip()
    news["writer"] = soup.find("h5", class_="title-author").text.strip()
    news["reading_time"] = int(
        soup.find("li", class_="meta-reading-time").text.split()[0].strip()
    )
    news["summary"] = soup.find("p").text.strip()
    news["category"] = (
        soup.find("a", class_="category-style")
        .find("span", class_="label")
        .text.strip()
    )

    return news


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://blog.betrybe.com")
    news_links = scrape_updates(html_content)
    news = []

    while len(news_links) < amount and html_content:
        next_page_link = scrape_next_page_link(html_content)
        if next_page_link:
            html_content = fetch(next_page_link)
            news_links += scrape_updates(html_content)
        else:
            break

    for link in news_links:
        news_html_content = fetch(link)
        news_details = scrape_news(news_html_content)
        news.append(news_details)

    create_news(news[:amount])

    return news[:amount]

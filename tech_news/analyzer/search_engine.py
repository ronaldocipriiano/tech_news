from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    title = title.lower()
    result = []

    for news in search_news({}):
        if title in news["title"].lower():
            result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = (
            datetime.strptime(date, "%Y-%m-%d")
            .strftime("%d/%m/%Y")
        )
    except ValueError as exc:
        raise ValueError("Data inválida") from exc

    result = []

    for news in search_news({"timestamp": formatted_date}):
        result.append((news["title"], news["url"]))

    return result


# Requisito 9
def search_by_category(category):
    category = category.lower()
    result = []

    for news in search_news(
        {"category": {"$regex": f".*{category}.*", "$options": "i"}}
    ):
        result.append((news["title"], news["url"]))

    return result

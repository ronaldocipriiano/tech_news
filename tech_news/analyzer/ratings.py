from collections import Counter
from tech_news.database import search_news


# Requisito 10
def top_5_categories():
    categories = [news["category"] for news in search_news({})]

    if not categories:
        return []

    categories_count = Counter(categories)

    sorted_categories = sorted(
        categories_count.items(),
        key=lambda category: (-category[1], category[0])
    )

    return [category[0] for category in sorted_categories[:5]]

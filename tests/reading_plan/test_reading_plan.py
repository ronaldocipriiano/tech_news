from unittest.mock import MagicMock
from pytest import raises
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


news_mock = [
    {"title": "Notícia 1", "reading_time": 2},
    {"title": "Notícia 2", "reading_time": 4},
    {"title": "Notícia 3", "reading_time": 1},
]


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=news_mock)
    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    result = ReadingPlanService.group_news_for_available_time(1)
    assert sorted(result.items()) == sorted({
        "readable": [
            {
                "unfilled_time": 0,
                "chosen_news": [("Notícia 3", 1)]
            }
        ],
        "unreadable": [
            ("Notícia 1", 2),
            ("Notícia 2", 4),
        ],
    }.items())

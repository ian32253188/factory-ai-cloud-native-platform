import random
from datetime import datetime
from typing import Dict, List


class MarketDataScraper:
    """
    Simulates / Fetches public web data streams for Market Intelligence.
    Aggregates news mentions, social sentiment, e-commerce product reviews & search trends.
    """

    def fetch_keyword_mentions(self, keyword: str) -> Dict:
        # Simulate dynamic scraping data for market trend analytics
        base_mentions = random.randint(1200, 8500)
        positive = round(random.uniform(45.0, 75.0), 1)
        negative = round(random.uniform(5.0, 25.0), 1)
        neutral = round(100.0 - positive - negative, 1)

        sentiment_index = round((positive - negative) / 100.0, 2)

        top_topics = [
            f"對 {keyword} 的品質滿意度上升",
            f"{keyword} 價格波動與競品比較",
            f"消費者對於 {keyword} 的新功能討論度爆發",
            f"社群論壇關於 {keyword} 的售後服務反饋"
        ]

        return {
            "keyword": keyword,
            "timestamp": datetime.utcnow().isoformat(),
            "total_mentions": base_mentions,
            "sentiment_breakdown": {
                "positive_pct": positive,
                "neutral_pct": neutral,
                "negative_pct": negative,
                "sentiment_index": sentiment_index
            },
            "trending_topics": top_topics,
            "sources": ["HackerNews", "Public News RSS", "E-Commerce Reviews", "Reddit Trend API"]
        }


market_scraper = MarketDataScraper()

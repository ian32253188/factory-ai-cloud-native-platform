from typing import Dict, Tuple


class AIMarketSentimentEngine:
    """
    AI Market Intelligence & Sentiment Analysis Engine.
    Evaluates consumer feedback, calculates net sentiment score, and generates actionable market advice.
    """

    def analyze_market_trend(self, keyword_data: Dict) -> Tuple[str, float, str, str]:
        sentiment_index = keyword_data["sentiment_breakdown"]["sentiment_index"]
        negative_pct = keyword_data["sentiment_breakdown"]["negative_pct"]

        if negative_pct > 20.0 or sentiment_index < 0.15:
            status = "critical"
            health_label = "【公關危機警告】負面聲量超標"
            advice = f"【負面警告】「{keyword_data['keyword']}」近期負面討論比例達到 {negative_pct}%。建議立即檢查產品退貨率與客服痛點，並進行溝通。"
        elif sentiment_index > 0.45:
            status = "positive"
            health_label = "【市場熱潮】正面口碑持續發酵"
            advice = f"【口碑強勁】「{keyword_data['keyword']}」正面情緒佔比過半！建議加大數位廣告投放與社群網紅行銷曝光。"
        else:
            status = "neutral"
            health_label = "【穩定平穩】市場聲量維持正常"
            advice = f"【市場平穩】「{keyword_data['keyword']}」目前消費者反應持平，建議持續追蹤競品動態並優化定價策略。"

        return status, sentiment_index, health_label, advice


ai_sentiment = AIMarketSentimentEngine()

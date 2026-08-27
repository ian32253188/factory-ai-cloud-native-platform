from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from app.api.market import keywords_db
from app.core.auth import get_current_tenant
from app.models.market import Tenant
from app.services.ai_sentiment import ai_sentiment
from app.services.market_scraper import market_scraper

router = APIRouter(prefix="/api/v1/reports", tags=["Executive Market Reports"])


@router.get("/html/{keyword_id}", response_class=HTMLResponse)
def generate_executive_market_report(keyword_id: str, tenant: Tenant = Depends(get_current_tenant)):
    """
    【企業高級訂閱專屬】自動生成一頁式高階主管/市場總監商業市場調查研報。
    """
    kw = next((k for k in keywords_db if k.id == keyword_id), None)
    if not kw:
        raise HTTPException(status_code=404, detail="找不到指定的市場關鍵字。")

    data = market_scraper.fetch_keyword_mentions(kw.keyword)
    status, sentiment_index, health_label, advice = ai_sentiment.analyze_market_trend(data)

    breakdown = data["sentiment_breakdown"]
    topics_html = "".join([f"<li>{t}</li>" for t in data["trending_topics"]])

    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Market AI - 商業市場調查研報 ({kw.keyword})</title>
        <style>
            body {{ font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif; background: #0b0f19; color: #f8fafc; padding: 40px; line-height: 1.6; }}
            .container {{ max-width: 850px; margin: 0 auto; background: #151d30; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 36px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5); }}
            .header {{ border-bottom: 2px solid #38bdf8; padding-bottom: 16px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; }}
            .title {{ font-size: 24px; font-weight: bold; color: #38bdf8; }}
            .subtitle {{ color: #94a3b8; font-size: 14px; }}
            .badge {{ display: inline-block; padding: 6px 16px; border-radius: 20px; font-weight: bold; font-size: 13px; }}
            .badge-positive {{ background: #059669; color: #fff; }}
            .badge-neutral {{ background: #0284c7; color: #fff; }}
            .badge-critical {{ background: #dc2626; color: #fff; }}
            .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-bottom: 24px; }}
            .card {{ background: #0b0f19; border: 1px solid rgba(255,255,255,0.08); padding: 18px; border-radius: 8px; }}
            .card-title {{ color: #64748b; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; }}
            .card-value {{ font-size: 22px; font-weight: bold; color: #f1f5f9; }}
            .recommendation-box {{ background: rgba(56, 189, 248, 0.1); border-left: 4px solid #38bdf8; padding: 18px; border-radius: 6px; margin-top: 24px; }}
            .topics-box {{ margin-top: 20px; background: rgba(255,255,255,0.02); padding: 16px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.05); }}
            .footer {{ margin-top: 32px; text-align: center; color: #64748b; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div>
                    <div class="title">📊 Market AI 商業市場調查研報</div>
                    <div class="subtitle">分析機構: {tenant.name} | 分類: {kw.category}</div>
                </div>
                <div class="badge badge-{status}">{health_label}</div>
            </div>

            <div class="grid">
                <div class="card">
                    <div class="card-title">調查目標 / 關鍵字</div>
                    <div class="card-value">{kw.keyword}</div>
                    <div style="color: #94a3b8; font-size: 13px;">ID: {kw.id}</div>
                </div>
                <div class="card">
                    <div class="card-title">網路總討論聲量</div>
                    <div class="card-value" style="color: #38bdf8;">{data['total_mentions']:,} 筆</div>
                    <div style="color: #94a3b8; font-size: 13px;">涵蓋新聞、論壇、社群與電商評論</div>
                </div>
                <div class="card">
                    <div class="card-title">AI 淨情緒指數 (Net Sentiment)</div>
                    <div class="card-value">{sentiment_index:+.2f}</div>
                    <div style="color: #94a3b8; font-size: 13px;">範圍: -1.00 (極負面) ~ +1.00 (極正面)</div>
                </div>
                <div class="card">
                    <div class="card-title">消費者情緒分布</div>
                    <div style="font-size: 14px; margin-top: 4px;">
                        <div>🟢 正面口碑: <strong>{breakdown['positive_pct']}%</strong></div>
                        <div>⚪ 中立討論: <strong>{breakdown['neutral_pct']}%</strong></div>
                        <div>🔴 負面批評: <strong>{breakdown['negative_pct']}%</strong></div>
                    </div>
                </div>
            </div>

            <div class="topics-box">
                <div style="font-weight: bold; color: #f1f5f9; margin-bottom: 8px;">🔥 熱門話題與消費者關切重點</div>
                <ul style="padding-left: 20px; color: #cbd5e1; font-size: 14px;">
                    {topics_html}
                </ul>
            </div>

            <div class="recommendation-box">
                <div style="font-weight: bold; color: #38bdf8; margin-bottom: 6px;">💡 AI 商業顧問策略建議</div>
                <div style="font-size: 15px; color: #e2e8f0;">{advice}</div>
            </div>

            <div class="footer">
                研報產出時間: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')} | Market Intelligence Cloud-Native SaaS Platform
            </div>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)

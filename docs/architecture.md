# 系統架構演進 (Architecture Evolution)

本專案的架構設計採取**漸進式演進 (Evolutionary Architecture)** 策略。每個階段皆旨在示範如何從單體架構，演進為支援商業市場調查與網路輿情分析的高擴展性雲原生 SaaS 平台。

---

## 階段 1 — 生產級單體架構 (Production-Shaped Monolith)

```text
Client (客戶端/分析師)
  |
FastAPI (網頁框架)
  |
Router -> Service -> Repository
                     |
                 PostgreSQL (市場調查與聲量資料庫)
```

**學習重點 (Key Learnings)**:
- HTTP / REST API 設計規範與狀態碼
- 分層架構 (Layering) 與依賴邊界 (Dependency Boundaries)
- SQL 查詢與事務管理 (Transactions)
- 自動化測試 (Unit / Integration Tests)
- 12-Factor 環境配置 (Configuration Management)

---

## 階段 2 — 容器化與商業化 SaaS 模組 (Containerized Application & SaaS Core)

```text
Docker Compose
├── API (FastAPI Gateway)
├── PostgreSQL (主資料庫)
├── Redis (熱門關鍵字快取與 Rate Limit)
└── Stripe Billing Integration
```

**學習重點 (Key Learnings)**:
- 多租戶隔離 (Multi-Tenancy Isolation)
- Stripe 金流 API 與按用量計費 (Usage-based Billing)
- API Key 鑑權與權限控管 (RBAC)
- 容器化部署與 Redis 快取策略

---

## 階段 3 — 數據收集與 AI 商業情報 (Data Collection & AI Analytics Platform)

```text
Public APIs / Web Scraper -> Feature Pipeline -> PostgreSQL
                                  |                 |
                                  v                 v
                       NLP Sentiment Engine ---> Executive PDF Report Generator
```

**學習重點 (Key Learnings)**:
- 網路公開數據抓取 (Scraper Ingestion)
- AI NLP 情感分析與負面輿情預警
- 自動化 PDF 商業市場研報生成 (Report Generator)

---

## 階段 4 — Kubernetes 叢集與 SRE 可觀測性 (Kubernetes & SRE)

```text
Kubernetes Cluster
├── Gateway Deployment + Service
├── Scraper Worker Deployment
├── AI Analytics Deployment
├── ConfigMaps / Secrets
└── HPA (自動擴縮) / Health Probes (健康檢查)
```

---

## 階段 5 — CI/CD 與 GitOps 自動化 (CI/CD & GitOps)

```text
Developer -> GitHub PR
               |
          GitHub Actions (Lint -> Test -> Build Image)
               |
            Argo CD (GitOps Controller)
               |
          Kubernetes Cluster
```

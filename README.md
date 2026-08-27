# Market Intelligence & AI/MLOps Cloud-Native Platform (雲原生商業市場調查與 AI 輿情數據 SaaS 平台)

本專案是一個兼具**雲原生微服務 (Cloud-Native Microservices)**、**SRE 網站可靠性工程 (SLI/SLO)**、**大數據與 NoSQL 資料工程 (PostgreSQL, MariaDB, MongoDB, Cassandra, MinIO/S3, PySpark)**、**AI Platform / MLOps (MLflow, Model Serving)**，以及**商業化多租戶付費訂閱 (Monetizable B2B SaaS)** 的生產級全棧平台。

本專案完全對照頂尖企業的工程師、雲原生架構師、SRE 與 MLOps 專家職缺要求（Job Descriptions）設計，提供完整的 **30 天每日詳細學習、實作與可驗證步驟**。

---

## 🎯 5 大職缺技能與本專案對照 (JD Capability Matrix)

- **高級應用開發與重構 (Software Engineering & Refactoring)**：FastAPI、REST API、OOP/FP 範式、12-Factor 原則、測試金字塔 (Unit / Integration Tests)。
- **雲原生微服務與 Kubernetes (Cloud-Native & K8s)**：Docker、Kubernetes、Istio (Service Mesh)、ArgoCD (GitOps)、Helm/Kustomize、HPA 自動擴縮。
- **SRE 可觀測性 (Observability & SRE)**：Prometheus、Grafana、Alertmanager、PromQL、SLI/SLO/SLA 定義、Error Budget 燃燒率與事故復盤 (Postmortem)。
- **大數據與 NoSQL 資料工程 (Data Infrastructure)**：PostgreSQL、MariaDB、MongoDB、Cassandra、MinIO (S3 物件儲存)、PySpark 巨量數據處理。
- **AI 平台與 MLOps (AI/MLOps Platform)**：特徵工程 (Feature Pipeline)、MLflow 實驗追蹤與模型註冊、Data Drift 數據偏移檢測、線上 API 推論服務 (Model Serving)。
- **B2B 多租戶與 SaaS 商業化 (SaaS Monetization)**：Multi-Tenancy 租戶隔離、Stripe 金流連動、API Key 限流與按用量計費 (Usage-Based Billing)。

---

## 🗓️ 30 天每日詳細學習與實作路線圖 (30-Day Masterclass Roadmap)

> 📘 **完整詳細課綱請參閱 [`docs/learning-roadmap.md`](docs/learning-roadmap.md)**
> 
> 每天課程包含 **6 大完整區塊**：📖 核心觀念（3~5 個概念深度講解）→ 📚 延伸知識（業界實戰案例）→ 🔨 實作練習（3 道漸進式練習題 A/B/C）→ 🧪 測試驗證（pytest 測試案例 + 完成條件）→ 🗣️ 面試問答（5~8 題附標準答案）→ 📎 參考資源

### 📌 第一週：軟體工程基本功、12-Factor 與生產級單體架構

#### Day 01 — HTTP, REST API, FastAPI & Git 工作流
- **📖 學習內容 (Learn)**: Client/Server 模型、IP/Port/URL、HTTP Methods (GET/POST/PUT/DELETE)、Status Codes (2xx/4xx/5xx)、REST 冪等性、FastAPI 工廠模式 (`create_app`)。
- **🔨 程式實作 (Build)**: 實作 `/health` 端點，建立 Git 倉庫並配置 `.gitignore` 與預備 CI 本地驗證環境。
- **✅ 驗證方式 (Verify)**: 執行 `uvicorn app.main:app` 並發送 `curl http://127.0.0.1:8000/health` 回傳 `200 OK` 及 JSON 配置。
- **🗣️ 面試考點 (Explain)**: 說明 Client 與 Server 的互動流程，以及為何 GET 請求不應產生狀態副作用。

#### Day 02 — OOP 物件導向、FP 函數式風格與系統分層
- **📖 學習內容 (Learn)**: Class vs Object、封裝、函數式 Immutable Data、Router ➔ Service ➔ Repository 職責分離與依賴反轉。
- **🔨 程式實作 (Build)**: 設計 `MarketKeyword` 與 `ProductMetric` 領域模型，實現分層介面。
- **✅ 驗證方式 (Verify)**: 執行 `pytest tests/test_market_saas.py` 驗證 Router 與 Service 模組獨立解耦。
- **🗣️ 面試考點 (Explain)**: 說明為何 API Router 層不應直接包含業務邏輯或資料庫操作。

#### Day 03 — 關聯式 SQL 與 12-Factor 配置管理
- **📖 學習內容 (Learn)**: PostgreSQL Table/PK/FK/ACID 事務與 Index 索引優化；12-Factor 的 Config 與 Code 分離原則。
- **🔨 程式實作 (Build)**: 使用 `SQLAlchemy` + `pydantic-settings` 讀取 `.env` 環境變數。
- **✅ 驗證方式 (Verify)**: 修改 `.env` 的 `FACTORY_ENVIRONMENT` 變數，重啟後存取 `/health` 驗證配置隔離。
- **🗣️ 面試考點 (Explain)**: 說明硬編碼配置在不同環境 (Dev/Staging/Prod) 部署時所帶來的安全與維護風險。

#### Day 04 — 測試金字塔 (Testing Pyramid & TDD)
- **📖 學習內容 (Learn)**: Unit vs Integration vs E2E 測試、Arrange/Act/Assert 結構、Mocking 技巧與 Code Coverage 覆蓋率。
- **🔨 程式實作 (Build)**: 撰寫 `pytest` 套件、FastAPI TestClient API 整合測試。
- **✅ 驗證方式 (Verify)**: 執行 `python -m pytest`，確保單元測試與 API 整合測試 100% 綠燈通過。
- **🗣️ 面試考點 (Explain)**: 說明單元測試與整合測試在發掘 Bug 成本上的差異。

#### Day 05 — 重構 (Refactoring) 與 SOLID 原則
- **📖 學習內容 (Learn)**: Single Responsibility, Open/Closed, Interface Segregation 原則與 Code Smell 識別。
- **🔨 程式實作 (Build)**: 重構關鍵字查詢與數據存取邏輯，提高程式碼內聚度與可維護性。
- **✅ 驗證方式 (Verify)**: 執行 `pytest` 驗證重構前後外部 API 行為與回傳格式 100% 一致。
- **🗣️ 面試考點 (Explain)**: 說明「重構 (Refactoring)」與「重新編寫 (Rewriting)」在工程實踐上的區別。

#### Day 06 — 演算法、資料結構與記憶體限流 (Algorithms)
- **📖 學習內容 (Learn)**: 時間/空間複雜度 (Big-O)、Sliding Window 限流演算法、LRU Cache 與 Hash Table 機制。
- **🔨 程式實作 (Build)**: 手寫 Sliding Window 記憶體限流器中間件。
- **✅ 驗證方式 (Verify)**: 短時間連續發送 101 次請求，驗證精準拋出 `429 Too Many Requests`。
- **🗣️ 面試考點 (Explain)**: 說明 Sliding Window 與 Token Bucket 兩種限流演算法的優缺點。

#### Day 07 — 第一週單體架構驗收與 Code Review
- **📖 學習內容 (Learn)**: Monolith 演進至微服務的 Tradeoffs (延遲、網路邊界、維護成本)。
- **🔨 程式實作 (Build)**: 完成生產級單體市場調查 API 系統，產出架構圖 v1，模擬 Code Review 檢查機制。
- **✅ 驗證方式 (Verify)**: 執行全套端到端流轉，驗證各分層運作順暢。
- **🗣️ 面試考點 (Explain)**: 說明為何初創專案適合從單體架構開始而非直接構建微服務。

---

### 📌 第二週：商業多租戶、金流計費、數據管道與微服務拆分

#### Day 08 — 多租戶隔離 (Multi-Tenancy) & B2B 授權
- **📖 學習內容 (Learn)**: Multi-Tenant 租戶隔離模式、API Key 發放與權限控管 (RBAC)。
- **🔨 程式實作 (Build)**: 建立 `Tenant` 與 `SubscriptionTier` 模型，實作 `X-API-Key` 鑑權中間件。
- **✅ 驗證方式 (Verify)**: 帶入無效 API Key 發送請求，驗證 `401 Unauthorized` 攔截，且不同 Tenant 數據完全隔離。
- **🗣️ 面試考點 (Explain)**: 說明如何確保 B2B SaaS 多租戶架構下資料不會發生跨租戶滲漏。

#### Day 09 — Stripe 金流整合與 Usage-Based Billing
- **📖 學習內容 (Learn)**: 按量計費 (Usage-Based Billing) 商業模式、Stripe Webhook 處理機制。
- **🔨 程式實作 (Build)**: 建立 `/api/v1/billing/subscribe` 金流端點，達到月配額時拋出 `402 Payment Required`。
- **✅ 驗證方式 (Verify)**: 模擬試用版配額用盡後自動封鎖，呼叫 `/subscribe` 成功提升配額與重置 API Key。
- **🗣️ 面試考點 (Explain)**: 說明按量計費與固定訂閱制在後端計量扣額上的設計差異。

#### Day 10 — Docker 容器化與最佳化 Dockerfile
- **📖 學習內容 (Learn)**: Image vs Container、Layer 快取優化、Multi-Stage Build 多階段構建、Non-root 安全容器。
- **🔨 程式實作 (Build)**: 編寫最小化生產級 Dockerfile 並在本地運行。
- **✅ 驗證方式 (Verify)**: 執行 `docker build -t market-api .` 與 `docker run` 驗證容器輕量化與啟動成功。
- **🗣️ 面試考點 (Explain)**: 說明 Docker 多階段構建 (Multi-Stage Build) 如何有效減少最終鏡像體積。

#### Day 11 — Docker Compose & Redis 快取機制
- **📖 學習內容 (Learn)**: 容器網路 (Bridge)、Service Discovery、Redis Cache-Aside 模式與 TTL 機制。
- **🔨 程式實作 (Build)**: Compose 整合 API + PostgreSQL + Redis 快取熱門關鍵字聲量。
- **✅ 驗證方式 (Verify)**: 執行 `docker-compose up`，發送二次相同查詢，驗證回應時間縮短至 <5ms (Redis 命中)。
- **🗣️ 面試考點 (Explain)**: 說明 Cache-Aside 模式與 Cache Penetration (快取穿透) 的因應策略。

#### Day 12 — 分散式 NoSQL 資料庫實務 (MongoDB / MariaDB)
- **📖 學習內容 (Learn)**: Document-oriented NoSQL 特性、Schema-less 靈活性與查詢效能。
- **🔨 程式實作 (Build)**: 使用 MongoDB 儲存非結構化網路貼文與評價數據。
- **✅ 驗證方式 (Verify)**: 執行 MongoDB 存取腳本，驗證多型貼文 JSON 數據成功寫入與多維度查詢。
- **🗣️ 面試考點 (Explain)**: 說明在什麼情境下選擇 SQL (Relational) 與 NoSQL (Document Store)。

#### Day 13 — 大數據批次與串流管道 (Hadoop / PySpark)
- **📖 學習內容 (Learn)**: Hadoop 生態系、MapReduce 原理、PySpark 巨量數據平行處理。
- **🔨 程式實作 (Build)**: 編寫 PySpark 腳本進行巨量聲量數據清洗與詞頻特徵抽取。
- **✅ 驗證方式 (Verify)**: 執行 PySpark 批次腳本，驗證巨量聲量數據成功清洗並產出詞頻特徵統計。
- **🗣️ 面試考點 (Explain)**: 說明 Batch Processing (批次) 與 Stream Processing (串流) 的適用情境。

#### Day 14 — 微服務邊界拆分 (Monolith to Microservices)
- **📖 學習內容 (Learn)**: Bounded Context 領域邊界、Database-per-Service 模式、API Contract。
- **🔨 程式實作 (Build)**: 將「數據抓取 (Scraper Ingestion)」從單體系統拆分為獨立微服務與非同步 Worker。
- **✅ 驗證方式 (Verify)**: 啟動 Scraper Ingestion 微服務，發送跨服務 REST 請求驗證解耦運作。
- **🗣️ 面試考點 (Explain)**: 說明微服務拆分帶來的網路延遲與分散式事務 (Distributed Transaction) 挑戰。

---

### 📌 第三週：Kubernetes 雲原生編排、Service Mesh (Istio)、GitOps (ArgoCD) 與 SRE

#### Day 15 — Kubernetes (K8s) 核心編排
- **📖 學習內容 (Learn)**: Cluster, Pod, Deployment, Service, ConfigMap, Secret 核心概念。
- **🔨 程式實作 (Build)**: 將 API 部署至 local K8s (kind / minikube)。
- **✅ 驗證方式 (Verify)**: 執行 `kubectl get pods,svc` 驗證 API 與 DB 順利部署至 Kubernetes 叢集。
- **🗣️ 面試考點 (Explain)**: 說明 Kubernetes 的 desired state (期望狀態) 與 reconciliation loop (調和循環)。

#### Day 16 — K8s 健康檢查 (Probes) 與優雅關機
- **📖 學習內容 (Learn)**: Liveness, Readiness, Startup Probes 運作機制與 SIGTERM 訊號處理。
- **🔨 程式實作 (Build)**: 配置探針與 Pod 優雅關機。
- **✅ 驗證方式 (Verify)**: 模擬 API 端點死鎖，觀察 Kubernetes Readiness/Liveness Probes 自動觸發容器重啟。
- **🗣️ 面試考點 (Explain)**: 說明 Liveness Probe 與 Readiness Probe 的差異與配置失誤後果。

#### Day 17 — K8s 自動擴縮 (HPA) 與資源配額
- **📖 學習內容 (Learn)**: Horizontal Pod Autoscaler (HPA)、CPU/Memory Requests & Limits。
- **🔨 程式實作 (Build)**: 設定 HPA 並使用高併發流量觸發 Pod 自動擴展。
- **✅ 驗證方式 (Verify)**: 使用壓測工具灌入流量，執行 `kubectl get hpa` 驗證 Pod 數量從 1 自動擴展至 5。
- **🗣️ 面試考點 (Explain)**: 說明為什麼在 Kubernetes 中必須設定 Resource Requests 與 Limits。

#### Day 18 — Service Mesh (Istio) 流量管理與金絲雀部署
- **📖 學習內容 (Learn)**: Istio Envoy Sidecar, VirtualService, DestinationRule, Canary Deployment (金絲雀發布) 與 Circuit Breaker (斷路器)。
- **🔨 程式實作 (Build)**: 設定 Istio 將 10% 流量導入新版 API。
- **✅ 驗證方式 (Verify)**: 配置 Istio VirtualService，連發 100 次請求驗證 10% 流量精準分流至 Canary 新版。
- **🗣️ 面試考點 (Explain)**: 說明 Service Mesh 在微服務架構中扮演的角色與價值。

#### Day 19 — GitOps (ArgoCD) 與 Helm/Kustomize 包裹
- **📖 學習內容 (Learn)**: GitOps 聲明式部署、Single Source of Truth 理念、ArgoCD 狀態調和。
- **🔨 程式實作 (Build)**: 使用 Helm/Kustomize 包裹 K8s 清單，設定 ArgoCD 自動同步 Git 變更。
- **✅ 驗證方式 (Verify)**: 修改 Git 倉庫的 K8s 清單並 push，觀察 ArgoCD 控制台自動同步至 K8s 實體叢集。
- **🗣️ 面試考點 (Explain)**: 說明 GitOps 比起傳統腳本部署在可稽核性與 Rollback 上的優勢。

#### Day 20 — CI/CD 自動化 Toolchain (GitHub Actions)
- **📖 學習內容 (Learn)**: CI vs CD、Quality Gates、Immutable Build Artifacts。
- **🔨 程式實作 (Build)**: 建立 GitHub Actions Workflow (Lint ➔ Pytest ➔ Docker Build ➔ ArgoCD Trigger)。
- **✅ 驗證方式 (Verify)**: 提交 GitHub PR，驗證 Actions 綠燈觸發 (Lint ➔ Pytest ➔ Docker Build ➔ ArgoCD)。
- **🗣️ 面試考點 (Explain)**: 說明不可變產物 (Immutable Artifacts) 在 CI/CD 流程中的安全性。

#### Day 21 — SRE 可觀測性 (Prometheus & PromQL)
- **📖 學習內容 (Learn)**: RED (Rate, Errors, Duration) 與 USE 監控方法學、PromQL 查詢語言。
- **🔨 程式實作 (Build)**: 在 FastAPI 埋點 `/metrics`，使用 Prometheus 抓取 API 延遲與錯誤率。
- **✅ 驗證方式 (Verify)**: 存取 `http://localhost:9090`，使用 PromQL 查詢 `rate(http_requests_total[5m])` 延遲曲線。
- **🗣️ 面試考點 (Explain)**: 說明 Pull 模型 (Prometheus) 與 Push 模型監控架構的比較。

#### Day 22 — Grafana 視覺化 Dashboard & Alertmanager
- **📖 學習內容 (Learn)**: Dashboard 設計原則、Alerting 告警觸發規則與 Alertmanager。
- **🔨 程式實作 (Build)**: 建立高顏值 Grafana 控制台，設定 Alertmanager 當 5xx 錯誤率 > 1% 時發送 Slack/Email 告警。
- **✅ 驗證方式 (Verify)**: 開啟 Grafana 控制台，故意引發 5xx 錯誤，驗證 Alertmanager 成功發送 Slack 告警。
- **🗣️ 面試考點 (Explain)**: 說明警報疲勞 (Alert Fatigue) 的成因與預防告警雜訊的方法。

#### Day 23 — SRE SLI/SLO/SLA 與 Error Budget 扣減
- **📖 學習內容 (Learn)**: SLI (指標), SLO (目標), SLA (協議) 與 Error Budget 殘餘預算計算。
- **🔨 程式實作 (Build)**: 定義「API 成功率 >= 99.9%」與「p95 延遲 < 200ms」之 SLO，建立 Error Budget 燃燒率儀表板。
- **✅ 驗證方式 (Verify)**: 查看 Grafana SLO 面板，驗證 7 天滾動可用性 (>=99.9%) 與 Error Budget 燃燒率計算。
- **🗣️ 面試考點 (Explain)**: 說明 Error Budget 如何平衡軟體新功能開發與系統穩定度。

---

### 📌 第四週：AI/MLOps 平台、物件儲存 (MinIO/Cassandra)、研報自動化與生產故障演練

#### Day 24 — S3 / MinIO 物件儲存與數據治理
- **📖 學習內容 (Learn)**: Unstructured Data 物件儲存、S3 API、Metadata 數據治理與品質管理。
- **🔨 程式實作 (Build)**: 部署 MinIO，儲存原始貼文數據與 AI 模型權重檔 (Artifacts)。
- **✅ 驗證方式 (Verify)**: 透過 Python SDK (boto3) 上傳與讀取 MinIO 中的貼文資料與模型 Artifacts 物件。
- **🗣️ 面試考點 (Explain)**: 說明 Block Storage, File Storage 與 Object Storage 的架構適用性。

#### Day 25 — AI/ML 生命週期與特徵工程 (Feature Pipeline)
- **📖 學習內容 (Learn)**: ML 生命週期（數據收集 ➔ 探索 ➔ 特徵工程 ➔ 訓練 ➔ 評估）、Data Drift (資料偏移)。
- **🔨 程式實作 (Build)**: 建立 NLP 情感分析特徵管道，計算 Sentiment Vector 並監控數據偏移。
- **✅ 驗證方式 (Verify)**: 執行 Data Drift 檢測腳本，輸出 KS-test 數據偏移統計結果與特徵矩陣。
- **🗣️ 面試考點 (Explain)**: 說明 Data Drift 與 Concept Drift 的差異及其對生產模型效能的影響。

#### Day 26 — MLOps / MLflow 模型註冊與管理 (Model Registry)
- **📖 學習內容 (Learn)**: Experiment Tracking (實驗追蹤)、Model Registry (模型註冊庫)、版本控管與可重複性。
- **🔨 程式實作 (Build)**: 使用 MLflow 記錄模型參數、AUC/Accuracy 指標並註冊 Selected Model。
- **✅ 驗證方式 (Verify)**: 存取 `http://localhost:5000` (MLflow UI)，驗證模型實驗追蹤、AUC 指標與 Selected 版本註冊。
- **🗣️ 面試考點 (Explain)**: 說明 MLflow 如何保障 ML 模型的試驗可追蹤性與可重複訓練。

#### Day 27 — 線上 AI 推論服務 (Online Model Serving API)
- **📖 學習內容 (Learn)**: Online Inference 延遲優化、Model Serialization、符合 SLO 的高可用推論。
- **🔨 程式實作 (Build)**: 公開 `/api/v1/predict` 端點，載入 MLflow 註冊的模型進行實時推論。
- **✅ 驗證方式 (Verify)**: 發送 POST 至 `/api/v1/predict`，驗證 AI 即時回傳情感分類與預測信心分數。
- **🗣️ 面試考點 (Explain)**: 說明 Online Real-time Inference 與 Batch Offline Inference 在延遲要求上的權衡。

#### Day 28 — 高管 PDF 商業研報與現代化 Web 控制台
- **📖 學習內容 (Learn)**: 資料視覺化、使用者體驗 (UX) 第一印象 (WOW Factor)、PDF 動態渲染。
- **🔨 程式實作 (Build)**: 實作 `/api/v1/reports/html/{id}` 自動生成 PDF 研報；建置深色系 ECharts 市場調查 Dashboard。
- **✅ 驗證方式 (Verify)**: 瀏覽器開啟 `http://127.0.0.1:8000/` 體驗儀表板，並存取 `/api/v1/reports/html/K-001` 下載 PDF 研報。
- **🗣️ 面試考點 (Explain)**: 說明全棧數據可視化面板在展現產品商業價值時的重要性。

#### Day 29 — 生產環境故障演練 (Production Incident Exercise)
- **📖 學習內容 (Learn)**: Chaos Engineering 故障注入、故障排除流程與 Postmortem 復盤報告撰寫。
- **🔨 程式實作 (Build)**: 注入 500ms 網路延遲與 Redis 連線中斷，利用 Grafana + 日誌定位根因並完成復原。
- **✅ 驗證方式 (Verify)**: 注入 500ms 網路延遲與 Redis 中斷，使用 Grafana + 日誌定位根因並撰寫事故 Postmortem。
- **🗣️ 面試考點 (Explain)**: 說明如何在故障發生時進行根因分析 (RCA - Root Cause Analysis)。

#### Day 30 — 專案封裝、技術展演與履歷/面試 Demo
- **📖 學習內容 (Learn)**: 如何向面試官精準展示架構權衡 (Tradeoffs) 與個人專案亮點。
- **🔨 程式實作 (Build)**: 整理最終版 README (繁體中文)、架構演進圖，錄製 Demo 影片，對照 5 大 JDs 自我模擬面試答辯。
- **✅ 驗證方式 (Verify)**: 錄製完整 Demo 影片、對照 5 大 JDs 自我模擬面試答辯，達成 100% Portfolio-Ready。
- **🗣️ 面試考點 (Explain)**: 針對 5 大 JDs 提出之核心考點進行流利答辯。

---

## 🏗️ 系統目標架構圖 (Target Architecture)

```text
網路公開數據源 (HackerNews / Public News / Social APIs)
                              |
                              v
                 FastAPI / Gateway API Router
                              |
           +------------------+------------------+
           | Auth & API Key   | Multi-Tenancy    | Stripe Billing
           | Rate Limiting    | DB Isolation     | Usage Quota Check
           +------------------+------------------+
                              |
                     +--------+--------+
                     |                 |
                     v                 v
               PostgreSQL            Redis (熱門關鍵字快取/Rate Limit)
                     |
       +-------------+---------------------+
       |                                   |
       v                                   v
 PySpark / Feature Pipeline           AI Sentiment Inference (MLflow Registry)
       |                                   |
       v                                   v
 MinIO (S3 Object Storage)            Executive PDF Report Generator
       |                                   |
       +-----------------+-----------------+
                         |
                         v
          Kubernetes + Istio + ArgoCD GitOps
                         |
           Prometheus + Grafana Monitoring
```

---

## 💻 本地端快速執行 (Run Locally)

建議使用 **Python 3.12+**。

### 1. 啟動 Python 虛擬環境

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. 安裝套件與執行測試

```bash
pip install -e ".[dev]"
python -m pytest
```

### 3. 啟動 FastAPI 服務與儀表板

```bash
uvicorn app.main:app --reload
```

啟動後即可存取：
- **Web SaaS 儀表板**：`http://127.0.0.1:8000/`
- **Swagger API 文件**：`http://127.0.0.1:8000/docs`
- **健康檢查 Health Check**：`http://127.0.0.1:8000/health`
- **一頁式高管 PDF 研報預覽**：`http://127.0.0.1:8000/api/v1/reports/html/K-001`

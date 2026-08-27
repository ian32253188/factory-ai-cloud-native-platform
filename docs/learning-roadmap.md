# 30 天頂尖職缺對照實戰學習路線圖 (30-Day Masterclass Roadmap)

本路線圖遵循 **學習 (Learn) ➔ 實作 (Build) ➔ 驗證 (Verify) ➔ 解說 (Explain)** 的閉環學習流程，全面對照 5 大頂尖職缺要求。

每天課程包含 **6 大完整區塊**：

| 區塊 | 說明 |
|------|------|
| 📖 核心觀念 | 3~5 個關鍵概念深度講解，附類比與圖示 |
| 📚 延伸知識 | 進階知識點、業界實戰案例與最佳實踐 |
| 🔨 實作練習 | 練習 A（引導式）→ B（半自主）→ C（挑戰題），每道附驗證指令 |
| 🧪 測試驗證 | pytest 測試案例 + 完成條件 (Definition of Done) |
| 🗣️ 面試問答 | 5~8 題面試必考題，附標準答案要點 |
| 📎 參考資源 | 官方文件、推薦閱讀 |

---
---

# 📌 第一週：軟體工程基本功、12-Factor 與生產級單體架構

---

## Day 01 — HTTP, REST API, FastAPI & Git 工作流

### 📖 核心觀念 (Core Concepts)

#### 1. Client / Server 模型（客戶端 / 伺服器模型）
- **Client (客戶端)**：發出請求的一方，例如瀏覽器、curl、手機 App。
- **Server (伺服器)**：監聽網路埠口、接收請求並回傳結果的一方。
- 類比：**餐廳模型** — Client 是點菜的客人，Server 是廚房，HTTP 是服務生在兩者之間傳遞點單與餐點。

```text
Client (瀏覽器/curl)
     |
     | HTTP GET /health
     v
Server (FastAPI + Uvicorn)
     |
     | JSON Response
     v
Client 收到結果
```

#### 2. HTTP 協定基礎
- **IP 位址 (IP Address)**：用來識別網路中的一台主機（例如 `127.0.0.1` 代表「本機」）。
- **Port 埠口**：用來識別主機上的某一個服務（例如 `8000` 代表你的 FastAPI 伺服器）。
- **URL 統一資源定位符**：完整描述「在哪台主機的哪個埠口存取哪個資源」。
- **HTTP (HyperText Transfer Protocol)**：應用層通訊協定，定義了請求 (Request) 和回應 (Response) 的格式與語意。

#### 3. HTTP Methods（HTTP 動詞）
| 方法 | 用途 | 是否冪等 | 是否安全 |
|------|------|----------|----------|
| `GET` | 讀取資源 | ✅ 是 | ✅ 是 |
| `POST` | 建立資源或觸發操作 | ❌ 否 | ❌ 否 |
| `PUT` | 整體替換資源 | ✅ 是 | ❌ 否 |
| `PATCH` | 部分更新資源 | ❌ 否 | ❌ 否 |
| `DELETE` | 刪除資源 | ✅ 是 | ❌ 否 |

#### 4. HTTP Status Codes（HTTP 狀態碼）
- **2xx 成功**：`200 OK`、`201 Created`、`204 No Content`
- **4xx 客戶端錯誤**：`400 Bad Request`、`401 Unauthorized`、`403 Forbidden`、`404 Not Found`、`422 Unprocessable`、`429 Too Many Requests`
- **5xx 伺服器錯誤**：`500 Internal Server Error`、`503 Service Unavailable`

#### 5. REST 架構風格與冪等性 (Idempotency)
- **REST (Representational State Transfer)**：以資源為中心的 API 設計風格，URL 代表資源、HTTP 動詞代表操作。
- **冪等性**：同一個請求發送一次跟發送一百次，對伺服器產生的「最終效果」完全相同。為什麼重要？因為分散式系統中網路會超時、客戶端會重試。

### 📚 延伸知識 (Deep Dive)

#### 1. FastAPI 的自動化魔法
FastAPI 在背後自動完成了以下工作：
1. 註冊路由 (Route Registration)
2. 匹配傳入的 HTTP 請求
3. 呼叫對應的 Python 函式
4. 自動將 Python 字典序列化為 JSON
5. 建構 HTTP 回應
6. **自動生成 OpenAPI/Swagger 互動式文件**

#### 2. 應用程式工廠模式 (Application Factory Pattern)
不直接在模組層級建立 `app` 物件，而是透過 `create_app()` 函式建立：
- 更易於測試（每次可建立全新實例）
- 更清晰的應用組裝流程
- 為後續環境特化配置預留空間

#### 3. 為什麼配置不應寫死在程式碼裡 (12-Factor: Config)
`app/core/config.py` 從環境變數讀取設定值。這讓同一份程式碼能在 Development、Staging、Production 環境中以不同設定運行，直接連結 12-Factor App 原則的第三條。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：啟動服務與 Swagger UI 體驗（引導式）
1. 建立並啟動 Python 虛擬環境：
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # Windows PowerShell
   pip install -e ".[dev]"
   ```
2. 啟動 Uvicorn 開發伺服器：
   ```bash
   uvicorn app.main:app --reload
   ```
3. 在瀏覽器開啟以下頁面：
   - Swagger UI：`http://127.0.0.1:8000/docs`
   - Health 端點：`http://127.0.0.1:8000/health`
4. 在 PowerShell 使用 `curl.exe` 測試：
   ```bash
   curl.exe http://127.0.0.1:8000/health
   ```
5. **預期結果**：回傳 `{"status":"ok","service":"Market Intelligence...","environment":"development"}`

#### 練習 B：新增 Query Parameter 端點（半自主）
1. 在 `app/api/health.py` 中新增 `/health/detail` 端點。
2. 支援 `?verbose=true` 查詢參數。
3. 當 `verbose=true` 時，額外回傳 `timestamp`、`environment`、`mode` 欄位。
4. **驗證指令**：
   ```bash
   curl.exe "http://127.0.0.1:8000/health/detail?verbose=true"
   ```
5. **預期結果**：回傳的 JSON 中包含 `"timestamp"` 與 `"mode": "verbose_diagnostic"`。

#### 練習 C：自行建立市場關鍵字查詢端點（挑戰題）
1. 在 `app/api/` 中建立一個新的 Router 檔案。
2. 實作 `GET /api/v1/keywords/search`。
3. 支援 `?q=AI` 查詢參數，從記憶體列表中搜尋關鍵字。
4. 回傳匹配的關鍵字列表與匹配數量。
5. 未傳入 `q` 時回傳全部關鍵字。
6. **驗證指令**：
   ```bash
   curl.exe "http://127.0.0.1:8000/api/v1/keywords/search?q=AI"
   ```
7. **預期結果**：回傳包含 `"total"` 欄位與匹配的關鍵字陣列。

### 🧪 測試驗證 (Test & Verify)

```python
# 練習 B 的測試
def test_health_detail_basic():
    response = client.get("/health/detail")
    assert response.status_code == 200
    assert "timestamp" not in response.json()

def test_health_detail_verbose():
    response = client.get("/health/detail?verbose=true")
    assert response.status_code == 200
    payload = response.json()
    assert "timestamp" in payload
    assert payload["mode"] == "verbose_diagnostic"

# 練習 C 的測試
def test_keywords_search_with_query():
    response = client.get("/api/v1/keywords/search?q=AI")
    assert response.status_code == 200
    payload = response.json()
    assert "total" in payload
    assert payload["total"] >= 0
```

**完成條件 (Definition of Done)**：
- [ ] 服務啟動成功，`/health` 回傳 200
- [ ] `python -m pytest` 全數通過
- [ ] 已在 Swagger UI 中互動測試過至少 2 個端點
- [ ] 已使用 `curl.exe` 在 Terminal 中測試成功
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：HTTP 和 REST 有什麼不同？**
> HTTP 是一種**通訊協定**（規定訊息怎麼傳遞的格式）；REST 是一種**架構風格**（規定 API 應該怎麼設計），REST 通常建立在 HTTP 之上，但兩者不是同一件事。

**Q2：為什麼 GET 請求應該是「安全」的？**
> 安全 (Safe) 代表這個操作不應產生任何副作用（不修改伺服器狀態）。因為搜尋引擎爬蟲、CDN 快取都會自動發送 GET 請求，如果 GET 會修改資料，會導致不可預期的資料變動。

**Q3：什麼是冪等性 (Idempotency)？為什麼重試機制讓它變得重要？**
> 冪等性代表同一個操作執行一次和執行多次的最終效果相同。在分散式系統中，網路可能超時但伺服器其實已經處理完畢，客戶端會重試，如果操作不冪等，重試可能導致重複建立資源。

**Q4：404 和 500 的差別是什麼？**
> `404 Not Found` 是**客戶端錯誤**，代表你請求的資源不存在（通常是 URL 打錯）。`500 Internal Server Error` 是**伺服器錯誤**，代表伺服器程式碼出了 Bug 或例外未被捕獲。

**Q5：什麼是 Health Endpoint？為什麼每個微服務都需要它？**
> Health Endpoint 回答一個簡單問題：「這個服務是否活著且能正常處理請求？」。Kubernetes 的 Liveness/Readiness Probe 會持續檢查這個端點，決定是否要重啟或將流量導走。

**Q6：為什麼配置應該來自環境變數而非寫死在程式碼裡？**
> 12-Factor App 第三條原則：配置與程式碼分離。同一份程式碼部署到不同環境（開發/測試/生產）應該只改環境變數，不改程式碼。寫死的配置會導致機密外洩風險和部署僵化。

**Q7：寫測試的目的是什麼？為什麼要在重構之前先寫好測試？**
> 測試保護的是「外部可觀察行為」。如果我們在重構前就有測試覆蓋，重構後跑測試全通過，就能有信心知道重構沒有破壞任何功能。

**Q8：從 `curl /health` 到收到 JSON 回應，中間發生了什麼事？**
> 1) curl 建立 TCP 連線到 127.0.0.1:8000 → 2) 發送 HTTP GET 請求 → 3) Uvicorn 接收請求轉交 FastAPI → 4) FastAPI 匹配路由找到 `health_check()` 函式 → 5) 執行函式取得 Python 字典 → 6) 序列化為 JSON → 7) 建構 HTTP 200 回應 → 8) 透過 TCP 回傳給 curl。

### 📎 參考資源 (References)

- [FastAPI 官方教學](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI 測試文件](https://fastapi.tiangolo.com/tutorial/testing/)
- [MDN HTTP 概覽](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [HTTP 語意規範 RFC 9110](https://www.rfc-editor.org/rfc/rfc9110)
- [12-Factor App](https://12factor.net/)
- [GitHub Git 手冊](https://docs.github.com/en/get-started/using-git/about-git)

---

## Day 02 — OOP 物件導向、FP 函數式風格與系統分層

### 📖 核心觀念 (Core Concepts)

#### 1. 物件導向程式設計 (OOP) 四大支柱
- **封裝 (Encapsulation)**：把資料與操作資料的方法包在同一個 class 裡，外部只透過公開方法存取。
- **抽象 (Abstraction)**：隱藏實作細節，只暴露必要的介面。
- **繼承 (Inheritance)**：子類別自動獲得父類別的屬性與方法（Python 中少用深層繼承，偏好組合）。
- **多型 (Polymorphism)**：不同類別的物件可以用相同的介面呼叫，各自產生不同行為。

#### 2. 函數式程式設計 (FP) 核心理念
- **Immutability (不可變性)**：資料一旦建立就不修改，需要變更時建立新副本。
- **Pure Function (純函式)**：相同輸入永遠產生相同輸出，且無副作用。
- **First-class Function (一等公民函式)**：函式可以當作參數傳遞、當作回傳值。
- **Python 中的 FP 工具**：`map()`、`filter()`、`lambda`、`functools.reduce()`。

#### 3. 三層分層架構 (3-Tier Architecture)
```text
[ 客戶端 請求 ]
       │
       ▼
1. Router 層 (API 控制層)   ── 職責：接收 HTTP、驗參、回 JSON
       │
       ▼
2. Service 層 (業務邏輯層)  ── 職責：演算法、AI 推論、商業規則
       │
       ▼
3. Repository 層 (資料存取層) ── 職責：對 DB / 外部 API 讀寫
```

#### 4. 依賴反轉原則 (Dependency Inversion Principle)
- **高層模組不應依賴低層模組，兩者都應依賴抽象**。
- 範例：Service 層不直接 `import PostgreSQL driver`，而是依賴一個 `Repository` 抽象介面，實際使用哪個資料庫由外部注入。

#### 5. Pydantic 領域模型 (Domain Models)
- 使用 `pydantic.BaseModel` 定義強型別資料結構。
- 自動進行型別校驗、序列化、文件生成。
- 在本專案中 `MarketKeyword`、`Tenant`、`SubscriptionTier` 都是 Pydantic 模型。

### 📚 延伸知識 (Deep Dive)

#### 1. 高內聚、低耦合 (High Cohesion, Low Coupling)
- **高內聚**：同一模組內的程式碼彼此高度相關，專注完成單一使命。
- **低耦合**：不同模組之間依賴最小化，修改 A 模組不會破壞 B 模組。
- **分層架構如何實現**：Router 層只知道 Service 層的介面，不知道 Repository 層的存在，因此更換資料庫時 Router 層完全不受影響。

#### 2. OOP vs FP：不是二選一，而是混用
| 情境 | 選擇 OOP | 選擇 FP |
|------|----------|---------|
| 有狀態的實體（使用者、訂單） | ✅ 類別封裝 | |
| 無狀態的資料轉換（ETL、計算） | | ✅ 純函式 |
| 複雜的業務邏輯引擎 | ✅ 策略模式 | ✅ 高階函式 |

Python 是多範式語言，業界最佳實踐是 **OOP 做結構骨架，FP 做資料轉換邏輯**。

#### 3. FastAPI 的依賴注入 (Dependency Injection)
FastAPI 的 `Depends()` 機制就是一種輕量級 DI：
```python
@router.get("/sentiment/{id}")
def analyze(id: str, tenant: Tenant = Depends(get_current_tenant)):
    ...
```
`get_current_tenant` 函式會在每次請求時被自動呼叫，注入認證過的租戶物件。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：閱讀並理解現有分層架構（引導式）
1. 依序開啟以下 3 個檔案，理解三層架構的實際程式碼：
   - `app/api/market.py`（Router 層）
   - `app/services/ai_sentiment.py`（Service 層）
   - `app/models/market.py`（Domain Model 層）
2. 畫出三個檔案之間的呼叫關係圖（手畫或文字皆可）。
3. **驗證方式**：能用自己的話向別人解釋「為什麼 `market.py` 不直接寫 AI 演算法？」。

#### 練習 B：獨立測試 Service 層（半自主）
1. 在 `tests/test_market_saas.py` 中新增一個測試函式 `test_ai_sentiment_engine_positive_case()`。
2. 建立一個 `mock_data` 字典，其中 `sentiment_index = 0.85`、`negative_pct = 5.0`。
3. 呼叫 `ai_sentiment.analyze_market_trend(mock_data)` 並斷言回傳的 `status` 是 `"positive"`。
4. **驗證指令**：
   ```bash
   python -m pytest tests/test_market_saas.py -v -k "positive"
   ```
5. **預期結果**：`test_ai_sentiment_engine_positive_case PASSED`。

#### 練習 C：實作新的 Service 層函式（挑戰題）
1. 在 `app/services/ai_sentiment.py` 中新增一個方法 `generate_summary(keyword_data: dict) -> str`。
2. 此方法根據 `sentiment_index` 的高低，回傳不同的中文摘要文字。
3. 在 Router 層 (`app/api/market.py`) 中呼叫此方法，在回傳的 JSON 中加入 `"summary"` 欄位。
4. 撰寫對應的單元測試。
5. **驗證指令**：
   ```bash
   python -m pytest -v
   curl.exe http://127.0.0.1:8000/api/v1/market/sentiment/K-001
   ```
6. **預期結果**：API 回傳的 JSON 中出現 `"summary"` 欄位。

### 🧪 測試驗證 (Test & Verify)

```python
from app.services.ai_sentiment import ai_sentiment

def test_ai_sentiment_engine_critical_threshold():
    mock_data = {
        "keyword": "測試產品",
        "sentiment_breakdown": {"sentiment_index": 0.05, "negative_pct": 30.0}
    }
    status, score, label, advice = ai_sentiment.analyze_market_trend(mock_data)
    assert status == "critical"
    assert "公關危機警告" in label

def test_ai_sentiment_engine_positive_case():
    mock_data = {
        "keyword": "AI 新趨勢",
        "sentiment_breakdown": {"sentiment_index": 0.85, "negative_pct": 5.0}
    }
    status, score, label, advice = ai_sentiment.analyze_market_trend(mock_data)
    assert status == "positive"
    assert "口碑" in label
```

**完成條件 (Definition of Done)**：
- [ ] 能用自己的話解釋 Router → Service → Repository 三層各自的職責
- [ ] 至少撰寫 2 個獨立的 Service 層單元測試
- [ ] 所有測試通過 (`python -m pytest -v`)
- [ ] 理解 `Depends()` 依賴注入的機制
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：為什麼 API Router 層不應該直接寫 SQL 查詢或 AI 演算法？**
> 違反職責單一原則。Router 的職責是 HTTP 通訊（參數校驗、回應格式），把業務邏輯抽到 Service 層後：1) 程式碼可重用（Worker、CLI 也能呼叫 Service）；2) 單元測試不需要啟動 HTTP 客戶端；3) 更換資料庫時 Router 不受影響。

**Q2：什麼是「高內聚、低耦合」？**
> 高內聚：模組內部程式碼彼此緊密相關，專注單一職責。低耦合：模組之間依賴最小化，修改一個模組不會連帶破壞其他模組。分層架構讓每一層只依賴下一層的抽象介面，實現低耦合。

**Q3：OOP 的封裝 (Encapsulation) 解決什麼問題？**
> 防止外部程式碼直接修改物件內部狀態，只能透過公開方法操作。這保護了資料一致性，也讓內部實作可以自由修改而不影響外部使用者。

**Q4：純函式 (Pure Function) 為什麼好測試？**
> 純函式只依賴輸入參數、不依賴外部狀態、不產生副作用。所以測試時不需要模擬資料庫或網路環境，直接傳入參數就能驗證輸出。

**Q5：什麼是依賴注入 (Dependency Injection)？**
> 不讓模組自己建立依賴的物件，而是由外部傳入。好處：1) 測試時可以注入 Mock 物件；2) 切換實作（如換資料庫）不需修改消費端程式碼；3) 解耦。

**Q6：Python 中什麼時候用 class，什麼時候用 function？**
> 當你需要封裝「有狀態」的實體（使用者、訂單、AI 引擎的配置）時用 class。當你做的是「無狀態的資料轉換」（計算情感分數、過濾列表）時用純函式。

### 📎 參考資源 (References)

- [Python OOP 教學 — Real Python](https://realpython.com/python3-object-oriented-programming/)
- [函數式程式設計概念 — Real Python](https://realpython.com/python-functional-programming/)
- [FastAPI 依賴注入](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Pydantic 官方文件](https://docs.pydantic.dev/latest/)
- [Clean Architecture — Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

## Day 03 — 關聯式 SQL 與 12-Factor 配置管理

### 📖 核心觀念 (Core Concepts)

#### 1. 關聯式資料庫 (RDBMS) 基礎
- **Table (資料表)**：由欄位 (Column) 與列 (Row) 組成的二維結構。
- **Primary Key (PK, 主鍵)**：每一列的唯一識別符，保證不重複。
- **Foreign Key (FK, 外鍵)**：參照另一張表主鍵的欄位，建立表與表之間的關聯。
- 類比：**Excel 試算表** — 但有嚴格的型別約束和關聯規則。

#### 2. ACID 事務特性
| 特性 | 說明 | 類比 |
|------|------|------|
| Atomicity (原子性) | 事務中所有操作要嘛全部成功，要嘛全部回滾 | 銀行轉帳：扣款和入帳必須同時完成 |
| Consistency (一致性) | 事務前後資料庫約束都必須被滿足 | 餘額不能為負數 |
| Isolation (隔離性) | 併發事務之間互不干擾 | 兩人同時轉帳不會互相覆蓋 |
| Durability (持久性) | 事務一旦提交，即使停電資料也不會丟失 | 寫入磁碟才算完成 |

#### 3. Index 索引優化
- 索引就像書本的目次，讓資料庫不需要逐行掃描 (Full Table Scan) 就能快速找到目標資料。
- **B-Tree Index**：最常見的索引類型，適用於等值查詢與範圍查詢。
- **何時該加索引**：經常出現在 `WHERE`、`JOIN`、`ORDER BY` 中的欄位。
- **代價**：索引會佔用額外儲存空間，且每次 INSERT/UPDATE 都需同步更新索引。

#### 4. 12-Factor App 第三條：Config（配置與程式碼分離）
- 任何在不同環境（Dev/Staging/Prod）之間可能變動的值，都不應寫死在程式碼中。
- 應透過**環境變數**注入：資料庫連線字串、API Key、Feature Flag。
- Python 實踐：使用 `pydantic-settings` 的 `BaseSettings` 自動讀取 `.env` 檔案。

#### 5. SQLAlchemy ORM 概念
- **ORM (Object-Relational Mapping)**：用 Python 類別來表示資料庫表格，用 Python 物件來表示資料列。
- 開發者寫 Python 程式碼，ORM 自動翻譯成 SQL 指令。
- **好處**：不用手寫 SQL、防止 SQL Injection、跨資料庫移植。

### 📚 延伸知識 (Deep Dive)

#### 1. N+1 查詢問題
- 在迴圈中逐一查詢關聯資料，導致原本 1 次查詢變成 N+1 次。
- 解法：使用 `JOIN` 或 ORM 的 `eager loading` (預先載入)。

#### 2. Connection Pooling（連線池）
- 建立資料庫連線的成本很高（TCP 握手 + 認證），每次請求都建新連線會拖慢效能。
- 連線池預先建立一批連線，請求來時「借用」，處理完「歸還」。
- SQLAlchemy 內建連線池，預設 `pool_size=5`。

#### 3. Database Migration（資料庫遷移）
- 使用 Alembic 管理資料庫 schema 變更歷史，就像 Git 管理程式碼版本。
- 每次修改 Model 時，生成遷移腳本，可以前進或回滾。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：使用 pydantic-settings 管理環境變數（引導式）
1. 開啟 `app/core/config.py`，觀察 `Settings` 類別如何使用 `BaseSettings`。
2. 在專案根目錄建立 `.env` 檔案：
   ```env
   FACTORY_ENVIRONMENT=practice
   FACTORY_APP_NAME=My Market Intelligence Platform
   ```
3. 重啟 Uvicorn 後存取 `/health`。
4. **預期結果**：回傳的 `environment` 變為 `"practice"`，`service` 變為新名稱。

#### 練習 B：設計 SQLAlchemy 資料模型（半自主）
1. 建立 `app/models/db_models.py`。
2. 定義 `KeywordRecord` SQLAlchemy Model，包含：`id (PK)`、`keyword (VARCHAR)`、`category`、`mentions_count (INTEGER)`、`created_at (DATETIME)`。
3. 定義 `SentimentLog` Model，透過 `keyword_id` 外鍵關聯到 `KeywordRecord`。
4. **驗證方式**：成功 import 模型且無語法錯誤。
   ```bash
   python -c "from app.models.db_models import KeywordRecord, SentimentLog; print('Models loaded OK')"
   ```

#### 練習 C：實作 Repository 層抽象介面（挑戰題）
1. 建立 `app/repositories/keyword_repo.py`。
2. 定義一個抽象基底類別 `KeywordRepository`，包含方法：
   - `get_all() -> list`
   - `get_by_id(id: str) -> Optional[dict]`
   - `create(data: dict) -> dict`
3. 實作 `InMemoryKeywordRepository` 子類別（使用 Python list 儲存資料）。
4. 撰寫 3 個單元測試驗證 CRUD 操作。
5. **驗證指令**：
   ```bash
   python -m pytest tests/ -v -k "keyword_repo"
   ```

### 🧪 測試驗證 (Test & Verify)

```python
def test_env_config_isolation():
    """驗證設定值來自環境變數而非硬編碼"""
    from app.core.config import settings
    assert hasattr(settings, "environment")
    assert hasattr(settings, "app_name")

def test_in_memory_repo_create_and_get():
    repo = InMemoryKeywordRepository()
    created = repo.create({"keyword": "AI", "category": "tech"})
    assert created["keyword"] == "AI"
    found = repo.get_by_id(created["id"])
    assert found is not None
```

**完成條件 (Definition of Done)**：
- [ ] 能解釋 ACID 四大特性各自的作用
- [ ] `.env` 修改後 `/health` 回應內容隨之改變
- [ ] SQLAlchemy Model 定義完成且可成功 import
- [ ] 至少 1 個 Repository 層單元測試通過
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：寫死在程式碼中的設定在不同環境部署時有什麼風險？**
> 1) 安全風險：資料庫密碼、API Key 會被 commit 進 Git，任何有 repo 存取權的人都能看到。2) 維護風險：每次切換環境都要改程式碼，容易出錯。3) 部署僵化：同一份 Docker Image 無法在不同環境重用。

**Q2：什麼是 ACID？請舉一個銀行轉帳的例子。**
> A=原子性：A 扣款和 B 入帳必須同時成功或同時失敗。C=一致性：轉帳前後總金額不變。I=隔離性：兩筆同時進行的轉帳不會互相干擾。D=持久性：轉帳成功後即使停電，資料也不會丟失。

**Q3：什麼時候應該加資料庫索引？什麼時候不應該？**
> 應該加：經常出現在 WHERE/JOIN/ORDER BY 中的欄位。不應該加：很少被查詢的欄位、頻繁大量 INSERT 的表（索引更新成本高）、資料量極小的表（Full Scan 更快）。

**Q4：什麼是 ORM？它的優缺點是什麼？**
> ORM 讓開發者用程式語言物件操作資料庫，自動翻譯成 SQL。優點：防 SQL Injection、開發效率高、跨資料庫移植。缺點：複雜查詢效能可能不如手寫 SQL、有一定學習曲線、ORM 抽象層也可能有 Bug。

**Q5：什麼是 N+1 查詢問題？如何解決？**
> 在迴圈中逐一查詢關聯資料，導致 1 次主查詢 + N 次子查詢。解法：使用 SQL JOIN 或 ORM 的 eager loading (如 SQLAlchemy 的 `joinedload()`) 一次性取回所有關聯資料。

**Q6：12-Factor App 的 Config 原則如何在 Python 中實現？**
> 使用 `pydantic-settings` 的 `BaseSettings` 類別，自動從環境變數或 `.env` 檔案讀取設定值。設定值有型別校驗、預設值、在缺少必要設定時啟動即報錯。

### 📎 參考資源 (References)

- [SQLAlchemy 2.0 官方教學](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [12-Factor App — Config](https://12factor.net/config)
- [PostgreSQL 索引教學](https://www.postgresql.org/docs/current/indexes.html)
- [Alembic 資料庫遷移](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## Day 04 — 測試金字塔 (Testing Pyramid & TDD)

### 📖 核心觀念 (Core Concepts)

#### 1. 測試金字塔 (Testing Pyramid)
```text
        /\
       /  \        E2E 測試 (少量、慢、貴)
      /----\
     /      \      整合測試 (中量、中速)
    /--------\
   /          \    單元測試 (大量、快、便宜)
  /____________\
```
- **單元測試 (Unit Test)**：測試最小單位（一個函式、一個方法），不涉及外部系統，執行速度 < 1ms。
- **整合測試 (Integration Test)**：測試多個模組的協作，如 API 端點 + Service 層。
- **端到端測試 (E2E Test)**：模擬真實使用者行為，最慢、最昂貴但覆蓋面最廣。

#### 2. Arrange-Act-Assert (AAA) 三段式
每個測試函式都應遵循這個結構：
```python
def test_example():
    # Arrange (準備)：建立測試資料與環境
    data = {"keyword": "AI"}

    # Act (執行)：呼叫被測試的函式或 API
    result = service.process(data)

    # Assert (斷言)：驗證結果是否符合預期
    assert result["status"] == "ok"
```

#### 3. TDD 紅 — 綠 — 重構 (Red-Green-Refactor)
1. **Red (紅燈)**：先寫一個會失敗的測試（因為功能還沒實作）。
2. **Green (綠燈)**：寫最少的程式碼讓測試通過。
3. **Refactor (重構)**：在不破壞測試的前提下改善程式碼品質。

#### 4. Mocking（模擬物件）
- 當你的函式依賴外部系統（資料庫、API）時，用 Mock 物件替代真實依賴。
- Python 標準庫：`unittest.mock.patch`、`MagicMock`。
- **好處**：測試更快、更穩定、不受外部系統狀態影響。

#### 5. Code Coverage（程式碼覆蓋率）
- 衡量測試涵蓋了多少比例的程式碼行數/分支。
- 工具：`pytest-cov`。
- **注意**：100% 覆蓋率不等於零 Bug！覆蓋率只代表「每行程式碼都被執行過」，不代表所有邊界情況都被測試過。

### 📚 延伸知識 (Deep Dive)

#### 1. 發現 Bug 的成本曲線
```text
  修復成本
    ↑
    |                              ★ 生產環境
    |                    ★ QA 階段
    |           ★ 整合測試
    |    ★ 單元測試
    |★ Code Review
    +──────────────────────────→ 時間
```
Bug 越晚被發現，修復成本呈**指數級增長**。單元測試在開發階段就攔截 Bug，成本最低。

#### 2. FastAPI TestClient 的運作原理
- `TestClient(app)` 不需要啟動真正的 HTTP 伺服器。
- 它在 Python 記憶體中直接將 HTTP 請求傳遞給 FastAPI 應用，速度極快。
- 因此可以在 CI/CD Pipeline 中每次 commit 都跑完全部測試。

#### 3. 測試的反模式 (Anti-patterns)
- **測試內部實作**：測試不應該關心函式內部用了什麼演算法，只應該關心輸入 → 輸出。
- **脆弱測試 (Fragile Test)**：微小的程式碼變動就導致大量測試失敗。
- **測試之間有依賴**：測試 B 依賴測試 A 先執行 — 這是大忌，每個測試必須獨立。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：用 pytest-cov 檢查程式碼覆蓋率（引導式）
1. 安裝 coverage 套件：
   ```bash
   pip install pytest-cov
   ```
2. 執行帶覆蓋率報告的測試：
   ```bash
   python -m pytest --cov=app --cov-report=term-missing
   ```
3. 觀察每個模組的覆蓋率百分比和未覆蓋的行號。
4. **預期結果**：看到類似 `app/api/health.py  15  2  87%  14-15` 的報告。

#### 練習 B：用 TDD 方式開發新功能（半自主）
1. **先寫測試（Red 紅燈）**：在 `tests/test_health.py` 中新增：
   ```python
   def test_health_returns_version():
       response = client.get("/health")
       assert "version" in response.json()
   ```
2. 執行 `python -m pytest` — 測試應該**失敗**（因為還沒加 `version` 欄位）。
3. **最少程式碼讓它通過（Green 綠燈）**：在 `app/api/health.py` 的 `health_check()` 回傳字典中加入 `"version": "1.0.0"`。
4. 再次執行 `python -m pytest` — 測試應該**通過**。
5. **驗證指令**：
   ```bash
   python -m pytest tests/test_health.py -v
   ```

#### 練習 C：用 Mock 模擬外部 API 呼叫（挑戰題）
1. 建立 `tests/test_mock_example.py`。
2. 假設有一個函式 `fetch_external_price(keyword: str) -> float` 會呼叫外部 API 取得價格。
3. 用 `unittest.mock.patch` 模擬這個函式，讓它回傳固定值 `99.9`。
4. 驗證你的業務邏輯函式在收到 `99.9` 後的處理結果。
5. **驗證指令**：
   ```bash
   python -m pytest tests/test_mock_example.py -v
   ```

### 🧪 測試驗證 (Test & Verify)

```python
# 練習 B — TDD 驗證
def test_health_returns_version():
    response = client.get("/health")
    assert response.status_code == 200
    assert "version" in response.json()

# 練習 C — Mock 驗證
from unittest.mock import patch

def test_price_calculation_with_mock():
    with patch("app.services.market_scraper.fetch_external_price", return_value=99.9):
        result = calculate_total(keyword="AI", quantity=10)
        assert result == 999.0
```

**完成條件 (Definition of Done)**：
- [ ] 能解釋單元測試、整合測試、E2E 測試的差異與適用場景
- [ ] 成功執行 `pytest --cov` 並看到覆蓋率報告
- [ ] 完成一輪 TDD Red-Green-Refactor 循環
- [ ] 至少撰寫 1 個使用 Mock 的測試
- [ ] 所有測試通過 (`python -m pytest -v`)
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：單元測試和整合測試的差異是什麼？發現 Bug 的成本差異？**
> 單元測試只測最小功能單位、不涉及外部系統、執行快速（< 1ms）。整合測試測多模組協作，較慢但能發現模組間的相容性問題。越早發現 Bug 修復成本越低，單元測試是最便宜的 Bug 攔截機制。

**Q2：什麼是 TDD？它的 Red-Green-Refactor 循環是什麼？**
> TDD 是先寫測試再寫實作的開發方法。Red：先寫一個失敗的測試。Green：寫最少的程式碼讓測試通過。Refactor：在測試保護下改善程式碼結構。好處是每一行新程式碼都有測試保護。

**Q3：什麼是 Mocking？什麼時候該用？**
> Mocking 是用模擬物件替代真實依賴（資料庫、外部 API）。當你想測試業務邏輯但不想被外部系統的不穩定性影響時使用。注意：過度 Mock 會讓測試變得脆弱且失去意義。

**Q4：100% 程式碼覆蓋率代表零 Bug 嗎？**
> 絕對不是。覆蓋率只代表每行程式碼都被執行過，但不代表所有邊界條件、競態條件、錯誤路徑都被測試過。一個有意義的測試比追求覆蓋率數字更重要。

**Q5：什麼是測試的 Arrange-Act-Assert 模式？**
> Arrange：準備測試資料和環境。Act：執行被測試的函式。Assert：驗證結果是否符合預期。這三段式結構讓測試易讀、易維護。

**Q6：FastAPI TestClient 為什麼不需要啟動真正的伺服器？**
> TestClient 在 Python 記憶體中直接將 HTTP 請求傳遞給 ASGI 應用（FastAPI），跳過 TCP 網路層，因此速度極快且不佔用任何埠口。

### 📎 參考資源 (References)

- [pytest 官方文件](https://docs.pytest.org/en/stable/)
- [pytest-cov 覆蓋率工具](https://pytest-cov.readthedocs.io/)
- [unittest.mock 官方文件](https://docs.python.org/3/library/unittest.mock.html)
- [Martin Fowler — Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [FastAPI Testing 文件](https://fastapi.tiangolo.com/tutorial/testing/)

---

## Day 05 — 重構 (Refactoring) 與 SOLID 原則

### 📖 核心觀念 (Core Concepts)

#### 1. SOLID 五大原則
| 原則 | 英文全稱 | 白話解釋 |
|------|----------|----------|
| S | Single Responsibility | 一個類別只負責一件事 |
| O | Open/Closed | 對擴展開放，對修改關閉 |
| L | Liskov Substitution | 子類別可以完全替換父類別使用 |
| I | Interface Segregation | 介面要小而精，不要一個大介面包山包海 |
| D | Dependency Inversion | 高層模組依賴抽象，不直接依賴低層實作 |

#### 2. 什麼是重構 (Refactoring)？
- **重構**：在不改變外部可觀察行為的前提下，改善程式碼內部結構。
- **重寫**：從頭重新開發，外部行為可能改變。
- **關鍵差異**：重構有測試保護網，每一步都能驗證行為不變；重寫則風險極高。

#### 3. 常見 Code Smell（程式碼壞味道）
- **Long Method (過長方法)**：一個函式超過 20~30 行 → 拆分為多個小函式。
- **God Class (上帝類別)**：一個類別負責太多事情 → 拆分職責。
- **Feature Envy (特性忌妒)**：方法頻繁存取其他類別的資料 → 搬移到正確的類別。
- **Magic Number (魔術數字)**：硬編碼的數字 `if score > 0.15` → 提取為命名常數。
- **Duplicated Code (重複程式碼)**：相同邏輯出現在多處 → 抽取為共用函式。

#### 4. 常用重構手法
- **Extract Method (提取方法)**：把長函式中的一段邏輯抽成獨立函式。
- **Rename Variable (重命名變數)**：讓變數名稱更具描述性。
- **Replace Magic Number with Constant**：`0.15` → `CRITICAL_SENTIMENT_THRESHOLD = 0.15`。
- **Move Method (搬移方法)**：把方法移到更合適的類別。

#### 5. 重構的前提條件
- **必須有測試覆蓋**：沒有測試保護的重構是危險的冒險行為。
- **小步快跑**：每次只做一個小重構，重構完就跑測試，確保沒破壞任何東西。

### 📚 延伸知識 (Deep Dive)

#### 1. Open/Closed 原則實戰：策略模式 (Strategy Pattern)
```python
# 不好的寫法：每新增一種分析方式就要修改原函式
def analyze(method: str, data: dict):
    if method == "sentiment":
        ...
    elif method == "frequency":
        ...
    # 每加一種都要改這裡 — 違反 Open/Closed！

# 好的寫法：策略模式
class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, data: dict) -> dict: ...

class SentimentStrategy(AnalysisStrategy):
    def analyze(self, data): ...

class FrequencyStrategy(AnalysisStrategy):
    def analyze(self, data): ...
```

#### 2. 設計模式初探：Repository Pattern
- 將資料存取邏輯封裝在 Repository 類別中。
- Service 層只知道 Repository 的介面，不知道底層是 PostgreSQL、MongoDB 還是記憶體。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：消除魔術數字（引導式）
1. 開啟 `app/services/ai_sentiment.py`。
2. 找到所有硬編碼的數字（如 `0.15`、`20.0`）。
3. 將它們提取為類別常數：
   ```python
   CRITICAL_SENTIMENT_THRESHOLD = 0.15
   NEGATIVE_CRISIS_THRESHOLD = 20.0
   ```
4. 用常數替換原本的魔術數字。
5. **驗證指令**：
   ```bash
   python -m pytest -v
   ```
6. **預期結果**：所有測試依然通過（行為不變，只改善了可讀性）。

#### 練習 B：Extract Method 重構（半自主）
1. 找出專案中最長的一個函式。
2. 把其中一段可獨立的邏輯抽取為一個新的私有方法。
3. 原函式改為呼叫新方法。
4. **驗證指令**：
   ```bash
   python -m pytest -v
   ```
5. **預期結果**：測試全通過，但程式碼結構更清晰。

#### 練習 C：應用依賴反轉原則（挑戰題）
1. 建立 `app/repositories/base.py`，定義抽象基底類別 `BaseKeywordRepository`。
2. 建立 `app/repositories/memory_repo.py`，實作記憶體版本。
3. 修改 Service 層，讓它接受 Repository 介面而非直接存取資料。
4. 撰寫測試，驗證注入不同 Repository 實作時 Service 行為一致。
5. **驗證指令**：
   ```bash
   python -m pytest tests/ -v
   ```

### 🧪 測試驗證 (Test & Verify)

```python
def test_refactored_sentiment_still_works():
    """重構後的 AI 引擎行為必須與重構前完全一致"""
    mock_data = {
        "keyword": "AI",
        "sentiment_breakdown": {"sentiment_index": 0.05, "negative_pct": 30.0}
    }
    status, _, label, _ = ai_sentiment.analyze_market_trend(mock_data)
    assert status == "critical"

def test_constants_are_defined():
    """驗證魔術數字已被提取為命名常數"""
    from app.services.ai_sentiment import AIMarketSentimentEngine
    assert hasattr(AIMarketSentimentEngine, "CRITICAL_SENTIMENT_THRESHOLD")
```

**完成條件 (Definition of Done)**：
- [ ] 能說出 SOLID 五大原則各自解決什麼問題
- [ ] 成功將至少 2 個魔術數字提取為命名常數
- [ ] 完成至少 1 次 Extract Method 重構
- [ ] 重構前後所有測試仍然通過
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：重構 (Refactoring) 和重寫 (Rewriting) 的區別？**
> 重構是在不改變外部行為的前提下改善內部結構，有測試保護，風險低且可漸進式進行。重寫是從頭開發，外部行為可能改變，風險高且耗時長。業界最佳實踐是「漸進式重構」而非「大爆炸式重寫」。

**Q2：什麼是 Single Responsibility Principle？為什麼重要？**
> 一個類別或函式只應有一個改變的理由。如果一個類別負責 HTTP 處理、資料庫查詢和 AI 計算，當任何一個需求變動時都要改這個類別，風險極高。拆分後每個模組獨立變動、獨立測試。

**Q3：什麼是 Code Smell？舉三個例子。**
> Code Smell 是暗示程式碼可能有設計問題的徵兆。例：1) Long Method 過長函式 2) Magic Number 魔術數字 3) Duplicated Code 重複程式碼。它們不一定是 Bug，但會降低可維護性。

**Q4：Open/Closed 原則的「對擴展開放、對修改關閉」是什麼意思？**
> 新增功能時應該透過「新增程式碼」（如新增一個類別）而非「修改既有程式碼」。例如使用策略模式，新增分析方式時只需新增一個 Strategy 子類別，不需修改現有邏輯。

**Q5：為什麼重構前一定要有測試？**
> 測試是重構的安全網。沒有測試保護的重構就像沒有安全繩的攀岩——你不知道自己有沒有破壞什麼東西，直到生產環境出事故才發現。

### 📎 參考資源 (References)

- [Refactoring Guru — 重構技巧大全](https://refactoring.guru/refactoring)
- [SOLID 原則 — Real Python](https://realpython.com/solid-principles-python/)
- [Martin Fowler — Refactoring](https://refactoring.com/)
- [Design Patterns — Refactoring Guru](https://refactoring.guru/design-patterns)

---

## Day 06 — 演算法、資料結構與記憶體限流 (Algorithms)

### 📖 核心觀念 (Core Concepts)

#### 1. 時間複雜度與空間複雜度 (Big-O Notation)
| 表示法 | 名稱 | 範例 |
|--------|------|------|
| O(1) | 常數時間 | 字典取值 `dict[key]` |
| O(log n) | 對數時間 | 二分搜尋 |
| O(n) | 線性時間 | 遍歷列表 |
| O(n log n) | 線性對數 | 排序演算法 (Merge Sort) |
| O(n²) | 平方時間 | 巢狀迴圈暴力搜尋 |

#### 2. Hash Table (雜湊表) — Python 的 `dict`
- **核心原理**：將 key 透過雜湊函式計算出一個索引位置，直接存取該位置的值。
- **時間複雜度**：查詢、插入、刪除平均都是 O(1)。
- **碰撞處理 (Collision)**：不同 key 產生相同索引時，使用鏈結法或開放定址法解決。
- **Python 實踐**：`dict`、`set`、`collections.Counter` 底層都是 Hash Table。

#### 3. Sliding Window 滑動窗口演算法
- **應用場景**：API 限流 (Rate Limiting)。
- **原理**：維護一個時間窗口（如最近 60 秒），計算窗口內的請求數量。
- **與固定窗口的差異**：固定窗口在分鐘邊界處可能允許 2 倍流量湧入，滑動窗口更精確。

```text
固定窗口問題：
   00:00:50 ──── 00:01:00 ──── 00:01:10
   [  50 次請求  ][  50 次請求  ]
   ← 在邊界的 20 秒內實際有 100 次請求！

滑動窗口：
   任意 60 秒窗口內最多 100 次請求 ✓
```

#### 4. LRU Cache (最近最少使用快取)
- **原理**：快取容量滿時，淘汰最久沒被使用的項目。
- **實現**：Python 內建 `functools.lru_cache` 裝飾器。
- **資料結構**：HashMap + Doubly Linked List 實現 O(1) 查找與 O(1) 淘汰。

#### 5. Token Bucket 令牌桶演算法
- **原理**：桶中定時補充令牌，每個請求消耗一個令牌，桶空則拒絕請求。
- **與 Sliding Window 比較**：Token Bucket 允許短時間爆發流量（桶中有積累令牌），Sliding Window 則嚴格限制窗口內的總量。

### 📚 延伸知識 (Deep Dive)

#### 1. 企業級限流的實際架構
- **單機限流**：使用記憶體內的滑動窗口（適合開發階段）。
- **分散式限流**：使用 Redis + Lua Script 實現跨節點一致性限流。
- **API Gateway 層限流**：Istio / Nginx / Kong 在網關層限流，避免請求進入應用層。

#### 2. 演算法在面試中的重要性
- 大型科技公司（FAANG）面試必考 LeetCode 風格的演算法題。
- 但在實際工作中，更重要的是「知道何時該用什麼資料結構」，而非手寫紅黑樹。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：Big-O 分析練習（引導式）
1. 分析以下三個函式的時間複雜度：
   ```python
   # 函式 1
   def find_in_dict(data: dict, key: str):
       return data.get(key)  # O(?)
   
   # 函式 2
   def find_in_list(data: list, target: str):
       for item in data:
           if item == target:
               return item   # O(?)
   
   # 函式 3
   def find_duplicates(data: list):
       for i in range(len(data)):
           for j in range(i+1, len(data)):
               if data[i] == data[j]:
                   return True  # O(?)
   ```
2. **預期答案**：O(1)、O(n)、O(n²)。

#### 練習 B：手寫 Sliding Window 限流中間件（半自主）
1. 在 `app/core/` 中建立 `rate_limiter.py`。
2. 實作 `SlidingWindowRateLimiter` 類別：
   - 建構子接受 `max_requests: int` 和 `window_seconds: int`。
   - `is_allowed(client_id: str) -> bool` 方法。
3. 使用 `collections.deque` 儲存每個 client 的請求時間戳記。
4. **驗證指令**：
   ```bash
   python -m pytest tests/test_rate_limiter.py -v
   ```

#### 練習 C：整合限流器到 FastAPI 中間件（挑戰題）
1. 將 `SlidingWindowRateLimiter` 整合為 FastAPI Middleware。
2. 超過限流時回傳 `429 Too Many Requests`。
3. 在 Swagger UI 或 Terminal 中快速連續發送請求驗證。
4. **驗證指令**：
   ```bash
   for ($i=1; $i -le 15; $i++) { curl.exe -s -o NUL -w "%{http_code}" http://127.0.0.1:8000/health }
   ```
5. **預期結果**：前 10 次回傳 `200`，超額後回傳 `429`。

### 🧪 測試驗證 (Test & Verify)

```python
from app.core.rate_limiter import SlidingWindowRateLimiter

def test_rate_limiter_allows_within_limit():
    limiter = SlidingWindowRateLimiter(max_requests=5, window_seconds=60)
    for _ in range(5):
        assert limiter.is_allowed("client-1") is True

def test_rate_limiter_blocks_over_limit():
    limiter = SlidingWindowRateLimiter(max_requests=5, window_seconds=60)
    for _ in range(5):
        limiter.is_allowed("client-1")
    assert limiter.is_allowed("client-1") is False

def test_rate_limiter_isolates_clients():
    limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=60)
    limiter.is_allowed("client-1")
    limiter.is_allowed("client-1")
    assert limiter.is_allowed("client-1") is False
    assert limiter.is_allowed("client-2") is True  # 不同 client 不受影響
```

**完成條件 (Definition of Done)**：
- [ ] 能正確分析給定程式碼的 Big-O 複雜度
- [ ] 完成 Sliding Window Rate Limiter 類別
- [ ] 限流器的 3 個單元測試全部通過
- [ ] 能解釋 Sliding Window 和 Token Bucket 的差異
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：什麼是 Big-O？O(1) 和 O(n) 的實際效能差異？**
> Big-O 描述演算法隨輸入規模增長的效能趨勢。O(1) 無論資料量多大都是固定時間（如字典查詢）；O(n) 時間與資料量成正比（如遍歷列表）。當資料量從 1,000 增長到 1,000,000 時，O(n) 慢 1,000 倍，O(1) 幾乎不變。

**Q2：Python 的 dict 底層是什麼資料結構？查詢複雜度是？**
> 底層是 Hash Table，平均查詢複雜度 O(1)。最壞情況（所有 key 碰撞到同一個 bucket）為 O(n)，但在實踐中幾乎不會發生。

**Q3：Sliding Window 和 Token Bucket 限流演算法各自的優缺點？**
> Sliding Window：精確控制窗口內請求數，但記憶體消耗較高（需記錄每個請求時間戳記）。Token Bucket：允許短時間爆發流量（桶中有累積令牌），實現簡單，但控制精度較低。

**Q4：為什麼 API 限流很重要？如果不做限流會怎樣？**
> 沒有限流時，惡意使用者或爬蟲可以無限量發送請求，導致伺服器過載、回應延遲飆升、影響正常使用者體驗，甚至觸發雪崩效應（Cascading Failure）導致整個系統崩潰。

**Q5：LRU Cache 的實現需要什麼資料結構？為什麼？**
> 需要 HashMap + Doubly Linked List。HashMap 提供 O(1) 查找，Doubly Linked List 提供 O(1) 移動元素到頭部（標記為最近使用）和 O(1) 刪除尾部（淘汰最久未使用的項目）。

**Q6：`functools.lru_cache` 適合用在什麼場景？**
> 適合用在：1) 純函式（相同輸入相同輸出）2) 計算成本高 3) 會被頻繁呼叫且參數重複率高。不適合用在：有副作用的函式、參數不可雜湊的情況。

### 📎 參考資源 (References)

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [Rate Limiting 演算法圖解 — Cloudflare Blog](https://blog.cloudflare.com/counting-things-a-lot-of-different-things/)
- [Python collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

---

## Day 07 — 第一週單體架構驗收與 Code Review

### 📖 核心觀念 (Core Concepts)

#### 1. Monolith 單體架構 vs Microservices 微服務
| 面向 | 單體 (Monolith) | 微服務 (Microservices) |
|------|-----------------|----------------------|
| 部署 | 整個應用一起部署 | 各服務獨立部署 |
| 通訊 | 函式內呼叫（快） | 網路 HTTP/gRPC（慢） |
| 除錯 | 容易（單一程序） | 困難（分散式追蹤） |
| 擴展 | 整體擴展 | 可針對熱點服務擴展 |
| 適合 | 早期專案、小團隊 | 成熟產品、大團隊 |

#### 2. 為什麼不要一開始就寫微服務？
- **Martin Fowler 的名言**：「Monolith First」— 先把業務邏輯搞清楚，等到系統夠大再拆分。
- 過早拆分的代價：分散式事務複雜度、網路延遲、運維成本倍增。
- **本專案的策略**：第一週打造完整的單體應用，第二週再開始拆分微服務邊界。

#### 3. Code Review 的價值與技巧
- **不只是抓 Bug**：Code Review 更重要的是知識傳遞、設計討論、維持程式碼風格一致性。
- **Review 清單**：
  1. ✅ 命名是否清晰易懂？
  2. ✅ 是否遵循 SOLID 原則？
  3. ✅ 有沒有重複程式碼？
  4. ✅ 測試覆蓋是否足夠？
  5. ✅ 有沒有安全漏洞（SQL Injection、敏感資訊外洩）？
  6. ✅ 效能是否有明顯問題？

#### 4. 架構決策記錄 (ADR - Architecture Decision Record)
- 記錄團隊做出的重要架構決策，包含：背景、選項、決定、理由。
- 讓未來加入團隊的人理解「為什麼選擇 A 而不是 B」。

#### 5. 端到端驗收 (End-to-End Validation)
- 驗收的不是單一功能，而是**完整的業務流程**能否從頭到尾跑通。
- 本專案的 E2E 流程：建立關鍵字 → 抓取聲量 → AI 分析 → 生成研報。

### 📚 延伸知識 (Deep Dive)

#### 1. 單體到微服務的演進路徑
```text
Stage 1: Monolith（我們現在）
    → 所有程式碼在同一個 FastAPI 應用中

Stage 2: Modular Monolith（模組化單體）
    → 模組間透過介面通訊，但仍在同一個程序中

Stage 3: Microservices（微服務）
    → 各模組拆分為獨立服務，透過 HTTP/gRPC/訊息佇列通訊
```

#### 2. 技術債 (Technical Debt) 管理
- 技術債就像金融負債：短期借貸可以加速開發，但長期不還會產生利息（維護成本增加）。
- **管理策略**：在每個 Sprint 中安排 15~20% 的時間專門還技術債。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：執行全套端到端驗收（引導式）
1. 確保 Uvicorn 正在運行。
2. 依序執行以下指令，驗證完整業務流程：
   ```bash
   # 1. 健康檢查
   curl.exe http://127.0.0.1:8000/health

   # 2. 查看關鍵字列表
   curl.exe http://127.0.0.1:8000/api/v1/market/keywords

   # 3. AI 情感分析
   curl.exe http://127.0.0.1:8000/api/v1/market/sentiment/K-001

   # 4. 計費方案
   curl.exe http://127.0.0.1:8000/api/v1/billing/plans

   # 5. 研報生成
   # 在瀏覽器開啟：http://127.0.0.1:8000/api/v1/reports/html/K-001

   # 6. 全套測試
   python -m pytest -v
   ```
3. **預期結果**：全部 API 回傳正確結果，全部測試通過。

#### 練習 B：自我 Code Review 檢查清單（半自主）
1. 依照以下清單逐一檢查專案中的每個 Python 檔案：
   - [ ] 變數與函式命名是否清晰？（`x` → `sentiment_score`）
   - [ ] 是否有魔術數字未提取為常數？
   - [ ] 是否有超過 30 行的函式需要拆分？
   - [ ] import 是否整理乾淨（未使用的 import）？
   - [ ] 是否有重複程式碼可以抽取為共用函式？
2. 記錄發現的問題與改善建議。

#### 練習 C：撰寫架構決策記錄 ADR（挑戰題）
1. 建立 `docs/adr/ADR-001-why-fastapi.md`。
2. 記錄為什麼選擇 FastAPI 而非 Flask / Django：
   - 背景：需要高效能非同步 API + 自動 OpenAPI 文件。
   - 選項：Flask、Django、FastAPI。
   - 決定：FastAPI。
   - 理由：原生 async、自動型別校驗、自動 Swagger UI。
3. **驗證方式**：文件結構完整，論述清晰。

### 🧪 測試驗證 (Test & Verify)

```bash
# 全套測試（含覆蓋率）
python -m pytest -v --tb=short

# 確認所有端點可正常存取
curl.exe http://127.0.0.1:8000/health
curl.exe http://127.0.0.1:8000/api/v1/market/keywords
curl.exe http://127.0.0.1:8000/api/v1/billing/plans
```

**完成條件 (Definition of Done)**：
- [ ] 全套 E2E 端到端驗收通過（5 個 API 端點 + pytest 全綠）
- [ ] 完成自我 Code Review 檢查清單
- [ ] 能口述單體架構 vs 微服務的 Tradeoff
- [ ] （選做）完成 ADR-001 架構決策記錄
- [ ] 已執行 `git commit` 儲存今日進度
- [ ] 整理本週學到的所有核心概念

### 🗣️ 面試問答 (Interview Q&A)

**Q1：為什麼初創專案應該從單體架構開始？**
> 初期業務邏輯和服務邊界都不明確，過早拆分微服務會增加分散式系統複雜度（網路延遲、分散式事務、運維成本），且拆錯邊界後修正的代價極高。先用單體架構快速驗證商業模式，等業務穩定後再根據實際瓶頸拆分。

**Q2：Monolith 和 Microservices 在部署上的差異？**
> 單體：所有功能在一個容器/程序中，部署簡單但一個小改動需要重新部署整個應用。微服務：各服務獨立部署，修改某服務不影響其他服務，但需要容器編排（Kubernetes）和服務發現機制。

**Q3：Code Review 最重要的目的是什麼？**
> 不僅是抓 Bug，更重要的是：1) 知識分享（團隊成員了解彼此的程式碼）2) 設計品質把關 3) 維持程式碼風格一致性 4) 培養初級工程師 5) 提早發現架構層面的設計問題。

**Q4：什麼是技術債？如何管理？**
> 技術債是為了趕工而犧牲程式碼品質的短期決策，長期會增加維護成本。管理方式：1) 在待辦清單中記錄 2) 每個迭代安排固定比例的時間還債 3) 防止技術債累積到不可控的程度。

**Q5：什麼是 ADR？為什麼重要？**
> ADR (Architecture Decision Record) 記錄團隊做出的重要架構選擇及其理由。重要性：1) 新成員能快速理解歷史脈絡 2) 避免重複討論已決定的議題 3) 決策過程可追蹤、可回溯。

**Q6：如果有人在 Code Review 中說你的程式碼「很醜」，你會怎麼回應？**
> 1) 先保持開放心態，請對方具體說明哪裡可以改進 2) 區分「風格偏好」和「實質問題」3) 如果是實質問題（可維護性、效能、安全），感謝指出並修改 4) 如果是風格偏好，建議團隊建立 Coding Convention。

### 📎 參考資源 (References)

- [Martin Fowler — Monolith First](https://martinfowler.com/bliki/MonolithFirst.html)
- [Google Engineering Practices — Code Review](https://google.github.io/eng-practices/review/)
- [ADR GitHub Template](https://github.com/joelparkerhenderson/architecture-decision-record)
- [Technical Debt — Martin Fowler](https://martinfowler.com/bliki/TechnicalDebt.html)

---
---

# 📌 第二週：商業多租戶、金流計費、數據管道與微服務拆分

---

## Day 08 — 多租戶隔離 (Multi-Tenancy) & B2B 授權

### 📖 核心觀念 (Core Concepts)

#### 1. 什麼是多租戶 (Multi-Tenancy)？
- **定義**：一個應用程式同時服務多個「租戶 (Tenant)」，每個租戶看到的是自己的資料，互不影響。
- 類比：**辦公大樓** — 同一棟大樓有很多公司（租戶），共用電梯和大廳（基礎設施），但各自的辦公室（資料）是獨立的。

#### 2. 三種隔離策略
| 策略 | 說明 | 隔離程度 | 成本 |
|------|------|----------|------|
| Database-per-Tenant | 每個租戶一個獨立資料庫 | 最高 | 最高 |
| Schema-per-Tenant | 同一資料庫，不同 Schema | 中等 | 中等 |
| Row-level Isolation | 同一張表，用 tenant_id 欄位區隔 | 最低 | 最低 |

#### 3. API Key 認證機制
- 每個租戶發放唯一的 API Key（如 `X-API-Key: mk_live_abc123`）。
- 伺服器在每個請求中驗證 API Key，識別租戶身份。
- 無效或缺少 API Key → 回傳 `401 Unauthorized`。

#### 4. RBAC 角色型存取控制 (Role-Based Access Control)
- 定義角色（admin、analyst、viewer），每個角色有不同的操作權限。
- 使用者被指派角色，權限由角色決定而非個人。

#### 5. FastAPI 的 Depends() 認證鏈
```python
def get_current_tenant(api_key: str = Header(alias="X-API-Key")) -> Tenant:
    tenant = verify_api_key(api_key)
    if not tenant:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return tenant

@router.get("/data")
def get_data(tenant: Tenant = Depends(get_current_tenant)):
    # 此處的 tenant 已經過認證
    return query_data_for_tenant(tenant.id)
```

### 📚 延伸知識 (Deep Dive)

#### 1. 跨租戶資料滲漏 (Cross-Tenant Data Leak) 防範
- 這是 SaaS 最嚴重的安全事故之一。
- 防範策略：所有 SQL 查詢必須帶 `WHERE tenant_id = :current_tenant`，永遠不允許不帶 tenant_id 的查詢。

#### 2. Rate Limiting per Tenant
- 不同訂閱等級（Free / Pro / Enterprise）有不同的 API 呼叫配額。
- Free 每月 100 次、Pro 10,000 次、Enterprise 不限。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：理解現有認證流程（引導式）
1. 開啟 `app/core/auth.py`，逐行閱讀 `get_current_tenant()` 函式。
2. 開啟 `app/api/market.py`，找到使用 `Depends(get_current_tenant)` 的端點。
3. 在 Swagger UI 中不帶 API Key 呼叫 `/api/v1/market/keywords`。
4. **預期結果**：回傳 `401 Unauthorized`。

#### 練習 B：實作租戶配額檢查（半自主）
1. 在 `app/core/auth.py` 中新增 `check_quota(tenant: Tenant) -> bool` 函式。
2. 檢查該租戶的當月使用量是否超過其訂閱等級配額。
3. 超額時拋出 `HTTPException(status_code=429, detail="Monthly quota exceeded")`。
4. 撰寫 2 個單元測試（配額內通過、配額外拒絕）。
5. **驗證指令**：
   ```bash
   python -m pytest tests/ -v -k "quota"
   ```

#### 練習 C：實作 Tenant 資料隔離中間件（挑戰題）
1. 建立 `app/middleware/tenant_isolation.py`。
2. 實作中間件：自動將 `tenant_id` 注入到所有資料查詢的上下文中。
3. 撰寫測試，驗證 Tenant-A 無法存取 Tenant-B 的資料。
4. **驗證指令**：
   ```bash
   python -m pytest tests/ -v -k "tenant"
   ```

### 🧪 測試驗證 (Test & Verify)

```python
def test_unauthorized_without_api_key():
    response = client.get("/api/v1/market/keywords")
    assert response.status_code == 401

def test_authorized_with_valid_api_key():
    response = client.get(
        "/api/v1/market/keywords",
        headers={"X-API-Key": "test-api-key-001"}
    )
    assert response.status_code == 200
```

**完成條件 (Definition of Done)**：
- [ ] 能解釋三種多租戶隔離策略的 Tradeoff
- [ ] 無 API Key 請求回傳 401
- [ ] 配額檢查測試通過
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：如何確保 B2B SaaS 多租戶架構下不會發生跨租戶資料滲漏？**
> 1) 所有資料查詢強制帶 tenant_id 過濾 2) 使用 API Key 或 JWT 在認證層識別租戶 3) 定期安全審計跨租戶查詢 4) 嚴格的 Code Review 檢查。

**Q2：Database-per-Tenant 和 Row-level Isolation 各自的優缺點？**
> DB-per-Tenant：隔離性最高、效能好、但運維成本高（每個客戶一個 DB）。Row-level：成本低、管理方便，但需要嚴格防範跨租戶查詢、大客戶資料量可能影響共享資源。

**Q3：什麼是 RBAC？和 ABAC 的差別？**
> RBAC 根據「角色」分配權限（admin 可以刪除、viewer 只能讀取）。ABAC 根據「屬性」判斷（用戶部門、資料分類、存取時間等多維度條件）。RBAC 簡單直觀，ABAC 更彈性但複雜。

**Q4：API Key 認證和 JWT 認證的差別？**
> API Key：簡單的靜態字串，適合 Server-to-Server 通訊。JWT：包含使用者資訊和過期時間的簽章令牌，適合前端使用者認證。API Key 洩漏後只能手動作廢，JWT 有自動過期機制。

**Q5：如何設計 Rate Limiting 讓不同訂閱等級有不同配額？**
> 在認證層取得租戶的訂閱等級，從設定檔讀取該等級對應的配額上限，在每個請求中遞增計數器並與上限比對。超額時回傳 429 並在 Response Header 中帶上 `X-RateLimit-Remaining`。

### 📎 參考資源 (References)

- [Multi-Tenancy Architecture Patterns — AWS](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/multi-tenancy-models.html)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)

---

## Day 09 — Stripe 金流整合與 Usage-Based Billing

### 📖 核心觀念 (Core Concepts)

#### 1. SaaS 商業模式：按量計費 (Usage-Based Billing)
- **固定訂閱制**：每月固定費用（如 Netflix），不論使用量多少。
- **按量計費制**：依實際使用量收費（如 AWS、Twilio），用多少付多少。
- **混合制**：基本費 + 超額按量（如手機資費），本專案採用此模式。

#### 2. Stripe 金流處理基本流程
```text
使用者 → 前端選擇方案 → 後端建立 Checkout Session → Stripe 處理付款
                                                        ↓
使用者付款成功 ← Stripe 回調 ← Webhook 通知 ← Stripe 處理結果
```

#### 3. Webhook 機制
- **定義**：當某個事件發生時（如付款成功），Stripe 主動向你的後端發送 HTTP POST 通知。
- **為什麼需要 Webhook**：因為付款可能在 Stripe 的頁面上完成，你的伺服器不知道什麼時候完成，所以 Stripe 反過來通知你。
- **安全驗證**：每個 Webhook 都帶有簽章，後端必須驗證簽章以防止偽造。

#### 4. 訂閱等級 (Subscription Tiers)
| 等級 | 月配額 | 功能 |
|------|--------|------|
| Free (試用版) | 100 次 API 呼叫 | 基礎關鍵字查詢 |
| Pro (專業版) | 10,000 次 | AI 情感分析 + 研報 |
| Enterprise (企業版) | 無限 | 全功能 + 專屬支援 |

#### 5. 冪等的付款處理
- 網路問題可能導致 Webhook 重複發送。
- 後端必須使用 `idempotency_key` 確保同一筆訂單不會被處理兩次。

### 📚 延伸知識 (Deep Dive)

#### 1. Revenue Metrics（營收指標）
- **MRR (Monthly Recurring Revenue)**：月經常性收入。
- **Churn Rate**：客戶流失率。
- **LTV (Lifetime Value)**：客戶終身價值。

#### 2. PCI DSS 合規
- 信用卡資訊不應經過你的伺服器，全程由 Stripe 處理。
- 你只需要處理 Stripe 回傳的 token，不接觸真實卡號。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：理解現有計費系統（引導式）
1. 開啟 `app/api/billing.py`，閱讀 `/plans`、`/usage`、`/subscribe` 端點。
2. 在 Swagger UI 中測試 `GET /api/v1/billing/plans`。
3. 測試 `GET /api/v1/billing/usage`（帶 API Key）。
4. **預期結果**：看到訂閱方案列表和當前使用量。

#### 練習 B：實作配額用盡自動封鎖（半自主）
1. 修改 `app/core/auth.py`，在 `get_current_tenant()` 中加入配額檢查。
2. 當月使用量超過訂閱配額時，拋出 `402 Payment Required`。
3. **驗證指令**：
   ```bash
   python -m pytest tests/ -v -k "billing"
   ```

#### 練習 C：設計 Webhook 端點（挑戰題）
1. 在 `app/api/billing.py` 中新增 `POST /api/v1/billing/webhook` 端點。
2. 接收 Stripe Webhook 事件，處理 `checkout.session.completed` 事件。
3. 成功時更新租戶的訂閱等級。
4. 實作冪等性檢查（同一 event_id 不重複處理）。
5. **驗證指令**：
   ```bash
   python -m pytest tests/ -v -k "webhook"
   ```

### 🧪 測試驗證 (Test & Verify)

```python
def test_billing_plans_returns_tiers():
    response = client.get("/api/v1/billing/plans")
    assert response.status_code == 200
    plans = response.json()
    assert len(plans) >= 3
    assert any(p["tier"] == "free" for p in plans)

def test_usage_endpoint():
    response = client.get("/api/v1/billing/usage",
                         headers={"X-API-Key": "test-api-key-001"})
    assert response.status_code == 200
    assert "used" in response.json()
```

**完成條件 (Definition of Done)**：
- [ ] 能解釋按量計費與固定訂閱制的設計差異
- [ ] 能解釋 Webhook 機制與安全驗證
- [ ] 計費相關測試通過
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：按量計費和固定訂閱制在後端設計上有什麼差異？**
> 固定訂閱：只需記錄訂閱狀態和到期日。按量計費：需要精確計量每次 API 呼叫、定期結算、處理超額邏輯、產生帳單明細。後者的後端複雜度高出很多。

**Q2：為什麼 Webhook 需要冪等性處理？**
> 網路不穩定時 Stripe 會重試發送 Webhook，同一事件可能被送達多次。如果不做冪等性檢查，同一筆訂單可能被處理兩次（重複扣款或重複升級）。

**Q3：為什麼信用卡資訊不應經過你的伺服器？**
> PCI DSS 合規要求：接觸信用卡資訊的系統必須通過嚴格的安全審計（成本極高）。使用 Stripe Checkout/Elements 讓卡號只經過 Stripe，你只處理 token，大幅降低合規負擔。

**Q4：如何防止使用者繞過配額限制？**
> 1) 在認證層（Middleware）統一檢查配額 2) 使用原子操作（Redis INCR）遞增計數器 3) 配額檢查在 API Gateway 層完成，應用層為第二道防線。

**Q5：什麼是 MRR？為什麼 SaaS 公司很看重這個指標？**
> MRR = Monthly Recurring Revenue，月經常性收入。投資人用它來評估 SaaS 公司的可預測營收能力和成長速度，比一次性收入更能代表公司的健康狀況。

### 📎 參考資源 (References)

- [Stripe 官方文件](https://stripe.com/docs)
- [Stripe Webhooks](https://stripe.com/docs/webhooks)
- [Usage-Based Billing Patterns](https://stripe.com/docs/billing/subscriptions/usage-based)

---

## Day 10 — Docker 容器化與最佳化 Dockerfile

### 📖 核心觀念 (Core Concepts)

#### 1. 什麼是 Docker？為什麼需要容器化？
- **問題**：「在我的電腦上可以跑啊！」— 開發環境與生產環境不一致。
- **解法**：容器將應用程式連同其所有依賴打包成一個標準化單元，在任何環境都能一致運行。
- 類比：**貨櫃運輸** — 不管裡面裝什麼貨物，貨櫃的外部尺寸標準化，任何貨船/卡車都能裝載。

#### 2. Image vs Container
- **Image (映像檔)**：一份唯讀的模板，包含應用程式的程式碼、依賴和執行環境。
- **Container (容器)**：Image 的運行實例，有自己的可寫層、網路和程序。
- 類比：Image 是模具，Container 是用模具做出來的成品，可以做無數個。

#### 3. Dockerfile 與 Layer 快取
```dockerfile
FROM python:3.12-slim    # 基礎映像
WORKDIR /app             # 工作目錄
COPY requirements.txt .  # 先複製依賴清單（利用快取）
RUN pip install -r requirements.txt  # 安裝依賴
COPY . .                 # 再複製程式碼
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
```
- **Layer 快取原理**：每一行指令產生一個 Layer，如果該行的輸入沒變，Docker 直接使用快取。
- **最佳實踐**：先複製 `requirements.txt`、再複製程式碼，這樣改程式碼時不需要重新安裝依賴。

#### 4. Multi-Stage Build（多階段構建）
```dockerfile
# Stage 1: 構建階段
FROM python:3.12 AS builder
RUN pip install --user -r requirements.txt

# Stage 2: 執行階段
FROM python:3.12-slim
COPY --from=builder /root/.local /root/.local
COPY . .
```
- **目的**：最終映像不包含構建工具（gcc、pip cache），體積大幅縮小。

#### 5. Non-root 安全容器
- **為什麼**：容器內以 root 身份運行，若容器被攻破，攻擊者就擁有主機 root 權限。
- **做法**：在 Dockerfile 中建立非 root 使用者並切換。

### 📚 延伸知識 (Deep Dive)

#### 1. .dockerignore 檔案
- 類似 `.gitignore`，排除不需要複製進映像的檔案（`.venv`、`__pycache__`、`.git`）。
- 減少構建上下文的傳輸時間。

#### 2. 映像大小對部署的影響
- 越小的映像 = 越快的拉取速度 = 越快的部署與擴展。
- `python:3.12` (~900MB) vs `python:3.12-slim` (~120MB) vs `python:3.12-alpine` (~50MB)。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：撰寫第一個 Dockerfile（引導式）
1. 在專案根目錄建立 `Dockerfile`。
2. 使用 `python:3.12-slim` 作為基礎映像。
3. 複製程式碼並安裝依賴。
4. 設定啟動指令。
5. **驗證指令**：
   ```bash
   docker build -t market-api .
   docker run -p 8000:8000 market-api
   curl.exe http://127.0.0.1:8000/health
   ```

#### 練習 B：加入 Multi-Stage Build 與 .dockerignore（半自主）
1. 修改 Dockerfile 為兩階段構建。
2. 建立 `.dockerignore` 排除 `.venv`、`__pycache__`、`.git`、`tests/`。
3. 比較修改前後的映像大小。
4. **驗證指令**：
   ```bash
   docker images market-api
   ```

#### 練習 C：建立非 root 安全容器（挑戰題）
1. 在 Dockerfile 中新增非 root 使用者。
2. 所有檔案權限設定正確。
3. 容器啟動後的程序以非 root 身份運行。
4. **驗證指令**：
   ```bash
   docker run market-api whoami  # 應輸出 appuser，不是 root
   ```

### 🧪 測試驗證 (Test & Verify)

```bash
# 構建映像
docker build -t market-api .

# 啟動容器
docker run -d -p 8000:8000 --name market-test market-api

# 測試健康檢查
curl.exe http://127.0.0.1:8000/health

# 檢查映像大小
docker images market-api

# 清理
docker stop market-test && docker rm market-test
```

**完成條件 (Definition of Done)**：
- [ ] 成功構建 Docker 映像
- [ ] 容器啟動後 `/health` 回傳 200
- [ ] 映像使用 slim 基礎映像（< 200MB）
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：Docker Image 和 Container 的差別？**
> Image 是唯讀模板，Container 是 Image 的運行實例。一個 Image 可以啟動多個 Container，每個 Container 有自己的可寫層和網路命名空間。

**Q2：Multi-Stage Build 如何減少映像體積？**
> 第一階段安裝所有構建工具和依賴，第二階段只從第一階段複製需要的產物（編譯後的二進位檔或安裝好的套件），構建工具不會出現在最終映像中。

**Q3：為什麼應該先 COPY requirements.txt 再 COPY 程式碼？**
> Docker Layer 快取機制：如果某一層的輸入沒變就使用快取。先複製 requirements.txt（很少改動）安裝依賴，再複製程式碼（經常改動），這樣修改程式碼時不需要重新安裝依賴。

**Q4：為什麼容器不應該以 root 身份運行？**
> 如果容器被攻破（例如有 RCE 漏洞），攻擊者就擁有容器內的 root 權限。配合容器逃逸漏洞，可能直接取得主機 root 權限。以非 root 運行限縮了攻擊面。

**Q5：.dockerignore 的作用是什麼？**
> 排除不需要進入映像的檔案，減少構建上下文的傳輸時間和最終映像體積。典型排除項目：`.git/`、`.venv/`、`__pycache__/`、`tests/`、`*.md`。

### 📎 參考資源 (References)

- [Docker 官方入門教學](https://docs.docker.com/get-started/)
- [Dockerfile 最佳實踐](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Python Docker 最佳實踐](https://testdriven.io/blog/docker-best-practices/)

---

## Day 11 — Docker Compose & Redis 快取機制

### 📖 核心觀念 (Core Concepts)

#### 1. Docker Compose：多容器編排
- **問題**：真實應用通常由多個服務組成（API + 資料庫 + 快取），手動逐一 `docker run` 很麻煩。
- **解法**：`docker-compose.yml` 一個檔案定義所有服務，`docker-compose up` 一個指令啟動全部。

#### 2. 容器網路 (Container Networking)
- Compose 自動建立 Bridge 網路，所有服務在同一網路中。
- 服務之間透過**服務名稱**互相存取（如 `redis:6379`），而非 IP。

#### 3. Redis 快取基礎
- **Redis**：記憶體內鍵值儲存 (In-Memory Key-Value Store)，讀寫速度極快（微秒級）。
- **常見用途**：API 回應快取、Session 儲存、Rate Limiting 計數器、訊息佇列。

#### 4. Cache-Aside 快取模式
```text
Client 請求 → 先查 Redis 快取
   ↓                    ↓
  有 (Cache Hit)     沒有 (Cache Miss)
   ↓                    ↓
  直接回傳           查資料庫 → 寫入 Redis → 回傳
```

#### 5. TTL (Time-To-Live) 機制
- 每個快取 key 可設定存活時間（如 300 秒）。
- 時間到自動失效，下次請求會重新從資料庫取得最新資料。
- **Trade-off**：TTL 太短 → 快取命中率低；TTL 太長 → 資料可能過時。

### 📚 延伸知識 (Deep Dive)

#### 1. 快取三大問題
| 問題 | 說明 | 解法 |
|------|------|------|
| Cache Penetration（穿透） | 查詢不存在的 key，每次都打穿到 DB | 快取空值 / Bloom Filter |
| Cache Breakdown（擊穿） | 熱門 key 過期瞬間大量請求湧入 DB | 互斥鎖 / 永不過期+背景刷新 |
| Cache Avalanche（雪崩） | 大量 key 同時過期 | 隨機化 TTL |

#### 2. Redis 資料結構
- String、List、Hash、Set、Sorted Set、Stream。
- 不只是簡單的 key-value！

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：撰寫 docker-compose.yml（引導式）
1. 在專案根目錄建立 `docker-compose.yml`。
2. 定義三個服務：`api`（FastAPI）、`db`（PostgreSQL）、`redis`（Redis）。
3. **驗證指令**：
   ```bash
   docker-compose up -d
   curl.exe http://127.0.0.1:8000/health
   ```

#### 練習 B：實作 Redis Cache-Aside 快取（半自主）
1. 安裝 `redis` Python 套件。
2. 在 `app/services/cache.py` 中實作 `get_or_set(key, fetch_fn, ttl)` 函式。
3. 在關鍵字查詢端點中使用快取。
4. **驗證方式**：發送兩次相同請求，第二次回應時間應明顯縮短。

#### 練習 C：測量快取命中率（挑戰題）
1. 新增 `/api/v1/cache/stats` 端點，回傳 `hits`、`misses`、`hit_rate`。
2. **驗證指令**：
   ```bash
   curl.exe http://127.0.0.1:8000/api/v1/cache/stats
   ```

### 🧪 測試驗證 (Test & Verify)

**完成條件 (Definition of Done)**：
- [ ] `docker-compose up` 成功啟動所有服務
- [ ] Redis 快取命中時回應時間 < 5ms
- [ ] 能解釋 Cache-Aside 模式
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：Cache-Aside 模式是什麼？和 Write-Through 有什麼差別？**
> Cache-Aside：應用程式負責讀/寫快取，DB 是主要資料源。Write-Through：每次寫入時同時更新快取和 DB，快取永遠是最新的，但寫入延遲較高。

**Q2：什麼是 Cache Penetration？如何防範？**
> 查詢不存在的 key，快取永遠 miss，每次都打穿到 DB。防範：1) 快取空值（null value）2) 使用 Bloom Filter 在查詢前先判斷 key 是否可能存在。

**Q3：Redis 為什麼快？**
> 1) 資料存在記憶體中（不是磁碟）2) 單執行緒模型避免鎖競爭 3) 非阻塞 I/O 多路復用 4) 高效的資料結構實現（SDS、ziplist、skiplist）。

**Q4：TTL 設太長和設太短各有什麼問題？**
> 太長：資料過時但仍在快取中，使用者看到舊資料。太短：快取命中率低，大量請求打到 DB，失去快取的意義。需要根據業務場景權衡。

**Q5：Docker Compose 中服務之間如何通訊？**
> Compose 自動建立 Bridge 網路，服務可透過服務名稱（如 `redis`、`db`）作為 hostname 互相存取，不需要知道對方的 IP。

### 📎 參考資源 (References)

- [Docker Compose 官方文件](https://docs.docker.com/compose/)
- [Redis 官方文件](https://redis.io/docs/)
- [快取策略詳解](https://codeahoy.com/2017/08/11/caching-strategies-and-how-to-choose-the-right-one/)

---

## Day 12 — 分散式 NoSQL 資料庫實務 (MongoDB / MariaDB)

### 📖 核心觀念 (Core Concepts)

#### 1. 為什麼需要 NoSQL？
- **關聯式資料庫 (SQL)**：Schema 固定、ACID 事務、適合結構化資料。
- **NoSQL**：Schema 靈活、水平擴展、適合半結構化/非結構化資料。
- 不是「替代」SQL，而是「互補」。

#### 2. MongoDB 文件型資料庫 (Document Store)
- 資料以 **JSON-like 的文件 (Document)** 儲存，不需要預定義 Schema。
- 適合儲存：社群貼文、使用者行為紀錄、產品評價（每筆資料的欄位可能不同）。

#### 3. CAP 定理 (CAP Theorem)
- **Consistency (一致性)**、**Availability (可用性)**、**Partition Tolerance (分區容錯)** 三者最多只能同時滿足兩個。
- MongoDB 預設 CP（一致性 + 分區容錯），犧牲部分可用性。

#### 4. SQL vs NoSQL 選型指南
| 考量 | 選 SQL | 選 NoSQL |
|------|--------|----------|
| 資料關聯性 | 多表 JOIN 頻繁 | 獨立文件，少 JOIN |
| Schema 穩定性 | Schema 固定 | Schema 經常變動 |
| 事務需求 | 嚴格 ACID | 最終一致性可接受 |
| 擴展方式 | 垂直擴展為主 | 水平擴展（Sharding） |

#### 5. Cassandra 寬欄式資料庫
- 專為超大規模寫入設計（IoT 感測器、事件日誌）。
- 無單點故障 (No Single Point of Failure)。

### 📚 延伸知識 (Deep Dive)

#### 1. 混合架構 (Polyglot Persistence)
- 在同一個系統中使用多種資料庫，各取所長。
- 本專案：PostgreSQL（交易資料）+ MongoDB（貼文數據）+ Redis（快取）。

#### 2. MongoDB Aggregation Pipeline
- 類似 SQL 的 GROUP BY，但更靈活。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：使用 Python 連接 MongoDB（引導式）
1. 在 Docker Compose 中加入 MongoDB 服務。
2. 使用 `pymongo` 連接並寫入測試資料。
3. **驗證指令**：
   ```bash
   python scripts/test_mongodb.py
   ```

#### 練習 B：實作貼文儲存 API（半自主）
1. 建立 `POST /api/v1/posts` 端點，將使用者貼文存入 MongoDB。
2. 建立 `GET /api/v1/posts` 端點，查詢貼文。
3. 支援 `?keyword=AI` 過濾。

#### 練習 C：MongoDB Aggregation Pipeline（挑戰題）
1. 實作聲量統計聚合查詢：按關鍵字分組，計算每個關鍵字的總提及次數。
2. 建立 `/api/v1/posts/stats` 端點。

### 🧪 測試驗證 (Test & Verify)

**完成條件 (Definition of Done)**：
- [ ] 能解釋 SQL 和 NoSQL 各自的適用場景
- [ ] MongoDB 讀寫操作成功
- [ ] 能解釋 CAP 定理
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：什麼情境下選 SQL？什麼情境下選 NoSQL？**
> SQL：資料高度結構化、需要複雜 JOIN、嚴格 ACID 事務（金融、訂單）。NoSQL：資料結構多變、需要水平擴展、最終一致性可接受（社群貼文、日誌、IoT 數據）。

**Q2：什麼是 CAP 定理？**
> 分散式系統中，一致性 (C)、可用性 (A)、分區容錯 (P) 三者最多滿足兩個。現實中網路分區不可避免（P 必選），所以實際上是在 C 和 A 之間權衡。

**Q3：MongoDB 的 Document Model 和 SQL 的 Table Model 有什麼不同？**
> Document Model：每筆資料是一個 JSON 文件，可以嵌套（Embedded），不需要 JOIN。Table Model：資料扁平化存在二維表中，關聯資料需要 JOIN 多張表。

**Q4：什麼是 Polyglot Persistence？**
> 在同一個系統中使用多種資料庫技術，各取所長。例如：PostgreSQL 存交易資料（ACID）、MongoDB 存非結構化貼文、Redis 做快取、Elasticsearch 做全文搜尋。

**Q5：MongoDB 如何水平擴展？**
> Sharding（分片）：將資料依 Shard Key 分散到多個節點，每個節點只存一部分資料。配合 Replica Set（副本集）實現高可用。

### 📎 參考資源 (References)

- [MongoDB 官方教學](https://www.mongodb.com/docs/manual/tutorial/)
- [CAP 定理圖解](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/)
- [Polyglot Persistence — Martin Fowler](https://martinfowler.com/bliki/PolyglotPersistence.html)

---

## Day 13 — 大數據批次與串流管道 (Hadoop / PySpark)

### 📖 核心觀念 (Core Concepts)

#### 1. 為什麼需要大數據處理？
- 當資料量超過單機記憶體容量（GB → TB → PB），傳統的 `for` 迴圈不再適用。
- 需要分散式計算框架將資料切分到多台機器平行處理。

#### 2. Hadoop 生態系
- **HDFS**：分散式檔案系統，將大檔案切成 Block 分散儲存。
- **MapReduce**：程式設計模型，Map（映射）+ Reduce（聚合）。
- **YARN**：資源管理器。

#### 3. PySpark 基礎
- Spark 是 MapReduce 的進化版，使用記憶體內計算（比 MapReduce 快 10~100 倍）。
- PySpark 是 Spark 的 Python API。
- **核心概念**：DataFrame（類似 pandas，但可分散式計算）。

#### 4. Batch vs Stream Processing
| 面向 | Batch（批次） | Stream（串流） |
|------|--------------|----------------|
| 延遲 | 分鐘~小時 | 毫秒~秒 |
| 資料量 | 大量歷史資料 | 即時產生的資料 |
| 工具 | Spark、MapReduce | Kafka、Flink、Spark Streaming |
| 場景 | 報表、ETL | 即時儀表板、即時警報 |

#### 5. ETL Pipeline
- **Extract (擷取)**：從來源抓取原始資料。
- **Transform (轉換)**：清洗、過濾、計算衍生特徵。
- **Load (載入)**：寫入目標資料倉儲。

### 📚 延伸知識 (Deep Dive)

#### 1. Data Lake vs Data Warehouse
- **Data Lake**：原始未處理的資料（Schema on Read）。
- **Data Warehouse**：清洗整理過的資料（Schema on Write）。

#### 2. PySpark 效能調優
- 避免 `collect()` 將全部資料拉到 Driver。
- 善用 `persist()` / `cache()` 避免重複計算。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：PySpark 本機安裝與 DataFrame 操作（引導式）
1. 安裝 PySpark：`pip install pyspark`。
2. 建立 `scripts/spark_demo.py`，用 PySpark 讀取 CSV 檔案。
3. 執行基本的 `groupBy`、`count`、`filter` 操作。

#### 練習 B：實作聲量數據 ETL Pipeline（半自主）
1. 建立 `scripts/etl_pipeline.py`。
2. Extract：讀取模擬的聲量 JSON 資料。
3. Transform：清洗無效數據、計算每個關鍵字的總提及次數。
4. Load：將結果寫入 CSV。

#### 練習 C：詞頻特徵抽取（挑戰題）
1. 用 PySpark 實作 TF-IDF 詞頻特徵抽取。
2. 從聲量文本中提取最具代表性的前 20 個詞彙。

### 🧪 測試驗證 (Test & Verify)

**完成條件 (Definition of Done)**：
- [ ] 能解釋 Batch 和 Stream Processing 的差異
- [ ] PySpark ETL 腳本成功執行
- [ ] 產出的 CSV 包含正確的統計結果
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：Batch Processing 和 Stream Processing 的適用情境？**
> Batch：處理大量歷史資料，對延遲不敏感（如每日報表、ETL）。Stream：處理即時產生的資料，需要秒級回應（如即時推薦、詐欺偵測、異常警報）。

**Q2：Spark 為什麼比 MapReduce 快？**
> Spark 使用記憶體內計算（In-Memory Computing），中間結果保存在記憶體中而非磁碟。MapReduce 每個階段都要讀寫 HDFS 磁碟，I/O 是瓶頸。

**Q3：什麼是 ETL？**
> Extract（從來源擷取資料）→ Transform（清洗、轉換、計算衍生特徵）→ Load（載入目標資料倉儲）。是資料工程中最基本的數據管道模式。

**Q4：PySpark 的 DataFrame 和 pandas 的 DataFrame 有什麼不同？**
> pandas DataFrame 在單機記憶體中運算，資料量受限於單機記憶體。PySpark DataFrame 是分散式的，資料分散在叢集多個節點上平行計算，可處理 TB~PB 級資料。

**Q5：Data Lake 和 Data Warehouse 的差異？**
> Data Lake：儲存原始未處理的資料（JSON、CSV、圖片），Schema on Read，適合探索性分析。Data Warehouse：儲存清洗整理過的資料，Schema on Write，適合固定報表和 BI。

### 📎 參考資源 (References)

- [PySpark 官方文件](https://spark.apache.org/docs/latest/api/python/)
- [Apache Spark 入門](https://spark.apache.org/docs/latest/quick-start.html)
- [ETL vs ELT 比較](https://www.ibm.com/think/topics/etl-vs-elt)

---

## Day 14 — 微服務邊界拆分 (Monolith to Microservices)

### 📖 核心觀念 (Core Concepts)

#### 1. Bounded Context（限界上下文）
- 來自 Domain-Driven Design (DDD) 的核心概念。
- 每個微服務對應一個 Bounded Context，有自己的領域模型和資料庫。
- 同一個詞（如「使用者」）在不同 Context 中可能有不同含義。

#### 2. Database-per-Service 模式
- 每個微服務擁有自己的資料庫，不直接存取其他服務的資料庫。
- 服務之間透過 API 或事件通訊。
- **好處**：獨立部署、獨立擴展、技術多樣性。

#### 3. API Contract（API 合約）
- 微服務之間的通訊介面必須有明確的合約定義。
- 修改合約時要考慮向下相容 (Backward Compatibility)。
- 工具：OpenAPI Spec、Protobuf (gRPC)。

#### 4. 同步 vs 非同步通訊
| 方式 | 工具 | 適合場景 |
|------|------|----------|
| 同步 (Sync) | HTTP REST, gRPC | 需要即時回應（查詢） |
| 非同步 (Async) | RabbitMQ, Kafka | 可延遲處理（郵件、報表） |

#### 5. Saga Pattern（分散式事務模式）
- 微服務中沒有跨服務的 ACID 事務。
- Saga 將一個分散式事務拆成多個本地事務，每個本地事務成功後發布事件觸發下一步，失敗則觸發補償事務。

### 📚 延伸知識 (Deep Dive)

#### 1. 拆分策略：Strangler Fig Pattern
- 不是一次性重寫，而是逐步將單體系統的功能抽取到微服務中。
- 新功能直接用微服務開發，舊功能逐步遷移。

#### 2. API Gateway
- 微服務的統一入口，負責路由、認證、限流、日誌。
- 外部客戶端只與 Gateway 通訊，不直接存取後端服務。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：識別微服務邊界（引導式）
1. 繪製現有單體系統的功能模組圖。
2. 識別可獨立部署的 Bounded Context：
   - 市場數據抓取 (Scraper Service)
   - AI 情感分析 (Sentiment Service)
   - 計費管理 (Billing Service)
3. **驗證方式**：產出一張清晰的微服務邊界圖。

#### 練習 B：將 Scraper 拆分為獨立模組（半自主）
1. 將 `app/services/market_scraper.py` 重構為可獨立運行的模組。
2. 定義清晰的 API 合約（Input/Output Schema）。
3. 原 Router 層透過合約呼叫，而非直接 import。

#### 練習 C：實作非同步事件通知（挑戰題）
1. 建立簡單的事件發布/訂閱機制（記憶體內）。
2. 當新的聲量數據被抓取時，發布 `DataIngested` 事件。
3. AI 分析服務訂閱此事件，自動觸發情感分析。

### 🧪 測試驗證 (Test & Verify)

**完成條件 (Definition of Done)**：
- [ ] 能畫出微服務邊界圖
- [ ] 能解釋 Bounded Context 的概念
- [ ] 至少一個模組可獨立測試運行
- [ ] 已執行 `git commit` 儲存今日進度

### 🗣️ 面試問答 (Interview Q&A)

**Q1：微服務拆分帶來的最大挑戰？**
> 1) 分散式事務的複雜度 2) 網路延遲（函式呼叫 → 網路呼叫）3) 運維成本（N 個服務 × 監控 × 日誌 × 部署）4) 資料一致性問題。

**Q2：什麼是 Bounded Context？為什麼重要？**
> DDD 中的核心概念，定義一個模型有效的邊界。不同 Context 中同一個詞可能有不同含義。正確的 Bounded Context 邊界決定了微服務拆分是否合理。

**Q3：Database-per-Service 模式有什麼代價？**
> 失去跨服務 JOIN 的能力、無法使用跨資料庫 ACID 事務、資料冗餘（部分資料需要在多個服務中儲存副本）。但好處是服務間完全解耦，可獨立擴展和部署。

**Q4：同步和非同步通訊各自的優缺點？**
> 同步（HTTP/gRPC）：實現簡單、即時回應，但呼叫鏈耦合（一個服務掛了整條鏈路失敗）。非同步（Message Queue）：服務間解耦、可應對流量尖峰，但實現複雜、除錯困難。

**Q5：什麼是 Strangler Fig Pattern？**
> 一種漸進式遷移策略：不一次性重寫系統，而是像絞殺榕一樣逐步用新微服務「包圍」舊單體系統。新功能用微服務開發，舊功能逐步遷移，最終舊系統被完全替代。

### 📎 參考資源 (References)

- [Microservices Patterns — Chris Richardson](https://microservices.io/patterns/)
- [DDD — Bounded Context](https://martinfowler.com/bliki/BoundedContext.html)
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)

---
---

# 📌 第三週：Kubernetes 雲原生編排、Service Mesh (Istio)、GitOps (ArgoCD) 與 SRE

---

## Day 15 — Kubernetes (K8s) 核心編排

### 📖 核心觀念 (Core Concepts)

#### 1. Kubernetes 核心元件
- **Cluster**：一組用來運行容器化應用的節點（Nodes）。
- **Pod**：K8s 最小調度單位，包含一個或多個容器。
- **Deployment**：管理 Pod 的副本數、滾動更新、回滾。
- **Service**：為 Pod 提供穩定的網路存取入口（IP + DNS）。
- **ConfigMap / Secret**：外部化配置與敏感資訊。

#### 2. 期望狀態 (Desired State) 與調和循環 (Reconciliation Loop)
- 你告訴 K8s「我想要 3 個 API Pod 在運行」（Desired State）。
- K8s 持續監測實際狀態，如果只有 2 個 Pod，自動啟動新的。
- 這就是聲明式 (Declarative) 管理的威力。

#### 3. 常見 kubectl 指令
```bash
kubectl get pods,svc          # 查看 Pod 和 Service
kubectl describe pod <name>   # 查看 Pod 詳細資訊
kubectl logs <pod-name>       # 查看 Pod 日誌
kubectl apply -f deploy.yaml  # 套用設定檔
kubectl delete -f deploy.yaml # 刪除資源
```

### 📚 延伸知識 (Deep Dive)
- Namespace（命名空間）：邏輯隔離多個環境（dev/staging/prod）。
- Label & Selector：標籤機制，Service 透過 Selector 找到對應的 Pod。

### 🔨 實作練習 (Hands-on Exercises)

#### 練習 A：安裝 minikube 或 kind 並部署第一個 Pod（引導式）
#### 練習 B：撰寫 Deployment + Service YAML（半自主）
#### 練習 C：使用 ConfigMap 注入環境變數（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)

**Q1：K8s 的 Desired State 和 Reconciliation Loop 是什麼？**
**Q2：Pod 和 Container 的差別？**
**Q3：為什麼需要 Service？直接用 Pod IP 不行嗎？**
**Q4：ConfigMap 和 Secret 的差別？**
**Q5：什麼是 Namespace？為什麼需要它？**

### 📎 參考資源 (References)
- [Kubernetes 官方教學](https://kubernetes.io/docs/tutorials/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

---

## Day 16 — K8s 健康檢查 (Probes) 與優雅關機

### 📖 核心觀念 (Core Concepts)
- Liveness Probe：Pod 是否活著？失敗則重啟。
- Readiness Probe：Pod 是否準備好接收流量？失敗則從 Service 移除。
- Startup Probe：Pod 是否已完成初始化？避免慢啟動被 Liveness 殺掉。
- Graceful Shutdown（優雅關機）：收到 SIGTERM 後完成處理中的請求再退出。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：配置 Liveness 和 Readiness Probe（引導式）
#### 練習 B：模擬 API 死鎖觀察自動重啟（半自主）
#### 練習 C：實作 Graceful Shutdown 處理（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：Liveness 和 Readiness Probe 配置錯誤會導致什麼問題？**
**Q2：為什麼需要 Startup Probe？**
**Q3：什麼是 Graceful Shutdown？為什麼重要？**
**Q4：preStop Hook 是什麼？**
**Q5：terminationGracePeriodSeconds 的作用？**

---

## Day 17 — K8s 自動擴縮 (HPA) 與資源配額

### 📖 核心觀念 (Core Concepts)
- HPA (Horizontal Pod Autoscaler)：根據 CPU/Memory 使用率自動調整 Pod 數量。
- Resource Requests：Pod 需要的最低資源量（調度依據）。
- Resource Limits：Pod 可使用的最大資源量（超過則被 OOMKilled）。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：設定 Resource Requests 和 Limits（引導式）
#### 練習 B：配置 HPA 並觸發自動擴展（半自主）
#### 練習 C：使用壓測工具驗證擴展（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：為什麼必須設定 Resource Requests 和 Limits？**
**Q2：Requests 和 Limits 的差別？設定不當的後果？**
**Q3：HPA 的擴展延遲大約多少？為什麼不是瞬間擴展？**
**Q4：VPA 和 HPA 的差別？**
**Q5：什麼是 OOMKilled？如何排查？**

---

## Day 18 — Service Mesh (Istio) 流量管理與金絲雀部署

### 📖 核心觀念 (Core Concepts)
- Envoy Sidecar Proxy：每個 Pod 旁邊的流量代理。
- VirtualService：定義流量路由規則。
- DestinationRule：定義流量分配策略。
- Canary Deployment（金絲雀部署）：將少量流量導向新版本，驗證穩定後全量發布。
- Circuit Breaker（斷路器）：防止級聯故障。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：安裝 Istio 並觀察 Sidecar（引導式）
#### 練習 B：設定 VirtualService 實作 90/10 流量分割（半自主）
#### 練習 C：實作 Circuit Breaker 熔斷策略（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：Service Mesh 解決什麼問題？**
**Q2：什麼是金絲雀部署？和藍綠部署的差別？**
**Q3：Circuit Breaker 的三種狀態？**
**Q4：Sidecar 模式的優缺點？**
**Q5：為什麼不在應用程式碼中實作重試/熔斷？**

---

## Day 19 — GitOps (ArgoCD) 與 Helm/Kustomize 包裹

### 📖 核心觀念 (Core Concepts)
- GitOps：Git 是 Single Source of Truth，所有基礎設施變更透過 Git PR。
- ArgoCD：持續監測 Git 與 K8s 叢集的差異，自動同步。
- Helm：K8s 的套件管理器（Template + Values）。
- Kustomize：K8s 原生的配置覆蓋工具。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：使用 Kustomize 管理多環境 Overlay（引導式）
#### 練習 B：安裝 ArgoCD 並設定自動同步（半自主）
#### 練習 C：觸發 Git Push 自動部署（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：GitOps 比傳統腳本部署好在哪裡？**
**Q2：Helm 和 Kustomize 的差異？什麼時候用哪個？**
**Q3：ArgoCD 的 Sync 和 Reconciliation 機制？**
**Q4：如何用 GitOps 做 Rollback？**
**Q5：GitOps 的安全考量（Secret 管理）？**

---

## Day 20 — CI/CD 自動化 Toolchain (GitHub Actions)

### 📖 核心觀念 (Core Concepts)
- CI (Continuous Integration)：每次 commit 自動構建 + 測試。
- CD (Continuous Delivery/Deployment)：自動化部署到生產環境。
- Quality Gates：必須通過 Lint + Test + Build 才能合併。
- Immutable Artifacts：構建產物不可修改，相同 commit 永遠產出相同映像。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：撰寫 GitHub Actions Workflow（引導式）
#### 練習 B：加入 Quality Gates（半自主）
#### 練習 C：Docker Build + Push 自動化（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：CI 和 CD 的差別？**
**Q2：什麼是 Immutable Artifacts？為什麼重要？**
**Q3：Quality Gates 應該包含哪些檢查？**
**Q4：如何在 CI 中安全地使用 Secret？**
**Q5：Monorepo 和 Polyrepo 對 CI/CD 的影響？**

---

## Day 21 — SRE 可觀測性 (Prometheus & PromQL)

### 📖 核心觀念 (Core Concepts)
- RED Method：Rate (流量)、Errors (錯誤)、Duration (延遲)。
- USE Method：Utilization (使用率)、Saturation (飽和度)、Errors (錯誤)。
- Prometheus：Pull 模式監控系統，定期抓取 `/metrics` 端點。
- PromQL：Prometheus 查詢語言。
- 四種 Metric 類型：Counter、Gauge、Histogram、Summary。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：在 FastAPI 中埋點 `/metrics`（引導式）
#### 練習 B：編寫 PromQL 查詢 API 延遲（半自主）
#### 練習 C：自定義業務指標（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：Pull 模型和 Push 模型監控的差異？**
**Q2：Counter 和 Gauge 的差別？**
**Q3：RED 和 USE 方法各適合監控什麼？**
**Q4：什麼是 Histogram？為什麼用它計算 p99 延遲？**
**Q5：Prometheus 的資料保存期限和儲存方式？**

---

## Day 22 — Grafana 視覺化 Dashboard & Alertmanager

### 📖 核心觀念 (Core Concepts)
- Grafana：將 Prometheus 指標視覺化的看板工具。
- Dashboard 設計原則：Overview → Drill-down → 可行動 (Actionable)。
- Alertmanager：接收 Prometheus 告警並分發（Slack、Email、PagerDuty）。
- Alert Fatigue（警報疲勞）：太多無意義的警報導致工程師忽視重要警報。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：建立 Grafana Dashboard（引導式）
#### 練習 B：設定 Alerting Rule（半自主）
#### 練習 C：故意觸發 5xx 錯誤驗證告警（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：好的 Dashboard 應該具備什麼特徵？**
**Q2：什麼是 Alert Fatigue？如何避免？**
**Q3：Alertmanager 的路由和分組機制？**
**Q4：On-call 輪值制度怎麼設計？**
**Q5：為什麼告警應該有 Runbook 連結？**

---

## Day 23 — SRE SLI/SLO/SLA 與 Error Budget 扣減

### 📖 核心觀念 (Core Concepts)
- **SLI (Service Level Indicator)**：衡量服務品質的具體指標（如成功率、延遲）。
- **SLO (Service Level Objective)**：SLI 的目標值（如「99.9% 成功率」）。
- **SLA (Service Level Agreement)**：對客戶的正式承諾，違反有商業後果。
- **Error Budget**：允許的失敗預算 = 1 - SLO。99.9% SLO → 每月 43 分鐘的 Error Budget。
- **燃燒率 (Burn Rate)**：Error Budget 被消耗的速率，速率過快要踩煞車。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：定義本專案的 SLI 和 SLO（引導式）
#### 練習 B：計算 Error Budget 並建立看板（半自主）
#### 練習 C：實作 Error Budget 燃燒率告警（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：SLI、SLO、SLA 三者的關係？**
**Q2：Error Budget 如何平衡開發速度和穩定性？**
**Q3：99.9% 和 99.99% 的 SLO 差多少停機時間？**
**Q4：Error Budget 耗盡時應該怎麼做？**
**Q5：如何選擇合適的 SLI？**

---
---

# 📌 第四週：AI/MLOps 平台、物件儲存 (MinIO/Cassandra)、研報自動化與生產故障演練

---

## Day 24 — S3 / MinIO 物件儲存與數據治理

### 📖 核心觀念 (Core Concepts)
- Block Storage vs File Storage vs Object Storage。
- S3 API：PUT、GET、DELETE 物件。
- MinIO：S3 相容的開源物件儲存。
- Metadata 數據治理：資料品質、資料目錄 (Data Catalog)。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：部署 MinIO 並上傳檔案（引導式）
#### 練習 B：用 boto3 Python SDK 存取物件（半自主）
#### 練習 C：實作資料版本控管（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：Block Storage、File Storage、Object Storage 的差異？**
**Q2：S3 的最終一致性模型是什麼？AWS 現在還是最終一致性嗎？**
**Q3：什麼是資料治理 (Data Governance)？**
**Q4：Object Storage 為什麼適合儲存 ML 模型和大型檔案？**
**Q5：MinIO 和 AWS S3 的關係？**

---

## Day 25 — AI/ML 生命週期與特徵工程 (Feature Pipeline)

### 📖 核心觀念 (Core Concepts)
- ML 生命週期：數據收集 → EDA → 特徵工程 → 訓練 → 評估 → 部署 → 監控。
- Feature Engineering（特徵工程）：從原始資料中提取有預測力的特徵。
- Data Drift vs Concept Drift。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：建立情感分析特徵管道（引導式）
#### 練習 B：計算 Sentiment Vector 特徵矩陣（半自主）
#### 練習 C：實作 Data Drift 檢測（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：Data Drift 和 Concept Drift 的差異？**
**Q2：特徵工程為什麼比模型選擇更重要？**
**Q3：如何偵測生產環境中的 Data Drift？**
**Q4：Feature Store 是什麼？為什麼需要它？**
**Q5：One-Hot Encoding 和 Embedding 的差別？**

---

## Day 26 — MLOps / MLflow 模型註冊與管理 (Model Registry)

### 📖 核心觀念 (Core Concepts)
- Experiment Tracking：記錄每次實驗的參數、指標、程式碼版本。
- Model Registry：模型的版本控管庫（Staging → Production → Archived）。
- 可重複性 (Reproducibility)：相同程式碼 + 相同資料 = 相同結果。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：安裝 MLflow 並記錄第一個實驗（引導式）
#### 練習 B：記錄模型參數和 AUC 指標（半自主）
#### 練習 C：註冊模型並管理版本（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：MLflow 解決什麼問題？**
**Q2：Experiment Tracking 為什麼重要？**
**Q3：模型版本管理和程式碼版本管理有什麼不同？**
**Q4：什麼是模型可重複性？如何保障？**
**Q5：ML Pipeline 中的 CI/CD 和傳統 CI/CD 有什麼不同？**

---

## Day 27 — 線上 AI 推論服務 (Online Model Serving API)

### 📖 核心觀念 (Core Concepts)
- Online Inference vs Batch Inference。
- Model Serialization（Pickle、ONNX、TorchScript）。
- 推論延遲優化：模型量化、快取、預計算。
- A/B Testing 模型版本。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：建立 `/api/v1/predict` 推論端點（引導式）
#### 練習 B：載入 MLflow 模型進行推論（半自主）
#### 練習 C：實作模型 A/B Testing（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：Online Inference 和 Batch Inference 的差別？**
**Q2：如何優化推論延遲？**
**Q3：模型部署後如何確保品質？**
**Q4：什麼是 Shadow Deployment？**
**Q5：Canary Deployment 在模型部署中怎麼用？**

---

## Day 28 — 高管 PDF 商業研報與現代化 Web 控制台

### 📖 核心觀念 (Core Concepts)
- 資料視覺化原則：Edward Tufte 的「資料墨水比」。
- Dashboard 設計：Overview → Drill-down → Action。
- PDF 動態渲染技術。
- ECharts/Chart.js 圖表庫。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：體驗現有 SaaS Dashboard（引導式）
#### 練習 B：自訂圖表樣式和互動效果（半自主）
#### 練習 C：設計並實作新的分析頁面（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：好的數據視覺化應該注意什麼原則？**
**Q2：為什麼全棧能力在面試中越來越重要？**
**Q3：PDF 報告 vs 互動式 Dashboard 各自的適用場景？**
**Q4：如何讓 Dashboard 的首屏載入速度最快？**
**Q5：什麼是 SSR vs CSR？對 SEO 的影響？**

---

## Day 29 — 生產環境故障演練 (Production Incident Exercise)

### 📖 核心觀念 (Core Concepts)
- Chaos Engineering：主動注入故障，測試系統的韌性。
- 故障排除流程：症狀 → 假設 → 驗證 → 修復 → 復盤。
- Root Cause Analysis (RCA)：找到故障的根本原因，而非只修復表面症狀。
- Postmortem（事後復盤報告）：記錄故障時間線、根因、改善措施。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：模擬 API 延遲故障（引導式）
#### 練習 B：使用日誌和指標定位根因（半自主）
#### 練習 C：撰寫完整的 Postmortem 報告（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：什麼是 Chaos Engineering？為什麼 Netflix 要主動搞破壞？**
**Q2：生產環境出事故時，你的第一步是什麼？**
**Q3：Postmortem 報告應該包含哪些內容？**
**Q4：什麼是 Blameless Postmortem？為什麼重要？**
**Q5：如何預防同類故障再次發生？**

---

## Day 30 — 專案封裝、技術展演與履歷/面試 Demo

### 📖 核心觀念 (Core Concepts)
- 如何向面試官精準展示架構權衡 (Tradeoffs)。
- STAR 面試答題法（Situation → Task → Action → Result）。
- Portfolio 專案的展示技巧。
- 技術 Demo 的黃金結構：問題 → 方案 → 實作 → 結果。

### 🔨 實作練習 (Hands-on Exercises)
#### 練習 A：整理 README 和架構圖（引導式）
#### 練習 B：準備 5 分鐘技術 Demo 演講稿（半自主）
#### 練習 C：模擬面試答辯（挑戰題）

### 🗣️ 面試問答 (Interview Q&A)
**Q1：描述你做過最有挑戰性的專案。（STAR 格式）**
**Q2：如果讓你重新設計這個系統，你會做哪些不同的選擇？**
**Q3：你如何衡量系統的成功？**
**Q4：你最近學到的一個新技術是什麼？怎麼學的？**
**Q5：你如何處理意見不一致的 Code Review？**

### 📎 參考資源 (References)
- [STAR 面試法](https://www.themuse.com/advice/star-interview-method)
- [技術面試準備指南 — Tech Interview Handbook](https://www.techinterviewhandbook.org/)

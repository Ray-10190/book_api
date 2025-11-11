# Book API

這是一個簡單的 Python API 範例，使用 FastAPI 並以 `book_date.json` 提供書籍資料。

檔案
- `book_date.json`：書籍資料（JSON 陣列，檔名由使用者指定）。
- `app/main.py`：FastAPI 應用程式。
- `requirements.txt`：相依套件。
- `tests/test_api.py`：簡單測試。

本地執行（Windows PowerShell）

1. 建議建立虛擬環境並安裝相依：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

2. 啟動 API：

```powershell
uvicorn app.main:app --reload --port 8000
```

3. 在瀏覽器或 curl 測試：
- 取得全部書籍： http://127.0.0.1:8000/books
- 依分類過濾： http://127.0.0.1:8000/books?分類=800
- 取得單本： http://127.0.0.1:8000/books/0

執行測試

```powershell
# 若尚未安裝相依，先執行安裝步驟
python -m pytest -q
```

將專案上傳到 GitHub（快速步驟）

1. 在 GitHub 網站登入並建立一個新的 repository（例如 `book_api`），不要勾選 README（我們本機已經有）。

2. 在本機專案目錄執行：

```powershell
git init
git add .
git commit -m "Initial commit: Book API"
# 將 <YOUR_REMOTE_URL> 換成 GitHub 上建立的 repo URL，例如：https://github.com/yourname/book_api.git
git remote add origin <YOUR_REMOTE_URL>
git branch -M main
git push -u origin main
```

備註：
- 如果想把這個程式部署成公開的線上 API（例如 Render、Railway、Fly 或其他雲端供應商），可在 GitHub 建好 repo 後直接連結到這些平台以自動部署。Render/ Railway 通常會偵測到 `uvicorn` 並自動啟動服務，或你可以新增 `Procfile` / 部署設定。
- 若需要我幫你加上 GitHub Actions 或示範 deploy 到某個平台（例如 Render），我可以幫忙設定。
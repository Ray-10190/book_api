from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "book_date.json"

app = FastAPI(title="Book API", description="簡單的書籍資料 API", version="0.1")

# 載入資料一次
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        _BOOKS = json.load(f)
except FileNotFoundError:
    _BOOKS = []

# 在回傳時加入 id（index）以方便用 /books/{id} 取得
def _with_id(books: List[dict]) -> List[dict]:
    return [dict({"id": idx}, **book) for idx, book in enumerate(books)]

@app.get("/", summary="API root")
def root():
    return {"message": "Book API - 請使用 /books 或 /books/{id}"}

@app.get("/books", summary="取得所有書籍，可用分類或作者過濾")
def get_books(分類: Optional[str] = None, 作者: Optional[str] = None, 書名: Optional[str] = None):
    """
    可用 query params 過濾：分類、作者、書名（部分比對）
    範例：/books?分類=800
    """
    results = _BOOKS
    if 分類:
        # 完整比對（可依需求改為包含）
        results = [b for b in results if b.get("分類") == 分類]
    if 作者:
        results = [b for b in results if 作者 in b.get("作者", "")]
    if 書名:
        results = [b for b in results if 書名 in b.get("書名", "")]
    return _with_id(results)

@app.get("/books/{book_id}", summary="依 id 取得單本書籍")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(_BOOKS):
        raise HTTPException(status_code=404, detail="找不到該書籍")
    book = dict({"id": book_id}, **_BOOKS[book_id])
    return book

# 可用下列指令啟動：
# uvicorn app.main:app --reload --port 8000

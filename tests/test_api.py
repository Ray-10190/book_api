from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_books():
    r = client.get("/books")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 18  # 原始資料共 18 本


def test_filter_by_category():
    r = client.get("/books?分類=800")
    assert r.status_code == 200
    data = r.json()
    assert all(item.get("分類") == "800" for item in data)
    assert len(data) == 2


def test_get_book_by_id():
    r = client.get("/books/0")
    assert r.status_code == 200
    book = r.json()
    assert book.get("書名") == "圖書館學概論"

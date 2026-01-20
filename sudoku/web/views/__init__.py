# ไฟล์: sudoku/web/views/__init__.py
from flask import Blueprint

# ตัวแปรนี้แหละที่ Python หาไม่เจอตอนแรก
module = Blueprint("web", __name__)


@module.route("/")
def index():
    print("testttt")
    return "<h1>Hello! Sudoku from Views Folder</h1>"

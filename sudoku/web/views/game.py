# ไฟล์: sudoku/web/views/game.py
from flask import Blueprint

# ตัวแปรนี้ต้องชื่อ 'module' เท่านั้น เพราะสคริปต์ Step 2 มันมองหาชื่อนี้
module = Blueprint("game", __name__, url_prefix="/")


@module.route("/")
def index():
    return "<h1>This is Game Page (Auto Discovered!)</h1>"

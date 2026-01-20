# ไฟล์: sudoku/web/views.py
from flask import Blueprint, render_template

# สร้าง Blueprint ชื่อ 'module' (เพื่อให้ตรงกับที่คุณเรียกใน __init__.py)
module = Blueprint("web", __name__)


@module.route("/")
def index():
    # ส่งข้อความกลับไปก่อน เพื่อเทสต์ว่าระบบทำงานได้
    return "<h1>Hello! Sudoku Server is Running.</h1>"

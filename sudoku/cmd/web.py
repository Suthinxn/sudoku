from livereload import Server

from sudoku import web
import os


def main():

    app = web.create_app()
    app.debug = True

    server = Server(app.wsgi_app)

    server.watch("sudoku/web")

    print("Starting Sudoku Server at http://127.0.0.1:8000")
    server.serve()

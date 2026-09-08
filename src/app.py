from http.server import BaseHTTPRequestHandler
import os


HTML_FILE = "templates/contacts.html"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            '''Используем os.path.join, чтобы корректно склеить пути на любой ОС'''
            file_path = os.path.join(os.getcwd(), HTML_FILE)
            with open(file_path, "r", encoding="utf-8") as f:
                page = f.read()

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page.encode("utf-8"))

        except FileNotFoundError:
            self.send_error(404, "Страница contacts не найдена")
        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")



# from wsgiref.simple_server import make_server
#
# def app(environ, start_response):
#     file_path = "C:\\Users\\shari\\OneDrive\\Desktop\\2025-03-28 15-28-45.mp4"
#     with open(file_path, "rb") as file:
#         data = file.read()
#
#     status = "200 OK"
#     response_headers = [("Content-type", "video/mp4")]      # video seerverga chiqarish
#
#     start_response(status, response_headers)
#
#     return [data]
#
# server = make_server("localhost", 8000, app)
# server.serve_forever()






# from wsgiref.simple_server import make_server
# from app import FrameWorkApp
#
# app = FrameWorkApp()
#
#
# server = make_server("localhost", 8000, app)       # run bilan ishlash
# server.serve_forever()




# from app import FrameWorkApp
# import json
#
# def load_date():
#     with open("users.json", "r") as file:
#         date = json.load(file)
#
# app = FrameWorkApp()
#
# @app.route("/home")
# def home(request, response):
#     response.text = "Home pagedan siz uchun maxsus salom!"
#
# @app.route("/about")
# def about(request, response):
#     response.text = "About pagedan siz uchun maxsus salom!"
#
# @app.route("/u/{id}")
# def get_info(request, response, id):
#     user = load_date()[int(id)]
#     response.text = json.dumps(user)





"""HOMEWORK"""
from app import FrameWorkApp
import json


def load_data():
    with open("users.json", "r") as file:
        data = json.load(file)
    return data


app = FrameWorkApp()


@app.route("/home")
def home(request, response):
    response.text = "Home pagedan siz uchun maxsus salom!"


@app.route("/about")
def about(request, response):
    response.text = "About pagedan siz uchun maxsus salom!"


@app.route("/u/{id}")
def get_user_info(request, response, id, is_admin=False):
    users = load_data()

    try:
        user = users[int(id)]
        if not is_admin:
            response.text = json.dumps(user)
        else:
            response.text = "Kirish taqiqlangan: Administrator maʼlumotlarini bu yerda koʻrib boʻlmaydi."
    except (IndexError, ValueError):
        response.status_code = 404
        response.text = "User topilmadi!"


@app.route("/admin/{id}")
def get_admin_info(request, response, id, is_admin=False):
    users = load_data()

    try:
        if is_admin:
            admin_data = users[int(id)]
            response.text = json.dumps(admin_data)
        else:
            response.text = "Kirish rad etildi: Siz administrator maʼlumotlarini koʻrish huquqiga ega emassiz."
    except (IndexError, ValueError):
        response.status_code = 404
        response.text = "ADMIN topilmadi!"

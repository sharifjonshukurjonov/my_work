from app import FrameWorkApp


import json

app = FrameWorkApp()

def load_users():
    with open( "user.json","r")as file:
        users = json.load(file)
    return users
def load_admin():
    with open("admin.json", "r") as file:
        admins = json.load(file)
    return admins

@app.route("/home")
def home(request,response):
    response.text = "shuhrat pagedan alangali salom!"


@app.route("/about")
def about (request,response):
    response.text = "about pageidan alangali salom!"

@app.route("/contact")
def contact (request,response):
    response.text = "91 336 2084"



@app.route("/admin/login")
def get_admin_info(request, response, login):
    admins = load_admin()
    admin = admins.get(login)

    if admin:
        response.text = json.dumps(admin)
    else:
        response.status_code = 404
        response.text = "Admin topilmadi!"

@app.route("/u/id")
def get_user_info(request, response, id):
    users = load_users()
    user = users.get(id)

    if user:
        response.text = json.dumps(user)
    else:
        response.status_code = 404
        response.text = "User topilmadi!"

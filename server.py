from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Dummy login HTML
login_file = open("login.html")
login_page = login_file.read()
login_file.close()

# Dummy success HTML
success_file = open("success.html")
success_page = success_file.read()
success_file.close()

print(success_page)

@app.route('/')
def index():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    return render_template_string(success_page)

if __name__ == '__main__':
    app.run(debug=True)

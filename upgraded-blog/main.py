import smtplib

import requests
from flask import Flask, render_template, request

my_email = "katiwatson29@gmail.com"
password = "pythoncore"
password1 = "zxcvbnmasdfghjkl1234567890"

app = Flask(__name__)
"""here we are rendering the posts and the post data comes from api"""
api_url = 'https://api.npoint.io/0067e63917ca7a5034d9'
response = requests.get(api_url).json()
all_post = []
for res in response:
    all_post.append(res)


@app.route('/')
def get_all_posts():
    return render_template('index.html', posts=all_post)


"""here we received the info of a form from the contact.html file"""


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        display_message = 'Successfully sent your information.'
        if request.form['submit_button'] == "send":
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="katiwatson29@yahoo.com",
                                    msg=f"{name}\n{email}\n{phone}\n{message}")
                print(f'{name}\n{email}\n{phone}\n{message}')
            return render_template('contact.html', message=display_message)
    else:
        return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:id>')
def posts(id):
    render_post = None
    for p in all_post:
        if p['id'] == id:
            render_post = p
    return render_template("post.html", post=render_post)


# @app.route('/form-entry', methods=['POST'])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     print(f'{name}\n{email}\n{phone}\n{message}')
#     return f'<h1>Successfully sent your information.</h1>'


if __name__ == '__main__':
    app.run(debug=True)

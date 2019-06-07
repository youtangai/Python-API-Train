from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index(): 
    pass 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    pass

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('login'))
        print(url_for('login', next='/'))
        url_for('static', filename='style.css')
        print(url_for('show_user_profile', username='John Doe'))
    app.run(host='0.0.0.0', debug=True)


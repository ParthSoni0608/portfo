from flask import Flask, render_template, url_for, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def myhome():
    return render_template('index.html')


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        spamwriter = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email, subject, message])


@app.route('/submit-form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')

    else:
        return 'something went wrong. Try again!'

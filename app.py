from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

__author__ = 'analystbruh'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ocnkipjgkglpbs:c10bbc17c423c2bc13245a342084c97e51e99a7a50603a01590ec410fc4fa5a5@ec2-23-21-198-69.compute-1.amazonaws.com:5432/d5kbrkeb0u7cd3'
#'postgres://chrismartin@localhost:5432/guestbook'
heroku = Heroku(app)
db = SQLAlchemy(app)


class Guests(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    comment = db.Column(db.String(140))

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def index():
    guests = Guests.query.order_by(Guests.id.desc()).limit(100).all()
    return render_template('index.html', guests=guests)


@app.route('/submit', methods=['POST'])
def submit():
    new_guest = Guests(request.form['name'], request.form['comment'])
    db.session.add(new_guest)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()

# CREATE TABLE surveytable (
# 	id serial PRIMARY KEY,
# 	product VARCHAR ( 200 ) NOT NULL,
# 	dealer VARCHAR ( 200 ) NOT NULL,
# 	rating INTEGER NOT NULL,
# 	review TEXT NULL
# );

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Ella135!@localhost/surveydb'
db = SQLAlchemy(app)

class addsurvey(db.Model):
    __tablename__ = 'surveytab3'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    review = db.Column(db.Text())

    def __init__(self, product, dealer, rating, review):
        self.product = product
        self.dealer = dealer
        self.rating = rating
        self.review = review

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    product = request.form['product']
    dealer = request.form['dealer']
    rating = request.form['rating']
    review = request.form['review']
    print(product, dealer, rating, review)
    
    data = addsurvey(product, dealer, rating, review)
    db.session.add(data)
    db.session.commit()
    return render_template('success.html')
   

if __name__ == "__main__":
    app.run(debug=True)

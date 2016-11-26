from flask_api import FlaskAPI
from flask import request, jsonify, url_for, abort
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from helper import get_location_name





app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    phone = db.Column(db.String(10))
    longt = db.Column(db.String(100))
    lat = db.Column(db.String(100))
    location = db.Column(db.String(100))
    offers = db.relationship('Offer', backref=db.backref('users', lazy='select'))

    def __init__(self, username, first_name, last_name, password, phone, longt, lat):
        self.username = username
        self.password = password
        self.phone = phone
        self.longt = longt
        self.lat = lat
        self.location = -1
        self.first_name = first_name
        self.last_name = last_name


    def to_dict(self):
        return {
            'id': self.id,
            'photo': 1,
            'username':self.username,
            'phone': self.phone,
            'firstname': self.first_name,
            'lastname': self.last_name,
            'lat': self.lat,
            'longt': self.longt,
	    'location':self.location
        }

    def __repr__(self):
        return '<User %r>' % self.username



class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    offer_name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float)
    category = db.Column(db.String(100))
    longt = db.Column(db.String(100))
    status = db.Column(db.String(100))
    date = db.Column(db.Date)
    location = db.Column(db.String(100))
    lat = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    images = db.relationship('Image', backref=db.backref('offers', lazy='select'))


    def to_dict(self):
        return {
            'offer_name':self.offer_name,
            'description':self.description,
            'price':self.price,
            'category':self.category,
            'longt':self.longt,
            'status':self.status,
            'location': self.location,
            'date':self.date,
            'lat':self.lat,
            'user_id':self.user_id
        }

    def to_array(self):
        d = {
            'offer_name':self.offer_name,
            'price':self.price,
            'category':self.category,
            'status':self.status,
            'date':self.date,
            'user_id': User.query.filter_by(id=self.user_id).first().to_dict()
        }
        return d
    def __init__(self, offer_name, description, price, category, longt, lat, status, date, user_id):
        self.offer_name = offer_name
        self.description = description
        self.price = price
        self.category = category
        self.longt = longt
        self.location = get_location_name(longt, lat)
        self.status = status
        self.date = date
        self.lat = lat
        self.user_id = user_id

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    offer_id = db.Column(db.Integer, db.ForeignKey('offers.id'))
    #def __init__(self, ):



@app.route('/')
def hello_world():
    return  jsonify('Hello World!')


@app.route('/api/users/<int:id>')
def get_user_id(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/users/login', methods=['POST'])
@cross_origin()
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'id': -1})
    elif user.password == password:
        return jsonify(user.to_dict())
    return jsonify({'id': -1})



@app.route('/offers/<int:id>')
@cross_origin()
def get_offer(id):
    offer = Offer.query.get(id)
    print offer.to_dict()
    return jsonify(offer.to_dict())


@app.route('/offers', methods=['POST'])
@cross_origin()
def new_offer():
    user_id = request.json.get('user_id')
    description = request.json.get('description')
    offer_name = request.json.get('offer_name')
    category = request.json.get('category')
    longt = request.json.get('longt')
    lat = request.json.get('lat')
    price = request.json.get('price')
    status = 'D'
    date = datetime.now()
    # images = request.json.get('images')
    # for image in images:
    #     im = Image(image)
    #     db.session.add(im)
    # db.session.commit()


    offer = Offer(offer_name, description, price, category, longt, lat, status, date, user_id)
    db.session.add(offer)
    db.session.commit()
    return jsonify({'id': offer.id})

@app.route('/offers', methods=['GET'])
@cross_origin()
def offer_list():
    offers = Offer.query.filter_by().all()
    for offer in offers:
        offer.image = [1,1,1]
    array = [off.to_array() for off  in offers]
    return jsonify(array)


@app.route('/users/offers/<int:id>')
@cross_origin()
def get_offers(id):
    user = User.query.filter_by(id=id)
    offers = Offer.query.filter_by().all()
    for offer in offers:
        offer.image = [1, 1, 1]
    array = [off.to_dict() for off in offers]
    return jsonify(array)


@app.route('/users', methods=['POST'])
@cross_origin()
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    longt = '0.00000'
    lat = '0.00000'
    phone = ""
    first_name = request.json.get('firstname')
    last_name = request.json.get('lastname')
    user = User(username, first_name, last_name, password, phone, longt, lat)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

@app.route('/users', methods=['GET'])
@cross_origin()
def users_list():
    users = User.query.filter_by().all()
    array = [usr.to_dict() for usr  in users]
    return jsonify(array)

@app.route('/users/settings/<int:id>', methods=['PUT'])
@cross_origin()
def update_user(id):
    user = User.query.filter_by(id=id).first()
    user.phone = request.json.get('phone')
    user.longt = request.json.get('longt')
    user.lat   = request.json.get('lat')
    user.location = request.json.get('location')
    db.session.commit()

def init_db():
    """For use on command line for setting up
    the database.
    """

    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    #app.run('0.0.0.0', '80')
    app.run('127.0.0.1', '5000')

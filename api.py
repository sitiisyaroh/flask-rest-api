from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from flask_migrate import Migrate

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

@app.route('/index.html')
def ui():
    return app.send_static_file('index.html')

@app.route('/edit.html')
def edit_page():
    return app.send_static_file('edit.html')

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    jabatan = db.Column(db.String(80), unique=False, nullable=True)
    usia = db.Column(db.Integer, unique=False, nullable=True)
    kota = db.Column(db.String(80), unique=False, nullable=True)

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email}, jabatan = {self.jabatan}, usia = {self.usia} kota = {self.kota})"

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")
user_args.add_argument('jabatan', type=str, required=False, help="Jabatan cannot be blank")
user_args.add_argument('usia', type=int, required=False, help="Usia cannot be blank")
user_args.add_argument('kota', type=str, required=False, help="Kota cannot be blank")

userFileds = {
    'id' : fields.Integer,
    'name' : fields.String,
    'email' : fields.String,
    'jabatan' : fields.String,
    'usia' : fields.Integer,
    'kota' : fields.String,
}

class Users(Resource):
    @marshal_with(userFileds)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFileds)
    def post(self):
        args = user_args.parse_args()
        if args["name"] is None or args["email"] is None:
            abort(400, message="Both 'name' and 'email' are required fields.")

        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
class User(Resource):
    @marshal_with(userFileds)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user    
    
    @marshal_with(userFileds)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        
        # Update fields if provided
        if args["name"] is not None:
            user.name = args["name"]
        if args["email"] is not None:
            user.email = args["email"]
        if args["jabatan"] is not None:
            user.jabatan = args["jabatan"]
        if args["usia"] is not None:
            user.usia = args["usia"]
        if args["kota"] is not None:
            user.kota = args["kota"]

        db.session.commit()
        return user, 200
    
    @marshal_with(userFileds)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 200
    
class EmailFilter(Resource):
    @marshal_with(userFileds)
    def get(self, email):
        user = UserModel.query.filter(UserModel.email.ilike(f"%{email}%")).all()
        if not user:
            abort(404, "Email not found")
        return user

class NameFilter(Resource):
    @marshal_with(userFileds)
    def get(self, name):
        # Use ilike for case-insensitive search with LIKE
        user = UserModel.query.filter(UserModel.name.ilike(f"%{name}%")).all()
        if not user:
            abort(404, "User not found")
        return user
      

    
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/id/<int:id>')
api.add_resource(NameFilter, '/api/users/name/<string:name>')
api.add_resource(EmailFilter, '/api/users/email/<string:email>')

@app.route('/')
def home():
    return '''<h1><a href="/index.html" style="text-decoration: none; color: inherit;">Hello, World!</a></h1>'''

if __name__ == '__main__':
    app.run(debug=True) 
from argparse import Namespace
from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource,reqparse,abort,fields,marshal_with
from numpy import negative

# create api with flask
app = Flask(__name__)
api = Api(app)
app.secret_key="me"
# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# თუ ტემპის ფაილი გვინდა 'sqlite:///tmp/database.db'
db = SQLAlchemy(app)

# model  instance for videos storing
class BaseModel(db.Model):
    id = db.Column(db.String, primary_key=True) #  any id wil be changed 
    total = db.Column(db.Integer)
    change = db.Column( db.String)
    


# parse
base_parser = reqparse.RequestParser() #auto parse reques as guidline
# guides
base_parser.add_argument("total" ,type=int,help="give me name ! it's required",required=True) #help is erro msg
base_parser.add_argument("change" ,type=str,help="give me name ! it's required",required=True) #help is erro msg


resource_fields = {
    "id":fields.String,
    "change":fields.String,
    "total":fields.Integer
}

db.create_all()
class Data(Resource):
    @marshal_with(resource_fields)
    def get(self,account_name):
        data = BaseModel.query.filter_by(id = account_name ).first()
        if not data:
            abort(404,message=f"data is empty for this name {account_name}")
        return data 

    @marshal_with(resource_fields)
    def put(self,account_name):
        info = base_parser.parse_args()
        base = BaseModel(id = account_name, total = info["total"], change = info["change"])
        db.session.add(base) # add
        db.session.commit() 
        return base, 201 

    @marshal_with(resource_fields) 
    def patch(self,account_name):      
        info = base_parser.parse_args()
        data = BaseModel.query.filter_by(id = account_name ).first()
        if info["total"]:
            data.total = info["total"]

        if info["change"]:
            data.change = info["change"]

        db.session.commit() # commit change
        return data 
        

    def delete(self,account_name):
        data = BaseModel.query.filter_by(id = account_name ).first()
        BaseModel.query.filter_by(id = account_name ).delete()
        db.session.commit()
        return  f'video id: "{data.id}"\nname: "{data.total}" has been deleted succesfully'

api.add_resource(Data,"/data/<string:account_name>")

if __name__== "__main__":
    app.run(debug=True)
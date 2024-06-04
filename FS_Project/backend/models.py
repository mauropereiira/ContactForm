from config import db

#db model represented as python class
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #nullable means can't pass null value
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

     #take all fields on the object and convert into a dictionary to convert to json
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
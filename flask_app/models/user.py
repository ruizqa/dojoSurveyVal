# import the function that will return an instance of a connection
import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments=data['comments']

# Now we use class methods to query our database
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if len(user['name']) < 1 or len(user['location'])<1 or len(user['language'])<1 or len(user['comments'])<1:
            flash("All fields must be at least 1 character long", "register")
            is_valid = False
        return is_valid
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users ORDER BY name;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('dojo_form').query_db(query)
        users=[]
        if len(result)<1:
            return False
        else:
            for i in range(len(result)):
                user = cls(result[i])
                users.append(user)
            return users
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( name , location , language , comments) VALUES ( %(name)s , %(location)s , %(language)s ,%(comments)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_form').query_db( query, data )
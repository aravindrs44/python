from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.ninjas = []
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at  = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        print(data)
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojo = cls(results[0])
        return dojo

    @classmethod 
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
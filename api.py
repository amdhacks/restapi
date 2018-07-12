from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_restful import reqparse
#import json
#from flask import request

#conn_string = "mssql+pyodbc://x:x@x:1433/x?driver=SQL Server"
import pyodbc 


app = Flask(__name__)
api = Api(app)

#Get all the records
class Get(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start', type = str)
        parser.add_argument('end', type = str)
        #args = parser.parse_args()
        connection = pyodbc.connect(driver='{SQL Server}', server='x', database='x',user='x', password='x')
        #cursor = connection.cursor()
        query = connection.execute("SELECT * FROM testtable")
    
        results=query.fetchall()        

        json_dict = []
        for row in results:
                res = {'id': row[0], 'f_name': row[1],'l_name':row[2],'company':row[3],'city':row[4]}
                json_dict.append(res)
 
        connection.close()
        
        return jsonify(test=json_dict)

#Get one id    
class Getone(Resource):
    def get(self,pid):
        connection = pyodbc.connect(driver='{SQL Server}', server='x', database='x',user='x', password='x')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM testtable")
        response = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall() if row[0]==pid]
        connection.close()

        return jsonify(test=response)


api.add_resource(Get, '/get',methods=['GET']) #To Get all the rows
api.add_resource(Getone, '/get/<int:pid>',methods=['GET']) #To get one row
#api.add_resource(Post, '/post/<int:id>',methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)


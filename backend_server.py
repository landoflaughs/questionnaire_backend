# -*- coding: gbk -*-
from flask_cors import CORS
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


host = '192.168.202.128'
user = 'root'
password = 'root'
db = 'ubuntu_test'
charset = 'utf8mb4'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{db}'
db = SQLAlchemy(app)
api = Api(app)
CORS(app)


def router():
    from DQ_Backend.api.qustionnaire_record import QuestionnaireAdd
    from DQ_Backend.api.qustionnaire_record import QuestionnaireGet
    from DQ_Backend.api.qustionnaire_record import QuestionnaireUpdate
    api.add_resource(QuestionnaireAdd, '/add')
    api.add_resource(QuestionnaireGet, '/get')
    api.add_resource(QuestionnaireUpdate, '/update')


if __name__ == '__main__':
    router()
    app.run(debug=True)

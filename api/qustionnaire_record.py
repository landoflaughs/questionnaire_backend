# -*- coding: gbk -*-
from flask import request
from flask_restful import Resource

from DQ_Backend.backend_server import db
from DQ_Backend.data_base.ms12 import Ms12


class QuestionnaireAdd(Resource):
    def post(self):
        """
        �����ʾ��¼��������������ݷ��͵����ݿ�
        :return:
        """
        data = Ms12(**request.json)
        db.session.add(data)
        db.session.commit()
        return {"msg": "ok"}


class QuestionnaireGet(Resource):
    def get(self):
        """
        ��ȡ��¼������
        :return:
        """
        question_result = Ms12.query.all()
        format_result = [i.as_dict() for i in question_result]
        return {"msg": 'ok', "data": format_result}


class QuestionnaireUpdate(Resource):
    def post(self):
        """
        �����ʾ�
        :return:
        """
        request_body = request.json
        ques_data = Ms12(**request.json).questionnaire_data

        ms12 = Ms12.query.filter_by(project_name=request_body.get("project_name")).first()
        ms12.committer = request_body.get("committer")
        ms12.project_name = request_body.get("project_name")
        ms12.submit_time = request_body.get("submit_time")
        ms12.questionnaire_data = ques_data
        db.session.commit()
        return {"msg": "updated"}

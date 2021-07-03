# -*- coding: gbk -*-
from DQ_Backend.backend_server import db
import json


class Ms12(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    committer = db.Column(db.String(20), unique=False, nullable=False)
    project_name = db.Column(db.String(30), unique=True, nullable=False)
    ms12version = db.Column(db.String(30), unique=False, nullable=False)
    submit_time = db.Column(db.String(60), unique=False, nullable=False)
    questionnaire_data = db.Column(db.JSON, unique=False, nullable=False)

    # questionnaire_data = db.Column(db.Text, unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    def as_dict(self):
        """
        返回测试用例的数据
        :return:
        """
        return {"id": self.id, "committer": self.committer, "project_name": self.project_name,
                "ms12version": self.ms12version,
                "submit_time": self.submit_time, "questionnaire_data": self.questionnaire_data}
        # return json.dumps(dic)


if __name__ == "__main__":
    # 删库
    db.drop_all()
    # 在远程数据库中创建表
    db.create_all()

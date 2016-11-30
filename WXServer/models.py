from WXServer import db
import time


class TodoDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    open_id = db.Column(db.String(120), nullable=False)
    nick_name = db.Column(db.String(120), nullable=False)
    task_content = db.Column(db.String(200), nullable=False)
    task_plan_complete_date = db.Column(db.Date)
    task_status = db.Column(db.Integer, nullable=False)
    task_complete_date = db.Column(db.Date)
    task_create_time = db.Column(db.DateTime, nullable=False)
    task_modify_time = db.Column(db.DateTime)

    def __int__(self, open_id, nick_name, task_content, task_plan_complete_date):
        self.open_id = open_id
        self.nick_name = nick_name
        self.task_content = task_content
        self.task_plan_complete_date = task_plan_complete_date
        self.taskStatus = 1
        self.task_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def __repr__(self):
        return "<TodoDetail:{0}>".format(self.id)

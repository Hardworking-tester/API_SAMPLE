# encoding:utf-8
# author:wwg
from flask_sqlalchemy import SQLAlchemy
from flask import *
# from app import db
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123abc@localhost/api_test2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)
class FunctionModelsDb(db.Model):
    #功能模块表
    __tablename__='auto_function_modules'
    id=db.Column(db.String(128),primary_key=True)
    name=db.Column(db.String(128))#功能模块名称
    cases=db.relationship('CaseInformationDb',backref='model')
    def __repr__(self):
        return '%s ' %self.name


class CaseInformationDb(db.Model):
    #测试用例信息表
    __tablename__='auto_case_information'
    id = db.Column(db.String(128), primary_key=True)
    case_number = db.Column(db.String(128))#测试用例编号
    case_summary = db.Column(db.String(128))#测试用例概述
    url = db.Column(db.String(128))#接口测试地址
    post_data = db.Column(db.String(128))#接口测试传递参数
    post_method = db.Column(db.String(128))#接口测试方法
    model_id=db.Column(db.String(128),db.ForeignKey('auto_function_modules.id'))
    test_data = db.relationship('CaseDataDb', backref='testdata')
    element_data = db.relationship('ElementLocateDb', backref='elementdata')
    def __repr__(self):
        return '%s' %self.case_number

class CaseDataDb(db.Model):
    # 测试数据表
    __tablename__ = 'auto_test_data'
    id = db.Column(db.String(128), primary_key=True)
    key = db.Column(db.String(128))#数据输入项别名
    value = db.Column(db.String(128))#输入项待录入数据
    case_id=db.Column(db.String(128),db.ForeignKey('auto_case_information.id'))
    def __repr__(self):
        return '%s ' %self.key


class ElementLocateDb(db.Model):
    #元素定位所需数据及操作方式表
    __tablename__ = 'auto_element_locate'
    id = db.Column(db.String(128), primary_key=True)
    element_name = db.Column(db.String(128))#需要定位的元素名称
    locate_method = db.Column(db.String(128))#元素定位方式
    locate_data = db.Column(db.String(128))#元素定位所需数据
    element_introdution = db.Column(db.String(128))#元素简介
    operate_index = db.Column(db.String(128))  # 元素简介
    operate_method = db.Column(db.String(128))#元素操作方式
    case_id = db.Column(db.String(128), db.ForeignKey('auto_case_information.id'))
    def __repr__(self):
        return '%s ' %self.element_name

class ResultTestDb(db.Model):
    # 测试结果表
    __tablename__ = 'auto_test_result'
    id = db.Column(db.String(128), primary_key=True)
    case_number = db.Column(db.String(128))  # 测试用例编号
    case_result = db.Column(db.Text)  # 测试结果
    Result_flag = db.Column(db.String(128))  # 测试结果标志
    image_path = db.Column(db.String(128))  # 测试结果图片存储位置
    add_time = db.Column(db.String(128))  # 测试结果添加时间

    def __repr__(self):
        return '%s ' % self.case_number

print db.session.query(ResultTestDb).all()
print ResultTestDb.query.order_by(db.desc(ResultTestDb.add_time)).all()
# User.query.order_by(db.desc(User.id))
# db.drop_all()
# print  db.session.query(CaseDataDb).all()
# print query_case_information
# data1=CaseDataDb.query.filter_by(case_id="72dad385e32141ef9bcecce5548db40f").first()
# print db.session.query(CaseDataDb).filter_by(case_id="72dad385e32141ef9bcecce5548db40f").frist()
# print data1

# aa=db.session.query(CaseDataDb.key,CaseDataDb.value).filter_by(case_id="72dad385e32141ef9bcecce5548db40f").all()
# print type(aa)
# print aa
# bb=aa[0]
# print bb[0]
# print bb[1]
# print type(bb)

# for i in  db.session.query(CaseInformationDb).all():
#     print i.model_id

# aa=db.session.query(ElementLocateDb.element_name).filter_by(case_id='6a54c78553c3424b835dea98cd13010b').order_by(ElementLocateDb.operate_index.asc()).all()
# print aa
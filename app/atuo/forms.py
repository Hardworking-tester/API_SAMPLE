# encoding:utf-8
# author:wwg
from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import *
from .. import db
from ..models import CaseInformationDb,FunctionModelsDb
class FunctionModelsForm(Form):
    """
    新增功能模块表单
    """
    model_name=StringField(u'请输入功能模块名称',validators=[Required()])
    submit = SubmitField(u'提交')

class FunctionModelsEditForm(Form):
    """
    编辑功能模块表单
    """
    model_name=StringField(u'请输入功能模块名称',validators=[Required()])
    submit = SubmitField(u'提交')

class CaseInformationForm(Form):
    """
    新增测试用例表单
    """
    case_number=StringField(u'请输入测试用例编号',validators=[Required()])
    case_summary=StringField(u'请输入测试用例概述',validators=[Required()])
    model_name=SelectField(u'所属功能模块')
    url = StringField(u'请输入请求地址', validators=[Required()])
    post_data = StringField(u'请输入请求数据')
    post_method =SelectField(u'请选择请求方法' ,choices=[('post', 'post'),('get', 'get'),('delete', 'delete')])
    submit = SubmitField(u'提交')
    def __init__(self,*args, **kwargs):
        super(CaseInformationForm, self).__init__(*args, **kwargs)
        self.model_name.choices = [(FunctionModels.id, FunctionModels.name)
                             for FunctionModels in db.session.query(FunctionModelsDb).all()]



class DataTestForm(Form):
    """
    新增测试数据表单
    """
    data_key = StringField(u'请输入录入框别名', validators=[Required()])
    data_value = StringField(u'请输入待录入数据', validators=[Required()])
    case_id = SelectField(u'请选择该测试数据所属测试用例')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(DataTestForm, self).__init__(*args, **kwargs)
        self.case_id.choices = [(case_information.id, case_information.case_number)
                                   for case_information in db.session.query(CaseInformationDb).all()]


class ElementLocateForm(Form):
    """
    新增元素定位方式及操作方式视图
    """
    element_name = StringField(u'请输入需要定位的元素的名称', validators=[Required()])
    operate_index = StringField(u'请输入操作顺序', validators=[Required()])
    locate_method = StringField(u'请输入定位方式', validators=[Required()])
    locate_data = StringField(u'请输入定位所需数据', validators=[Required()])
    element_introdution = StringField(u'请输入元素简介', validators=[Required()])
    operate_method = StringField(u'请输入元素操作方式', validators=[Required()])
    case_id = SelectField(u'请选择该元素定位数据所属测试用例')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(ElementLocateForm, self).__init__(*args, **kwargs)
        self.case_id.choices = [(case_information.id, case_information.case_number)
                                   for case_information in db.session.query(CaseInformationDb).all()]


class SubmitTestForm(Form):
    """
    新增功能模块表单
    """

    submit = SubmitField()
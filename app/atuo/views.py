# encoding:utf-8
# author:wwg
from flask import *
import time
import urllib2,urllib
from ..action import post
from forms import FunctionModelsForm,CaseInformationForm,DataTestForm,ElementLocateForm,SubmitTestForm,FunctionModelsEditForm
from app.models import FunctionModelsDb,CaseInformationDb,CaseDataDb,ElementLocateDb,ResultTestDb
from .. import db
from . import auto
import uuid
from ..resultlog import ResultLog
@auto.route('/addModels',methods=['GET','POST'])
def addFunctionModels():
    """新增功能模块视图"""
    form=FunctionModelsForm()

    if form.validate_on_submit():
        model=FunctionModelsDb(id=str(uuid.uuid4()).replace('-',''),name=form.model_name.data)
        form.model_name.data=''
        db.session.add(model)
        db.session.commit()

    return render_template('autotemplates/AddFunctionModel.html',form_html=form)

@auto.route('/editModels',methods=['GET','POST'])
def editFunctionModels():
    """编辑功能模块视图"""

    form=FunctionModelsEditForm()
    if request.method=="POST":
        form.model_name = request.form.get('modelname')
        print "-------------------------%s-----------------------" %form.model_name
        if form.validate_on_submit():
            model=FunctionModelsDb(id=str(uuid.uuid4()).replace('-',''),name=form.model_name.data)
            form.model_name.data=''
            db.session.add(model)
            db.session.commit()


    return render_template('autotemplates/EditFunctionModel.html',form_html=form)

@auto.route('/',methods=['GET','POST'])
def index():
    """首页访问视图"""
    return render_template('autotemplates/index.html')


@auto.route('/queryModel',methods=['GET','POST'])
def queryModels():
    """查询功能模块视图"""
    query_model_name=db.session.query(FunctionModelsDb).all()
    return render_template('autotemplates/queryModel.html',model_names=query_model_name)


@auto.route('/addCase',methods=['GET','POST'])
def addCaseInformation():
    """新增测试用例视图"""
    form =CaseInformationForm()
    if form.validate_on_submit():
        id = str(uuid.uuid4()).replace('-', '')
        case_number=form.case_number.data
        case_summary=form.case_summary.data
        model_id_foreign=form.model_name.data
        url = form.url.data
        post_data = form.post_data.data
        post_method = form.post_method.data
        case_info=CaseInformationDb(id=id,case_number=case_number,case_summary=case_summary,model_id=model_id_foreign,url=url,post_data=post_data,post_method=post_method)
        form.case_number.data=''
        form.case_summary.data = ''
        form.url.data = ''
        form.post_data.data = ''
        db.session.add(case_info)
        db.session.commit()
    return render_template('autotemplates/addCaseInformation.html', form_html=form)


@auto.route('/queryCaseInformation',methods=['GET','POST'])
def queryCaseInformation():
    """查询所有测试用例视图"""
    case_data=db.session.query(CaseInformationDb.case_number, CaseInformationDb.case_summary,
                     CaseInformationDb.url, CaseInformationDb.post_data, CaseInformationDb.post_method).all()
    return render_template('autotemplates/queryCaseInformation.html',case_informations=case_data)


@auto.route('/executeTest',methods=['GET','POST'])
def executeTest():
    """执行测试"""
    query_case_information=db.session.query(CaseInformationDb).all()
    if request.method=="POST":
        for m in query_case_information:
            if request.form.get(str(m)) !=None:
                id = str(uuid.uuid4()).replace('-', '')
                case_id_list = db.session.query(CaseInformationDb.id).filter_by(case_number=request.form.get(str(m))).all()
                case_id= case_id_list[0][0]
                post_url=db.session.query(CaseInformationDb.url).filter_by(case_number=request.form.get(str(m))).all()[0][0]
                first_post_data=db.session.query(CaseInformationDb.post_data).filter_by(case_number=request.form.get(str(m))).all()[0][0]
                post_method=db.session.query(CaseInformationDb.post_method).filter_by(case_number=request.form.get(str(m))).all()[0][0]
                result=post.Post().post(post_url,eval(first_post_data))
                flag=result[0]
                result_data=result[1]
                add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                test_result_data = ResultTestDb(id=id, case_number=request.form.get(str(m)), case_result=str(result_data), Result_flag=flag,add_time=add_time)
                db.session.add(test_result_data)
                db.session.commit()
    return render_template('autotemplates/executeTest.html',case_informations=query_case_information)


@auto.route('/getResult',methods=['GET','POST'])
def getResult():
    """得到测试结果"""
    query_case_information=db.session.query(CaseInformationDb).all()
    if request.method=="POST":
        for m in query_case_information:
            if request.form.get(str(m)) !=None:
                ResultLog.ResultLog().info(request.form.get(str(m)))
                case_number=request.form.get(str(m))
                case_id_list = db.session.query(ResultTestDb.id).filter_by(case_number=case_number).all()
                result_list = db.session.query(ResultTestDb.id,ResultTestDb.case_number,ResultTestDb.Result_flag,ResultTestDb.case_result,ResultTestDb.add_time,ResultTestDb.image_path).order_by(db.desc(ResultTestDb.add_time)).filter_by(case_number=case_number).all()
    return render_template('autotemplates/getResult.html',result_data=result_list)



@auto.route('/getAllResult',methods=['GET','POST'])
def getAllResult():
    """得到全部测试用例最后一次测试结果信息"""
    result_data = []
    query_case_information=db.session.query(CaseInformationDb).all()

    for m in query_case_information:
        result_list = db.session.query(ResultTestDb.case_number, ResultTestDb.Result_flag,ResultTestDb.add_time).order_by(db.desc(ResultTestDb.add_time)).filter_by(case_number=str(m)).first()
        print result_list
        result_data.append(result_list)
    print result_data
    return render_template('autotemplates/getAllResult.html',result_data=result_data)


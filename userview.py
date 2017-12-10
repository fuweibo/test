from flask import request, g, current_app, abort, jsonify
from flask_login import login_required, current_user

import os,json
from re import sub
import logging
from .. import user_blueprint as blueprint
from app import jwt_dumps
from ..forms import LoginForm
from app import current_minio
logger = logging.getLogger("app")


@blueprint.route("/login", methods=["POST"])
def login():
    print("asd")
    print(request)
    form = LoginForm(request.form)
    if not form.validate():
        return abort(400, "invalid params")



    # TODO check from db

    # TODO 把权限编码返回。敏感信息如密码，除外
    return jwt_dumps(uuid="uuidx")


@blueprint.route("/refresh")
@login_required
def refresh():
    """ 客户端要在token失效之前，调用此接口，刷新token """
    uuid = g.jwt["uuid"]
    return jwt_dumps(uuid=uuid)


# 一般不需要
# @user.route("/logout", methods=["POST"])
# @login_required
# def logout():
#     return "hello"


@blueprint.route("/info", methods=["GET"])
@login_required
def info():
    """ demo """
    print(g.jwt["uuid"])
    return "hello"


@blueprint.route("/headimg", methods=["POST"])
@login_required
def upload_headimg():
    file = request.files['file']
    filename = file.filename

    extension = filename.rsplit('.', 1)[1] if '.' in filename else None
    if not (extension and extension in current_app.config["HEADIMG_EXTENSIONS"]):
        return abort(400, "invalid params")

    uuid = current_user.uuid
    tmp_file = "{}/{}.{}".format(current_app.config['UPLOAD_FOLDER'], uuid, extension)

    # 散列，不要都放到同一个bucket(目录)下
    from binascii import crc32
    object_name = "{}/{}.{}".format(crc32(uuid.encode()) % 71, uuid, extension)

    try:
        file.save(tmp_file)

        # TODO 需要压缩？
        # TODO mime?
        current_minio.fput_object("headimg", object_name, tmp_file)
    except Exception as e:
        logger.error("save headimg fail", exc_info=1)
        raise
    finally:
        os.unlink(tmp_file)  # 无论如何，删除临时文件

    return jsonify(state=0, msg="ok")


# for test
total = 0
@blueprint.route("/12")
def index():
    import gevent

    global total
    total += 1

    print("start ", total , 2)
    # gevent.sleep(10)
    # from app.models import Message
    #
    # q =  Message.raw("select pg_sleep(5)").execute()
    # total -= 1
    # print("end ", total)
    return "xx"


@blueprint.route("/insert_task")
def insert():
    from app.models import Task
    import datetime,json ,uuid
    areacount = {"res1":{"areaname":"1-5列","number":100},
                  "res2":{"areaname":"6-10列","number":150}
                  }
    firsttime = datetime.datetime(2017,12,9,16,10,12,946118)
    task = Task.create(uuid=uuid.uuid4(),
                       employee=uuid.uuid4(),supervisor='14512e40-fa81-49bc-80ff-a8e0aa6fa747',
                       department='00c2ed9f-8dc8-43ba-903d-85bb78de6392',
                       manager='df611ca1-9f56-4a15-8e1f-4718da7c37d0',
                       tasktype='图书回架',dt_task='每日任务',area_count=json.dumps(areacount),
                       img_url='http://localhost:5000/img.jpg',status='初审通过',
                       ftrialtime=firsttime,strialtime=firsttime,bk_type='阅览图书',
                       )
    return jsonify(state=0, msg=dict(task._data))

@blueprint.route("/select_task",methods=["POST","GET"])
def task_select():
    from app.models import Task
    task_list = Task.select().where(Task.status == "初审通过")

    for task in task_list:
        dict_task = json.loads(sub('\'', '\"',task.area_count))
        for i in range(dict_task.__len__()):
            print(dict_task['res1']['areaname'])
        # print(json.loads(sub('\'', '\"',task.area_count))['res1']["areaname"])


    return jsonify(state=0,msg="ok")


@blueprint.route("/update_task",methods=["POST","GET"])
def task_update():
    catch = request.get_json()
    from app.models import Task
    task = Task.select()
    print(task)
    return jsonify(state=0,msg="ok")
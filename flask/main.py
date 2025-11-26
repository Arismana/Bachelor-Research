from flask import Flask, request, jsonify
from bilibili_api import sync
from flask_cors import CORS
import getUpdata,getVideoData,dbs,getDivisions,getSuisan
import re

b_pattern = r'^BV[a-zA-Z0-9]{10}$' #bid的正则表达

app = Flask(__name__)
CORS(app)

@app.route('/api/register',methods=['POST'])
def register():
    data =  request.json
    username = data.get("username")
    password = data.get("password")
    return jsonify(dbs.register(username,password))

@app.route('/api/login',methods=['POST'])
def login():
    data =  request.json
    username = data.get("username")
    password = data.get("password")
    return jsonify(dbs.login(username,password))

@app.route('/api/getUpInfo', methods=['GET'])
def get_request():
    uid = request.args.get('uid') 
    username = request.args.get('username')
    upBasicData = sync(getUpdata.getUpEleinfo(uid))
    if upBasicData['result'] == 0:
        dbs.addHistory(username,'upper',uid,'uid格式错误','')
        return jsonify({'result':0})
    upVideoData = sync(getUpdata.getUpvideos(uid))
    dbs.addHistory(username,'upper',uid,'完成','')
    upInfo = {"data":{**upBasicData, 'upVideoData':upVideoData},"result":1}
    return jsonify(upInfo)

@app.route('/api/getVInfo', methods=['GET'])
def get_request_():
    bvid = request.args.get('bvid') 
    username = request.args.get('username')
    if re.match(b_pattern, bvid) is None: #主动判别bvid格式
        dbs.addHistory(username,'video',bvid,'bvid格式错误','')
        return jsonify({'result':0})
    videoBasicInfo = sync(getVideoData.getVideoInfo(bvid))
    if videoBasicInfo['result'] == 0:
        dbs.addHistory(username,'video',bvid,'啥也木搜到','')
        return jsonify({'result':2})
    try:
        videoFeedBackCiyun = sync(getVideoData.getVideoCiyun(bvid))
    except Exception:
        dbs.addHistory(username,'video',bvid,'出错了','')
        return jsonify({'result':3})
    dbs.addHistory(username,'video',bvid,'完成',videoBasicInfo['keyTag'])
    obj = {"data":{"videoBasicInfo":videoBasicInfo['info'],"videoFeedBackCiyun":videoFeedBackCiyun},'result':1}
    return jsonify(obj)

@app.route('/api/getHis', methods=['GET'])
def getHistory():
    username = request.args.get('username')
    page = request.args.get('page')
    return jsonify(dbs.getHistory(username,page))

@app.route('/api/getHisNums', methods=['GET'])
def getHisNums():
    username = request.args.get('username')
    return jsonify(dbs.getHisNums(username))

@app.route('/api/getDivisions', methods=['GET'])
def getDivs():
    username = request.args.get('username')
    dname = request.args.get('dname')
    rid = request.args.get('rid')
    tid = request.args.get('tid')
    vInfo = getDivisions.getDivVideoInfo(rid)
    dInfo = sync(getDivisions.getDivBasicInfo(tid,dname))
    dbs.addHistory(username,'分区',dname,'完成','')
    obj = {'vInfo':vInfo,'dInfo':dInfo}
    return obj

@app.route('/api/getDivOfAll', methods=['GET'])
def getAllDivs():
    username = request.args.get('username')
    result = sync(getDivisions.getAllVideoInfo())
    if(result['result']):
        dbs.addHistory(username,'分区','全区','超时','')
        return {'error':1}
    dbs.addHistory(username,'分区','全区','完成','')
    return result

@app.route('/api/getUserInfo',methods=['GET'])
def getUserInfo():
    username = request.args.get('username')
    return jsonify(dbs.getUInfo(username))

@app.route('/api/changePassword',methods=['POST'])
def changePw():
    data =  request.json
    username = data.get("username")
    newPw = data.get("newPw")
    return jsonify(dbs.changeUPsw(username,newPw))

@app.route('/api/changeGender',methods=['POST'])
def changeGender():
    data =  request.json
    username = data.get("username")
    newGender = data.get("newGender")
    return jsonify(dbs.changeGender(username,newGender))

@app.route('/api/changeIntro',methods=['POST'])
def changeIntro():
    data =  request.json
    username = data.get("username")
    intro = data.get("intro")
    return jsonify(dbs.changeIntro(username,intro))

@app.route('/api/changeBir',methods=['POST'])
def changeBir():
    data =  request.json
    username = data.get("username")
    bir = data.get("bir")
    return jsonify(dbs.changeBir(username,bir))

@app.route('/api/getSuisan',methods=['GET'])
def getSuiSan():
    username = request.args.get('username')
    return jsonify(getSuisan.getSs(username))

if __name__ == '__main__':
    app.run()  # 启动 Flask 服务器，开启调试模式

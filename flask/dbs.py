from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import getUpdata
from bilibili_api import sync

app = Flask(__name__) #创建flask实例
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/sys?charset=utf8' #配置数据库URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #SQLAlchemy对象绑定到flask实例上，就可以直接操作数据库了
#SQLAlchemy 是一个ORM（对象关系映射）库，允许开发者通过操作Python对象来与数据库进行交互，而不需要直接编写SQL查询。

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)
    birthday = db.Column(db.String(45), nullable=False)
    introdution = db.Column(db.String(45))
    registerTime = db.Column(db.String(45), nullable=False)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    type = db.Column(db.String(45), nullable=False)
    sid = db.Column(db.String(45), nullable=False)
    time = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    style = db.Column(db.String(45), nullable=False)


def register(username,password):
    with app.app_context():
        result = getUser(username)
        if(result):
            return 2
        loc = sync(getUpdata.getLocation())
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d")
        new_user = Users(username=username, password=password,gender='-',location=loc['pro']+'-'+loc['city'],birthday='-',introdution='这家伙很懒，什么都没留下',registerTime=formatted_datetime)
        db.session.add(new_user)
        db.session.commit()
        return 1
    
def login(username,password):
    with app.app_context():
        result = getUserAndpw(username,password)
        if(result):
            return 1
        else:
            return 0
    
def getUser(username): #查找用户名是否已存在
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username).first()
        return user
    
def getUserAndpw(username,password):#查找用户名密码
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username,Users.password==password).first()
        return user
    
def addHistory(username,type,sid,state,style):
    with app.app_context():
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        his = History(username=username,type=type,sid=sid,time=formatted_datetime,state=state,style=style)
        db.session.add(his)
        db.session.commit()
        return 1
    
def getHistory(username,page):
    with app.app_context():
        page_ = int(page)
        history = db.session.query(History).filter(History.username==username).all()[(page_-1)*12:(page_)*12]
        history_data = [{'username': item.username, 'type': item.type, 'sid': item.sid,'time':item.time,'state':item.state} for item in history]
        return history_data
    
def getHisNums(username):
    with app.app_context():
        return db.session.query(History).filter(History.username==username).count()

def getUInfo(username): #获取用户信息
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username).first()
        obj = {'password':user.password,'gender':user.gender,'location':user.location,'birthday':user.birthday,'introdution':user.introdution,'registerTime':user.registerTime}
        return obj
    
def changeUPsw(username,newPw):
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username).first()
        user.password = newPw
        db.session.commit()
        return {'state':1}
    
def changeGender(username,newGender):
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username).first()
        user.gender = newGender
        db.session.commit()
        return {'state':1}
    
def changeIntro(username,intro):
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username).first()
        user.introdution = intro
        db.session.commit()
        return {'state':1}

def changeBir(username,bir):
    with app.app_context():
        user = db.session.query(Users).filter(Users.username==username).first()
        user.birthday = bir
        db.session.commit()
        return {'state':1}
    
def getHistoryTag(username):
    with app.app_context():
        history = db.session.query(History).filter(History.username==username,History.type=="video",History.style!="").all()
        return history

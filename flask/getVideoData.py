from bilibili_api import video,Credential,comment
from snownlp import SnowNLP
import jieba.analyse


credential = Credential(sessdata="bdcb4b52%2C1729143977%2Cac1a5%2A42CjDRJBnkjnrrHCU3JT4HURjkSJGmbd6BuGtNZAm4_o4c24zksHg9INwhuuZ_dtWhqQISVnFSeXpiTUdMZFNwNEg1YjZsem1SdUlaWXZBbEdhVWNwNjlfaEIwMnJPck5HcFI0MF8wd3pNLUhZWk9WT1owMUdNQTFWNHNHbXFfLWJQVVlNSXFEU3BRIIEC",
                        bili_jct="7113b4510b8bf57c250e85fffdf4e7a9", 
                        buvid3="7BBFB524-C4F9-29CF-55B4-C6269D13494138486infoc", 
                        dedeuserid="496004083",
                        ac_time_value='8e00dc87fcf0c336c7fac44124bf2f42')


async def getVideoInfo(bvid):
    try:
        v = video.Video(bvid=bvid)
        info = await (v.get_info()) #获取视频总信息
    except Exception:
        return {'result':0}
    else:
        return {"info":info,'result':1,'keyTag':info['tname']} #keyTag:视频关键标签，用于分析用户的喜好

async def getVideoCiyun(bvid):
    v = video.Video(bvid=bvid)
    dms = await(v.get_danmakus(page_index=0,from_seg=0,to_seg=1)) #获取视频弹幕
    ndms = danmuQingXi(dms) #弹幕清洗
    cms = await(getVideoComment(bvid))#获取视频评论信息
    danmuQxtj = anylize(ndms) #弹幕情绪统计
    commentsQxtj = anylize(cms) #评论情绪统计
    sentence = ''
    danmuSenti = 0
    cmSenti = 0
    for c in ndms:
        sentence += c #合成评论
        danmuSenti += SnowNLP(c).sentiments
    danmuScore = (danmuSenti / len(ndms)) * 100
    for c in cms:
        sentence += c #合成评论
        cmSenti += SnowNLP(c).sentiments
    pinglunScore = (cmSenti / len(cms)) * 100
    vFeedBackKws = danmuKeyWords(sentence) #弹幕关键词统计
    obj = {"vFeedBackKws":vFeedBackKws,"danmuAz":{'danmuScore':danmuScore,'danmuQxtj':danmuQxtj},"pinglunAz":{'pinglunScore':pinglunScore,'commentsQxtj':commentsQxtj}}
    return obj

def danmuKeyWords(danmu):
    sentence = danmu
    keywords = jieba.analyse.extract_tags(sentence , topK=50, withWeight=True, allowPOS=(['n']))
    return keywords

async def getVideoComment(bvid):
    v = video.Video(bvid=bvid)
    aid = v.get_aid()
    comments = []
    cs = []
    c = await (comment.get_comments_lazy(aid,comment.CommentResourceType.VIDEO,1,20,comment.OrderType.TIME,credential))
    comments.extend(c['replies'])
    for cmt in comments:
         cs.append(f"{cmt['content']['message']}")
    return cs

def danmuQingXi(dms): #数据清洗
    nDms = []
    for d in dms:
        w = d.text
        if  len(w) != 0:
            nDms.append(w)
    return nDms

def anylize(data): #弹幕/评论情绪分析与统计
    sentStatic = {'ac':0,'xj':0,'zl':0}
    for d in data:
        score = SnowNLP(d).sentiments
        if(score<=0.4):
            sentStatic['xj'] += 1
        elif(score>=0.6):
            sentStatic['ac'] += 1
        else:
            sentStatic['zl'] += 1
    sentStatic['ac'] = sentStatic['ac'] / len(data)
    sentStatic['xj'] = sentStatic['xj'] / len(data)
    sentStatic['zl'] = sentStatic['zl'] / len(data)
    return sentStatic
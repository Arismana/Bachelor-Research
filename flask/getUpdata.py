import jieba.analyse
from bilibili_api import user,sync,video
from bilibili_api import Credential,client


credential = Credential(sessdata="28e6f541%2C1725952252%2Ca9df2%2A32CjCzQCP0_Nwj0HoqAc_ZvsrqrZrGaeK2ZrOPtj7Q2baQNErfgdwtqiGiefYzn-hY2VQSVmExNTBfanNzUl9YNkZMNzNWYzUyOTNqU2hGalRycHFRWnpWZ092TDdRN093VXlEQ2hDQVhUZGt1d0xpM2E3bFVDUjBIVGFsWFhQS1hXSlhsOU5FbGVBIIEC",
                        bili_jct="377c22ecdb5a6d6d4035089b2f024d82", 
                        buvid3="7BBFB524-C4F9-29CF-55B4-C6269D13494138486infoc", 
                        dedeuserid="496004083",
                        ac_time_value='7864784869284ffd2335bddeaf607e32')

async def getUpEleinfo(uid):
    u = user.User(uid=uid)
    try:
        inf = await u.get_user_info()#获取用户基本信息
        flo = await u.get_relation_info() #获取关注数和粉丝数
    except Exception:
        return {'result':0}
    else:
        basicInfo = {**inf, **flo,"result":1}
        return basicInfo

async def getUpvideos(uid):
    u = user.User(uid,credential)
    videoInfo = await u.get_media_list() #获取近期视频信息
    s = ''
    for v in videoInfo['media_list']: #获取视频标签
        tags = await getTags(v['bv_id'])
        for t in tags:
            s += t['tag_name']
    keywords = danmuKeyWords(s) #视频标签词频统计
    return {'keywords':keywords,'videoInfo':videoInfo}

def danmuKeyWords(s):
    sentence = s
    keywords = jieba.analyse.extract_tags(sentence , topK=50, withWeight=True, allowPOS=(['n']))
    return keywords

async def getTags(bvid):
    v = video.Video(bvid=bvid)
    return await(v.get_tags())

async def getLocation():
    loc = await client.get_zone()
    return {'pro':loc['province'],'city':loc['city']}



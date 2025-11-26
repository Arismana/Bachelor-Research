from bilibili_api import video_zone,sync
import getVideoData,getUpdata
import requests

headers = {
    'Accept': 'application/json, text/plain, */*', #数据接受优先级
    'Origin': 'https://www.bilibili.com', #请求从B站主页发起
    'Host': 'api.bilibili.com', #请求地址
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0', 
    #通过Chrome请求，绕开反爬虫机制
    'Accept-Language': 'zh-cn',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bilibili.com/v/popular/rank/all' #目标资源所在的完整路径
}


def getDivVideoInfo(rid):
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=' + rid + '&type=all'
    r = requests.get(url, headers = headers)
    videoList = r.json()['data']['list'] #dict 该类排行页面总信息
    varr = []
    for v in videoList:
        title = v['title']
        bvid = v['bvid']
        playData = v['stat']
        dur = v['duration']
        try:
            loc = v['pub_location']
        except KeyError:
            loc = '未知'
            continue
        obj = {'title':title,'bvid':bvid,'playData':playData,'dur':dur,'loc':loc}
        varr.append(obj)
    return varr

async def getAllVideoInfo():
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
    r = requests.get(url, headers = headers)
    videoList = r.json()['data']['list'] #dict 该类排行页面总信息
    varr = []
    s = ''
    try:
        for v in videoList:
            title = v['title']

            bvid = v['bvid']

            tags = await getUpdata.getTags(bvid)
            for t in tags:
                s += t['tag_name']

            playData = v['stat']

            tid = v['tid']
            tname = getTname(tid)

            dur = v['duration']
            try:
                loc = v['pub_location']
            except KeyError:
                loc = '未知'
                continue
            obj = {'title':title,'bvid':bvid,'playData':playData,'dur':dur,'loc':loc,'tname':tname}
            varr.append(obj)
    except Exception:
        return {'result':1}
    else:
        keywords = getUpdata.danmuKeyWords(s)
        return {"varr":varr,"keywords":keywords,"result":0}

async def getDivBasicInfo(tid,dname):
    basicinfo = (video_zone.get_zone_info_by_name(dname))[0]
    hotTags = await video_zone.get_zone_hot_tags(tid)
    obj = {'basicinfo':basicinfo,'hotTags':hotTags}
    return obj

def getTname(tid):
    if(tid==1 or tid==24 or tid==25 or tid==27 or tid==47 or tid==86 or tid==210 or tid==253 or tid==257): 
        return '动画'
    if(tid==3 or tid==28 or tid==29 or tid==30 or tid==31 or tid==59 or tid==130 or tid==193 or tid==243 or tid==244): 
        return '音乐'
    if(tid==4 or tid==17 or tid==19 or tid==65 or tid==121 or tid==136 or tid==171 or tid==172 or tid==173): 
        return '游戏'
    if(tid==5 or tid==71 or tid==137 or tid==241 or tid==242): 
        return '娱乐'
    if(tid==11): 
        return '电视剧'
    if(tid==13 or tid==32 or tid==33 or tid==51 or tid==152): 
        return '番剧'
    if(tid==23): 
        return '电影'
    if(tid==36 or tid==122 or tid==124 or tid==201 or tid==207 or tid==208 or tid==209 or tid==228 or tid==229): 
        return '知识'
    if(tid==119 or tid==22 or tid==26 or tid==126 or tid==127 or tid==216): 
        return '鬼畜'
    if(tid==129 or tid==20 or tid==154 or tid==156 or tid==198 or tid==199 or tid==200 or tid==255): 
        return '舞蹈'
    if(tid==155 or tid==157 or tid==158 or tid==159 or tid==252): 
        return '时尚'
    if(tid==160 or tid==21 or tid==138 or tid==161 or tid==162 or tid==239 or tid==250 or tid==251 or tid==254): 
        return '生活'
    if(tid==167 or tid==153 or tid==168 or tid==169 or tid==170 or tid==195): 
        return '国创'
    if(tid==177): 
        return '纪录片'
    if(tid==181 or tid==85 or tid==182 or tid==183 or tid==184 or tid==256): 
        return '影视'
    if(tid==188 or tid==95 or tid==230 or tid==231 or tid==232 or tid==233): 
        return '科技'
    if(tid==202 or tid==203 or tid==204 or tid==205 or tid==206): 
        return '资讯'
    if(tid==211 or tid==76 or tid==212 or tid==213 or tid==214 or tid==215): 
        return '美食'
    if(tid==217 or tid==75 or tid==218 or tid==219 or tid==220 or tid==221 or tid==222): 
        return '动物圈'
    if(tid==223 or tid==176 or tid==227 or tid==240 or tid==245 or tid==246 or tid==247 or tid==248): 
        return '汽车'
    if(tid==234 or tid==164 or tid==235 or tid==236 or tid==237 or tid==238 or tid==249): 
        return '运动'


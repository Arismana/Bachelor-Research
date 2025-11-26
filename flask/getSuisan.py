import dbs
from datetime import datetime
from bilibili_api import search,sync
import random

def getSs(username):
    history = dbs.getHistoryTag(username)
    if(len(history) == 0): #用户没有搜索记录
        ssVideos = sync(getLikeVideos('',0))
        ssUps = [{'mid':5294454,'uname':'逗比的雀巢','upic':'https://i0.hdslb.com/bfs/face/e56d8c14d3b74b4e32fbaf2ac4af119328c56c93.jpg'},
                 {'mid':1271916102,'uname':'上将王司徒','upic':'https://i0.hdslb.com/bfs/face/1382786fbc113f7037b3bd4305166085611f737e.jpg'},
                 {'mid':447317111,'uname':'Meetfood觅食','upic':'https://i2.hdslb.com/bfs/face/bea5c769459bddb4b955c19ce4e4dc3d8b46f8ea.jpg'},
                 {'mid':8237763,'uname':'阿张RayZhang','upic':'https://i0.hdslb.com/bfs/face/2df5b1949170bc1dc6e6f41bf5bb771b198ef8a1.jpg'},
                 {'mid':628845081,'uname':'电棍otto','upic':'https://i0.hdslb.com/bfs/face/ecf4c55dad9446deed5cf67e5906f71fbbd6c032.jpg'},
                 {'mid':14110780,'uname':'凉风Kaze','upic':'https://i1.hdslb.com/bfs/face/e0cc906bb531195e9ee9f3b575effdd2b056eaea.jpg'}
                 ]
        return {'ssVideos':ssVideos,'ssUps':ssUps}
    current_datetime = datetime.now()
    now = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    time_1_struct = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    ssVideos = [] #推荐视频列表
    ssUps = [] #推荐up主列表
    for item in history:
        hisTime = datetime.strptime(item.time, "%Y-%m-%d %H:%M:%S")
        seconds = (time_1_struct - hisTime).total_seconds()
        style = item.style
        if seconds <= 604800: #近7天的搜索
            ssVideos = ssVideos + sync(getLikeVideos(style,12))
            ssUps = ssUps + sync(getLikeUps(style,12))
        elif seconds > 604800 and seconds <= 1209600: #近14天的搜索
            ssVideos = ssVideos + sync(getLikeVideos(style,6))
            ssUps = ssUps + sync(getLikeUps(style,6))
        if(len(ssVideos) >= 88): 
            random.shuffle(ssVideos)
            random.shuffle(ssUps)
            return {'ssVideos':ssVideos,'ssUps':ssUps[0:6]}
    random.shuffle(ssVideos)
    random.shuffle(ssUps)
    return {'ssVideos':ssVideos,'ssUps':ssUps[0:6]}
    


async def getLikeVideos(tag,num):
    if(tag==''):
        return random.sample((await search.search_by_type('镇站之宝', search_type=search.SearchObjectType.VIDEO,order_type=search.OrderVideo.CLICK, time_range=10, page=1, debug_param_func=print))['result'],30)
    result = (await search.search_by_type(tag, search_type=search.SearchObjectType.VIDEO,order_type=search.OrderVideo.TOTALRANK, time_range=10, page=1, debug_param_func=print))['result']
    chosen = random.sample(result,num)
    return chosen

async def getLikeUps(tag,num):
    result = (await search.search_by_type(tag, search_type=search.SearchObjectType.USER,order_type=search.OrderUser.FANS, time_range=10, page=1, debug_param_func=print))['result']
    chosen = random.sample(result,num)
    return chosen
from bilibili_api import video_zone,sync

print(video_zone.get_zone_info_by_tid('13')[0]) #获取分区信息

# print(sync(video_zone.get_zone_top10(tid=20))) #分区前十

# print(video_zone.get_zone_list()) #获取所有分区

# print(sync(video_zone.get_zone_hot_tags(tid=3))) #获取当前分区热门tag

# print(sync(video_zone.get_zone_videos_count_today())) #全部分区今日投稿数量

# print(sync(video_zone.get_zone_new_videos(tid=20))) #获取当前分区最新投稿

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
url='https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
r = requests.get(url, headers = headers)
json_data = r.json()['data']['list']  #dict 该类排行页面总信息
print(json_data)
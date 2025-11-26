from bilibili_api import user,sync,Credential,client,video,comment



credential = Credential(sessdata="bdcb4b52%2C1729143977%2Cac1a5%2A42CjDRJBnkjnrrHCU3JT4HURjkSJGmbd6BuGtNZAm4_o4c24zksHg9INwhuuZ_dtWhqQISVnFSeXpiTUdMZFNwNEg1YjZsem1SdUlaWXZBbEdhVWNwNjlfaEIwMnJPck5HcFI0MF8wd3pNLUhZWk9WT1owMUdNQTFWNHNHbXFfLWJQVVlNSXFEU3BRIIEC",
                        bili_jct="7113b4510b8bf57c250e85fffdf4e7a9", 
                        buvid3="7BBFB524-C4F9-29CF-55B4-C6269D13494138486infoc", 
                        dedeuserid="496004083",
                        ac_time_value='8e00dc87fcf0c336c7fac44124bf2f42')

u = user.User(14110780,credential)
# print(sync(u.get_media_list()))



print(sync(u.get_user_info()))




# print(sync(u.get_followers()))
# from datetime import datetime
# # print(sync(client.get_zone()))
# current_datetime = datetime.now()
# formatted_datetime = current_datetime.strftime("%Y-%m-%d")
# print(formatted_datetime)







# print(v.get_aid())

# comments = []

# cs = []

# c = sync(comment.get_comments_lazy('BV1e2421T74v',comment.CommentResourceType.VIDEO,1,20,comment.OrderType.TIME,credential))


# comments.extend(c['replies'])

# # print(comments)

# for cmt in comments:
#     # print(f"{cmt['member']['uname']}: {cmt['content']['message']}")
#     cs.append(f"{cmt['content']['message']}")

# print(cs)

# dms = sync(v.get_danmakus(page_index=0,from_seg=0,to_seg=1))

# print(type(dms))
# danmu = []


# for d in dms:
#     print(type(d.text))

# print(danmu)

# print(dms[0])

# for cmt in c:
#     print(f"{cmt['member']['uname']}: {cmt['content']['message']}")


# v = video.Video(bvid="BV1mt42137Uk")

# print(sync(v.get_info()))

# from bilibili_api import search

# print(sync(search.search_by_type("镇站之宝", search_type=search.SearchObjectType.VIDEO,order_type=search.OrderVideo.CLICK, time_range=10, page=1))['result'])
# print(sync(search.search_by_type("音乐", search_type=search.SearchObjectType.USER,order_type=search.OrderUser.FANS, time_range=10, page=1, debug_param_func=print))['result'])
# import time

# time_stamp = time.time()
# time_struct = time.localtime(time_stamp)    # 首先把时间戳转换为结构化时间
# time_format = time.strftime("%Y-%m-%d %H:%M:%S",time_struct)        # 把结构化时间转换为格式化时间
# print(time_format)

# time_struct = time.strptime(time_format,"%Y-%m-%d %H:%M:%S")   # 首先把格式化时间转换为结构化时间
# time_stamp = time.mktime(time_struct)
# print(time_stamp)

# from datetime import datetime

# # current_datetime1 = datetime.now()
# time_1 = "2024-05-11 21:00:25"
# # print(time_1)

# time_2 = "2024-04-11 15:54:44"

# time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
# time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")
# seconds = (time_2_struct - time_1_struct).total_seconds()
# print(seconds)

# a = ""
# if(a==''):
#     print(1)
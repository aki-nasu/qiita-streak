import requests

URL = "https://qiita.com/api/v2/"

def get_user_items(user_id):
    return requests.get(URL + "users/" + user_id + "/items").json()

# import datetime

# # test1
# # case: きょうだけ書いた。
# # output:
# #   current_streak:1
# #   most_streak:1
# def get_user_items(user_id):
#     t_date = datetime.datetime.now() - datetime.timedelta(days=0)
#     t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#     r = [{'created_at': t_strdate + 'T20:18:43+09:00'}]
#     return r

# # test2
# # case: きょう含めて3日続けて書いた。
# # output:
# #   current_streak:3
# #   most_streak:3
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now()
#     for i in range(3):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     return r


# # test3
# # case: 昨日だけ書いた。
# # output:
# #   current_streak:1
# #   most_streak:1
# def get_user_items(user_id):
#     t_date = datetime.datetime.now() - datetime.timedelta(days=1)
#     t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#     r = [{'created_at': t_strdate + 'T20:18:43+09:00'}]
#     return r

# # test4
# # case: 昨日含めて3日続けて書いた。
# # output:
# #   current_streak:3
# #   most_streak:3
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now() - datetime.timedelta(days=1)
#     for i in range(3):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     return r

# # test5
# # case: 一昨日だけ書いた。
# # output:
# #   current_streak:0
# #   most_streak:1
# def get_user_items(user_id):
#     t_date = datetime.datetime.now() - datetime.timedelta(days=2)
#     t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#     r = [{'created_at': t_strdate + 'T20:18:43+09:00'}]
#     return r

# # test6
# # case: 一昨日含めて3日続けて書いた。
# # output:
# #   current_streak:0
# #   most_streak:3
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now() - datetime.timedelta(days=2)
#     for i in range(3):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     return r

# # test7
# # case: 一昨日含めて3日連続書いたけど、昔7日連続書いたときがある
# # output:
# #   current_streak:0
# #   most_streak:7
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now() - datetime.timedelta(days=2)
#     for i in range(3):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     t_date = datetime.datetime.now() - datetime.timedelta(days=180)
#     for i in range(7):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     return r

# # test8
# # case: 一昨日含めて7日連続書いたけど、昔3日連続書いたときがある
# # output:
# #   current_streak:0
# #   most_streak:7
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now() - datetime.timedelta(days=2)
#     for i in range(7):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     t_date = datetime.datetime.now() - datetime.timedelta(days=180)
#     for i in range(3):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     return r

# # test9
# # case: Qiitaに記事なんて書かないよ
# # output:
# #   current_streak:0
# #   most_streak:0
# def get_user_items(user_id):
#     r = []
#     return r

# # test10
# # case: 10,000日欠かさずQiitaに記事を投稿しています！
# # output:
# #   current_streak:10000
# #   most_streak:10000
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now() - datetime.timedelta(days=1)
#     for i in range(10000):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     t_date = datetime.datetime.now() - datetime.timedelta(days=180)
#     return r

# # test11
# # case: 1日10投稿で毎日365日投稿しました。
# # output:
# #   current_streak:365
# #   most_streak:365
# def get_user_items(user_id):
#     r = []
#     t_date = datetime.datetime.now() - datetime.timedelta(days=1)
#     for _ in range(365):
#         t_strdate = datetime.datetime.strftime(t_date, '%Y-%m-%d')
#         for _ in range(10):
#             r.append({'created_at': t_strdate + 'T20:18:43+09:00'})
#         t_date -= datetime.timedelta(days=1)
#     t_date = datetime.datetime.now() - datetime.timedelta(days=180)
#     return r

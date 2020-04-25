import datetime
import qiita_request

def compareYMD(d1, d2):
    return d1.year == d2.year and d1.month == d2.month and d1.day == d2.day

r = qiita_request.get_user_items(input('username : '))

current_streak = 0
most_streak,most_tmp = 0,0
n = len(r)
if n == 0:
    print("current streak: " + str(current_streak))
    print("most streak: " + str(most_streak))
    exit(0)

r_created_at = [datetime.datetime.strptime(r[i]['created_at'].split('T')[0], '%Y-%m-%d') for i in range(n)]

inc_day = datetime.timedelta(days=1)
pre_date = datetime.datetime.now()

if compareYMD(pre_date, r_created_at[0]) or compareYMD(pre_date, r_created_at[0] + inc_day): current_streak += 1
most_tmp += 1
most_streak = max(most_streak, most_tmp)

pre_date = r_created_at[0]

for i in range(1,n):
    if compareYMD(pre_date, r_created_at[i]): continue
    if compareYMD(pre_date, r_created_at[i] + inc_day):
        if current_streak > 0: current_streak += 1
        most_tmp += 1
    else:
        if current_streak > 0: current_streak *= -1
        most_streak = max(most_streak, most_tmp)
        most_tmp = 1
    pre_date = r_created_at[i]
most_streak = max(most_streak, most_tmp)

if current_streak < 0: current_streak *= -1
print("current streak: " + str(current_streak))
print("most streak: " + str(most_streak))
exit(0)
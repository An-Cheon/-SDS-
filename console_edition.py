import cursor
import os
def clear():#清空cmd
    os.system('cls')
cursor.hide()
defalt_information = "SAS采用4级评分，主要评定症状出现的频度，其标准为:\n" \
                     "\"1\"表示没有或很少时间有\n" \
                     "\"2\"表示有时有\n" \
                     "\"3\"表示大部分时间有\n" \
                     "\"4\"表示绝大部分时间或全部时间都有\n"
question_list = ['我感到沮丧，郁闷','我感到早上心情最好','我要哭或想哭','我夜间睡眠不好','我吃饭像平时一样多'
                 ,'我的性功能正常','我感到体重减轻','我为便秘烦恼','我的心跳比平时快','我无故感到疲劳'
                 ,'我的头脑像往常一样清楚','我做事情像平时一样不感到困难','我坐卧不安,难以保持平静'
                 ,'我对未来感到有希望','我比平时更容易激怒','我觉得决定什么事很容易','我感觉自己是有用和不可缺少的人'
                 ,'我的生活很有意义','假若我死了别人会过的更好','我仍旧喜爱自己平时喜爱的东西']
print(defalt_information)
no_use = input("输入任意键继续\n")
clear()
sum_score = 0
j = 0
for i in range(10000000):
    print(question_list[j])
    temp_choice = input("" \
                     "\"1\"表示没有或很少时间有\n" \
                     "\"2\"表示有时有\n" \
                     "\"3\"表示大部分时间有\n" \
                     "\"4\"表示绝大部分时间或全部时间都有\n"
                        "")
    # 反向评分题
    if (j == 1) or (j == 4) or (j == 5) or (j == 10) or (j == 11) or (j == 13) or (j == 15) or (j == 16) or (j == 17) or (j ==19):
        temp_choice = str(5 - int(temp_choice))
    temp = j
    if temp_choice == '1':
        sum_score = sum_score + 1
        j = j + 1
    if temp_choice == '2':
        sum_score = sum_score + 2
        j = j + 1
    if temp_choice == '3':
        sum_score = sum_score + 3
        j = j + 1
    if temp_choice == '4':
        sum_score = sum_score + 4
        j = j + 1
    if temp == j:
        print("输入数字有误，请输入:1,2,3,4")
    clear()
    if j == len(question_list) - 1:
        break
final_score = sum_score / 80
if final_score < 0.5:
    print("无抑郁")
if 0.5 <= final_score < 0.59:
    print("轻微至轻度抑郁")
if 0.6 <= final_score < 0.69:
    print("中度至重度抑郁")
if final_score >= 0.7:
    print("重度抑郁")
print("")
print("我们要生活，不要追问。生命有许多美好的事情~")
print("请允许他人爱你呀~相信这份爱~为他们活下去，即使你觉得毫无意义~")
no_use = input("输入任意键退出\n")
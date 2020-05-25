i = int(input('净利润:'))

if i <= 100000:
    bonus = i * 0.1
    print("奖金", bonus, "元")
elif 100000 <= i <= 200000:
    bonus = (i - 100000) * 0.075 + 10000
    print("奖金", bonus, "元")

#有更好的方法解决，if实在太麻烦
# i = int(raw_input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print (i-arr[idx])*rat[idx]
#         i=arr[idx]
# print r

temper = list(map(int, input().split()))
btn = int(input())

btns_gap = [0] * btn
btns_tem = [0] * btn

time = abs(temper[0] - temper[1])

for x in range(btn):
    btns_tem[x] = (int(input()))
    btns_gap[x] = (abs(temper[1] - btns_tem[x]))
  
min = btns_gap[0]
btn_sel = 0
#print(f'min : {min}')
for i in range(btn):
    if min > btns_gap[i]:
        min = btns_gap[i]
        btn_sel = i

if time > min:
    temper[0] = btns_tem[btn_sel]
    time = abs(temper[0] - temper[1]) + 1

if time >= 600 :
    time = -1

print(time)
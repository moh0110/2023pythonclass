import random as r
import time as t

slot = [0, 0, 0] # slot = [0]*3
n = int(input('슬롯머신을 몇번 돌릴까요? '))
for s in range(n):
    for k in range(3):
        slot[k] = r.randrange(7, 10)
        print('%d ' % slot[k], end ='')
        t.sleep(1)
    if slot[0] + slot[1] + slot[2] == 21:
        print('\n잭팟이 터졌네요')
        break
    else:
        print('\n아까워\n')
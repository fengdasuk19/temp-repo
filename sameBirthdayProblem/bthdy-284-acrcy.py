# -*- coding: utf-8 -*-

b = 1.0

for i in range(365 - 284 + 1, 366): #284 人中 任 2 人生日都不同的概率
 a = i / 365.0
 b = b * a
 
P0 = 1.0 - b  #284 人中 至少两个人同一天生日的概率P0

b = 1.0

for i in range(364 - 282 + 1, 365): #284 - 2 = 282 人中 任 2 人生日都不同的概率
 a = i / 365.0
 b = b * a
  
P1 = ((284 * 283 / 2.0) * (1 / 365.0)) * b #284 人中 恰好 2 人生日相同的概率

print "P1 =",P1

P2 = P0 - P1 #284 人中 至少 3 人生日相同的概率

print "P2 =",P2

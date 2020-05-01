li=[]
import math
def solution(area):
  while area>0:
      num=math.floor(math.sqrt(area))
      num=num*num
      li.append(num)
      area = area-num
  return li
print(str(solution(15324))[1:][:-1])
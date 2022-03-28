# DemoDict.py

#함수를 정의
def calc(a,b):
    return a+b, a*b

#첫번쨰 컬럼 이동
result = calc(3,4)
print(result[0])
print(result[1])

#타입캐스팅(형식변환):List, Tuple, Set 형식 변환
a = set((1,2,3,))
print(a)
print(type(a))
b = list(a)
print(b)
b.append(5)
print(b)

#딕셔너리
d = {"apple":"red", "kiwi":"green"}
print(len(d))
print(d["apple"])
d["banana"] = "yellow"
print(d)

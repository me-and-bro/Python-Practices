#cabinet = {3:"돼지", 100:"거북이"}

# print(cabinet)
#
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3))

# print(cabinet.get(5))
# print(cabinet.get(5, "자료 없음"))

# ## Dictionary
# locations = {"A-3":"화장실", "B-99":"거실"}
#
# print(locations)
# locations["A-3"] = "다락방"
# locations["C-33"] = "안방"
# print(locations)
#
# del locations["A-3"]
# print(locations)
#
# print(locations.keys())
#
# print(locations.values())
#
# print(locations.items())
#
# ## 전체 삭제
# locations.clear()
# print(locations)

# ## Tuple
#
# menu = ("초밥", "돈까스")
# print(menu[0])
# print(menu[1])
#
# ## 튜플은 선언 후 추가 불가능
#
# name, age, hobby = "김문욱", 24, "달리기"
# print(name, age, hobby)

## Set(집합)
## 중복 안되는 성질, 순서 없음

# my_set = {1,2,3,3,3}
# print(my_set) # {1,2,3}
#
# A = {1, 3, 5}
# B = set([1, 2, 3])
#
# ## 교집합
# print(A & B)
# print(A.intersection(B))
#
# ## 합집합
# print(A | B)
# print(A.union(B))
#
# ## 차집합
# print(A - B)
# print(A.difference(B))
#
# ## 추가 및 삭제
# A.add(4)
# print(A)
# A.remove(3)
# print(A)

menu = {"밥", "반찬"}
countries = ["korea", "Japan", "USA", "China", "Russia", "Finland", "Germany"]
gold = [0, 4, 5, 10, 3, 0, 2]
silver = [2, 8, 0, 10, 4, 1, 4]
bronze = [1, 5, 1, 5, 2, 0, 2]

# 상위 3개 나라 메달 수 기준 정렬
medals = []
for  i in range(len(countries)):
    medals.append((gold[i]+silver[i]+bronze[i],countries[i]))

l = list(range(39))
l1 = list(l[::3])
l2 = list(l[2::3])

print(l1)
print(l2)

print(medals)
for i in range(len(l1)):
    c = 0
    for j in range(len(medals)):
        if medals[j][0]<l2[i] and medals[j][0]>=l1[i]:
            c+=1
    print("{}~{}: {}".format(l1[i], l2[i]-1, "*"*c))


medals.sort()
medals.reverse()
print(medals[:3])

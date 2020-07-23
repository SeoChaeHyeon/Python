heads = int(input("머리 수:"))
legs = int(input("다리 수:"))

dog = int(legs / 2 - heads)
chicken = int(heads - dog)

print("강아지의 수:{}".format(dog))
print("닭의 수:{}".format(chicken))
# a = int(input())
# b = int(input())
# count = 1
# lista = []
# for i in range(a, b):
#     if count % 4 == 0:
#         print(*lista)
#         lista = []
#     else:
#         lista.append(i)
#         lista.append('|')
#     count = count + 1

# ent = input().split()
# lista = []
# i = 0
# while i < len(ent): 
#     num = ent[i]
#     if len(num) != 4:
#         for j in range(int(ent[i-1]), int(ent[i+1]) + 1):
#             if j not in lista:
#                 lista.append(j)
#         i += 2
#     else:
#         if int(num) not in lista:
#             lista.append(int(num))
#         i += 1

# print(sorted(lista))

# 4158 a 4159 4194 à 4201 4203 à 4244 4246 à 4257 4259 à 4263 4265 à 4274 4276 à 4300 4302 à 4326 4328 à 4357 4359 à 4362 4365 à 4387 4389 a 4407 4447 4449 a 4464 4468 a 4484 4486 a 4500 4502 à 4544 4546 à 4568 4570 à 4620 4622 à 4634 4636 à 4646 4648 à 4650 4652 à 4660 4662 à 4663 4665 à 4676 4679 à 4708 4710 a 4714 4716 à 4734 4737 4740 4742 4795 4804 4811 4161 à 4179 4181 à 4185 4187 à 4201 4203 à 4244 4246 à 4257 4259 à 4263 4265 à 4274 4276 à 4300 4302 à 4326 4328 à 4357 4359 à 4362 4364 à 4387 4389 à 4407 4409

listinha = []
for i in range(4143,4883):
    listinha.append(i)
print(*listinha)
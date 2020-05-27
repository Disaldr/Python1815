# def sum(*args):
#     temp = args[0]
#
#     for i in range(1,len(args)):
#         temp += args[i]
#
#     return temp
#
#
# print(sum(0,1,3,4,123))
#
def intro(**data):
    print(type(data))
    if "name" in data.keys():
        print("Ура, имя было передано")
    for key, item in data.items():
        print(key, item)


intro(name = "Sasha", gender = "Male", city = "Moscow")

print(1,2,3,4,5,6,7,8,9,0,0,123,3123,123,123,123,123,123,123,123,123)


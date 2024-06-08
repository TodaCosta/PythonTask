# old_dict = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
#             {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
#
#
# def delete_dub(old_dict):
#     new_dict = []
#     for i in old_dict:
#         if i not in new_dict:
#             new_dict.append(i)
#     return new_dict
#
#
# print(delete_dub(old_dict))
# [{'key1': 'value1'}, {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}, {}, {'key2': 'value2'}]

# x=200
# m=3
# n=9
# count = m+1
# c=x+1000
# s=0
# ff=0
# while count <= n: #4<9
#     ff=n-count #
#     if m<ff:
#         s = s+c*m
#         c +=1000
#         count+=m
#     else:
#         s = (n-m)*c #2000 (last flow)
#         count+=m
# mx = (m-1)*x #from 2 to 5 = 4000
# s=s+x+mx #over 2000+200+4000=6200
# print(s)

gg=200
ffff=0
hhh=5
mm=2
oo=hhh%mm
for i in range(0,hhh-1,mm):
    print(i)
    sss = gg*mm #400
    ffff+=sss#400
    gg +=1000 #1200
ffff += oo*gg
print(ffff)



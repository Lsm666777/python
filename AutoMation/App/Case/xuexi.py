# str = 'lisit'
# print(str[2:-1])
#
# list = []
# list.extend([1,2,3,4,5,6,7,8,9,10])
# # print(list)
#
# tuple = ('z','x','c')
# list.insert(5,tuple)
# print(list)

# a = 'sasasx'
# print(a[2])


# for i in [1,2,3,4,5,6,7]:
#     if i == 8:
#         break
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('aaa')


# for a in range(0,5+6,2):
#     print(a)


# a = {'tom':180,'jack':165,'kite':190}
# for b in a:
#     print(a[b])

#while 循环
# e = ['z','x','c']
# i = len(e)
# while i != 0:
#     print(e[-i])
#     i = i - 1
#

# str = 'zhourunfa,xiaoxiao,chengyaojin'
# print(str[str.find('f'):str.find('e')+1])

# a = [1,2,3,4,5,6,7]
# for w in a:
#     print(w)

# a = {'fg','as','fv','as','er','k','x','lh','fh','e','hb','dp'}
# for e in a:
#     print(a[e])



# def paixu(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#     return nums
# print(paixu([2,25,45,23,43,65,23,44,45]))

# a = [2,25,45,23,43,65,23,44,45]
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)
# for w in  a:
#     print(w)

# a = ('z','x','c')
# for i in a:
#     print (i)



# a,b = 1,2
# while a < 10:
#     print(b,end = ",")
#     a,b = b,a + b
    # b,a = a,b+a

# print("{0} and {1} and {2}".format('out','go','fall'))
# import math
# print('常量PI的近似值为:{0:.3f}。'.format(math.pi))

#
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name, number in table.items():
#     print('{0:10}{1:5d}'.format(name, number))


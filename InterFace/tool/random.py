import random
# class Random(object):
#     def random(self):
#         array = random.sample('23456789',8)
#         # array = "".join(random.sample('1234567890',8))
#         return array
# a = Random().random()
# print(a)


a = list(range(1,39))
b = random.sample(a,7)
number1 = b[0]
print(number1)
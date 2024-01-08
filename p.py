# # # # # # def square(num):
# # # # # #     return num * num

# # # # # # print(square(5))

# # # # # # def add(n1, n2):
# # # # # #     return n1 + n2

# # # # # # print(add(5, 8))

# # # # # def sum(*si):
# # # # #     result = 0
# # # # #     for i in si:
# # # # #         result += i
# # # # #     return result

# # # # # print(sum(1, 2, 3))
# # # # # print(sum(1, 2, 3, 4, 5))

# # # # def pirnt_kwargs(**pirnt_kwargs):
# # # #     print(type(pirnt_kwargs))
# # # #     print(pirnt_kwargs)

# # # # print(pirnt_kwargs(n1 = 5, n2 = 8))
# # # # print(pirnt_kwargs(id = "Sooha", pw = "1234"))

# # # def power(b = 2, n = 2):
# # #     return pow(b, n)

# # # print(power())
# # # print(power(3))
# # # print(power(5, 2))
# # # print(power(n = 3))

# # def plus_and_minus(n1, n2):
# #     return n1 + n2, n1 - n2

# # result = plus_and_minus(8, 5)
# # print(result)

# # result1, result2 = plus_and_minus(8, 5)
# # print(result1, result2)

# def calc(op, n1, n2):
#     result = 0
#     if op == "+":
#         result = n1 + n2
#     elif op == "-":
#         result = n1 - n2
#     elif op == "*":
#         result = n1 * n2
#     elif op == "/":
#         result = n1 / n2
    
#     return result

# print(calc("+", 8, 5))
# print(calc("-", , 5))

# def avg(*abc):
#     sum_all = 0
#     count_all = 0

#     for i in abc:
#         sum_all += i
#     count_all = len(abc)

#     return (sum_all / count_all)

# print(avg(1, 3, 5, 19, 25))
# a = 10 
# sum = 10

# def var_scope(a):
#     # global sum
#     sum += a
    
# var_scope(10)
# print(sum )

# def func1(n1, n2):
#     def inner_func2(num1, num2):
#         return num1 + num2
#     return inner_func2(n1, n2)
# print(func1(1, 2))

# def count(n):
#     if n >= 1:
#         print(n, end=" ")
#         count(n -1 )
#     else:
#         return

# count(10)

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n * sum(n - 1)
    
# print(sum(10))

# li = [1, 2, 3, 4, 5]
# print(li)

# square = lambda n : n * n
# li =  list(map(square, li))
# print(li)

# li_1 = [1, 2, 3, 4, 5]
# li_2 = [6, 7, 8, 9, 10]
# pluscal = lambda n_1, n_2 : n_1 + n_2
# li = list(map(pluscal, li_1, li_2))

# print(li)

# li = list(range(10))
# print(li)
# evens = filter(lambda n : n % 2 is 0, li)
# print(list(evens))

# import functools
# li = list(range(10))
# sum = functools.reduce(lambda x, y: x + y, li)
# print(sum)
# len = functools.reduce(lambda x, y: x + 1, li, 0)
# print(len)
# max = functools.reduce(lambda x, y: x if x > y else y, li)
# print(max)

def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# print(gen())
# print(list(gen()))

# for i in gen():
#     print(i)

# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

def gen_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
    
for i in gen_even(10):
    print(i)

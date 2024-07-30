from func_with_return import *

#Task a
avg: float = my_avg(99, 90)
print(avg)

#Task b
head1: str = my_headline("python has concurred the world")
print(head1)

#Task c
a: list = [1, 2]
b: list = [3, 4, 5, 6]
c: list = [7, 8, 9]
d: list = concat_list(a, b, c)
print(f"{d} - The len of the list is {len(d)}")

#Task d
b1: str = say_bool(True)
print(b1)

def find_nth_digit(number, index):
    n = list(str(number))
    i = n[-index]
    i = int(i)
    print(i)


num = int(input())
ind = int(input())

find_nth_digit(num, ind)

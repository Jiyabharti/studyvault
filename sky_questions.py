
# def solution(N):




numbers = ['2', '6', '7']
added = numbers.append('5')


print(added)
#
# index_of_the_number= 0
# for number in range(len[list_N]):
#     if list_N[number] < '5':
#    index_of_the_number = number
# list_N.insert(index_of_the_number, '5')


list(map(int, input().split()))


def solution(N):

    numbers = [int(d) for d in str(abs(N))]

    # Find the maximum value by inserting "54321" at each position
    max_value = N
    for i in range(len(numbers) + 1):
        new_value = int(''.join(map(str, numbers[:i] + [5, 4, 3, 2, 1] + numbers[i:])))
        max_value = max(max_value, new_value)

    return max_value


def find_highest_and_lowest(arr):
    if not arr:
        return None, None

    highest = lowest = arr[0]

    for num in arr:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

    return highest, lowest



my_array = [3, -7, 9, 2, -5]
highest_num, lowest_num = find_highest_and_lowest(my_array)

print("Highest number:", highest_num)
print("Lowest number:", lowest_num)



def solution(N):
    string = str(N)
    if N >= 0:
        for i in range(len(string)):
            if string[i] < '5':
                return int(string[:i] + '5' + string[i:])
        return int(string + '5')
    else:
        for i in range(1, len(string)):
            if string[i] > '5':
                return int(string[:i] + '5' + string[i:])
        return int('-5' + string[1:])

    # def solution(A, B):
    #     A.sort()
    #     B.sort()
    #     i = 0
    #     for a in A:
    #         i < len(B) - 1 and B[i] < a:
    #         i += 1
    #
    # if a == B[i]:
    #     return a
    # return -1








# # ASK CLAUDE AI if this is correct
# def solution(A, B):
#     A.sort()
#     B.sort()
#     i = 0
#     for a in A:
#         if i < len(B) - 1 and B[i] < a:
#             i += 1
#         if a == B[i]:
#             return a
#     return -1
#
#
# # A = ([1, 3, 2, 1],
# # B = [4, 2, 5, 3, 2])
#
# def solution(A, B):
#     A.sort()
#     B.sort()
#     i = 0
#     for 1 in A:
#         if 0 < 5 - 1 and B[0] < 1:
#             0 += 1
#         if 1 == B[0]:
#             return 1
#     return -1
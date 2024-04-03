# def generate_combinations(P, Q):
#     combinations = []
#     for i in range(len(P)):
#         for j in range(len(Q)):
#             new_string = ''
#             if i == j :

#     return combinations

def solution(P, Q):
    global length
    global letter_map
    global num_of_distinct

    length = len(P)
    letter_map = {}

    for i in range(length):
        letter_map[i] = [P[i], Q[i]]

    num_of_distinct = []
    backtrack([], 0)

    return min(num_of_distinct)  # Sử dụng hàm min() để trả về giá trị nhỏ nhất


def backtrack(arr, index):
    if len(arr) == length:
        distinct_set = set(arr)
        num_of_distinct.append(len(distinct_set))
        return  # Kết thúc khi đạt được một tổ hợp đầy đủ

    for letter in letter_map[index]:
        arr.append(letter)
        backtrack(arr, index + 1)
        arr.pop()


# Test cases
print(solution("abc", "bcd"))  # Output: 2
print(solution("axxz", "yzwy"))  # Output: 2
print(solution("bacad", "abada"))  # Output: 1
print(solution("amz", "amz"))  # Output: 3

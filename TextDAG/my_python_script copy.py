# def solution(P, Q):
#     map = [[P[i], Q[i]] for i in range(len(P))]
#     for i in map[]:

# # Test cases
# print(solution("abc", "bcd"))  # Output: 2
# print(solution("axxz", "yzwy"))  # Output: 2
# print(solution("bacad", "abada"))  # Output: 1
# print(solution("amz", "amz"))  # Output: 3


# def generate_strings(map, index, current, strings):
#     # Nếu đã duyệt qua hết các vị trí trong map, thêm tổ hợp hiện tại vào danh sách strings
#     if index == len(map):
#         strings.append(''.join(current))
#         return

#     # Duyệt qua các ký tự tại vị trí index trong map
#     for letter in map[index]:
#         current[index] = letter
#         generate_strings(map, index + 1,
#                               current, strings)

def generate_strings(map, index, current, strings):
    if index == len(map):
        strings.append(''.join(current))
        return
    for letter in map[index]:
        current[index] = letter
        generate_strings(map, index + 1, current, strings)


def solution(P, Q):
    map = [[P[i], Q[i]] for i in range(len(P))]
    strings = []
    generate_strings(map, 0, [''] * len(P), strings)
    min_unique = float('inf')
    for i in strings:
        unique = len(set(i))
        if unique < min_unique:
            min_unique = unique
    return min_unique


print(solution("abc", "bcd"))  # Output: 2
print(solution("axxz", "yzwy"))  # Output: 2
print(solution("bacad", "abada"))  # Output: 1
print(solution("amz", "amz"))  # Output: 3
# # Test case
# P = 'axxz'
# Q = 'yzwy'
# map = [[P[i], Q[i]] for i in range(len(P))]
# S = []
# generate_strings(map, 0, [''] * len(P), S)
# print(S)

# def generate_strings(P, Q):
#     length = len(P)
#     S = []

#     def backtrack(arr, index):
#         if len(arr) == length:
#             # Lưu trữ tổ hợp hiện tại vào list S.
#             S.append(arr.copy())
#             return

#         # Thử chọn ký tự từ P và Q tại vị trí index.
#         for char in (P[index], Q[index]):
#             arr.append(char)
#             backtrack(arr, index + 1)
#             # Không cần sử dụng `pop` để loại bỏ phần tử khỏi arr.

#     backtrack([], 0)
#     return S


# # Test cases
# P = "abc"
# Q = "bcd"
# strings = generate_strings(P, Q)

# print("Số lượng tổ hợp:", len(strings))
# print("Các tổ hợp:")
# for string in strings:
#     print(string)

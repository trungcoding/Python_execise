# def solution(P, Q):
#     len_P = len(P)
#     len_Q = len(Q)
#     if len_P != len_Q:
#         return False
#     length = len(P)

#   # Tạo dictionary lưu trữ số lần xuất hiện của mỗi ký tự.
#     count = {}
#     for char in P + Q:
#         count[char] = count.get(char, 0) + 1

#   # Tìm số lượng ký tự ít xuất hiện nhất trong tất cả các tổ hợp.
#     min_distinct = float('inf')
#     for i in range(2**length):
#         # Tạo set lưu trữ các ký tự trong tổ hợp hiện tại.
#         chars = set()
#     for j in range(length):
#         if (i >> j) & 1:
#             chars.add(Q[j])
#         else:
#             chars.add(P[j])

#     # Tính số lượng ký tự ít xuất hiện nhất trong set.
#     min_distinct = min(min_distinct, min(count[char] for char in chars))

#     return min_distinct


# # Test cases
# print(solution("abc", "bcd"))  # Output: 2
# print(solution("axxz", "yzwy"))  # Output: 2
# print(solution("bacad", "abada"))  # Output: 1
# print(solution("amz", "amz"))  # Output: 3

def generate_combinations(P, Q):
    """
    Hàm tạo ra list chứa tất cả các tổ hợp có thể tạo thành từ P và Q.

    Args:
      P: String đầu tiên.
      Q: String thứ hai.

    Returns:
      List chứa tất cả các tổ hợp.
    """

    length = len(P)
    S = []

    def backtrack(arr, index):
        if len(arr) == length:
            # Lưu trữ tổ hợp hiện tại vào list S.
            S.append(arr.copy())
            return

        # Thử chọn ký tự từ P và Q tại vị trí index.
        for char in (P[index], Q[index]):
            arr.append(char)
            backtrack(arr, index + 1)
            # Không cần sử dụng `pop` để loại bỏ phần tử khỏi arr.

    backtrack([], 0)
    return S


# Test cases
P = "abc"
Q = "bcd"
combinations = generate_combinations(P, Q)

print("Số lượng tổ hợp:", len(combinations))
print("Các tổ hợp:")
for combination in combinations:
    print(combination)

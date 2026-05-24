if __name__ == "__main__":
    [n, m, k] = [int(i) for i in input().split()]

    desiredAptSizes = [int(i) for i in input().split()]

    aptSizes = [int(i) for i in input().split()]

    res = 0

    desiredAptSizes.sort()
    aptSizes.sort()

    ptr1, ptr2 = 0, 0

    while ptr1 < n and ptr2 < m:
        if aptSizes[ptr2] - k <= desiredAptSizes[ptr1] and aptSizes[ptr2] + k >= desiredAptSizes[ptr1]:
            res += 1
            ptr1 += 1
            ptr2 += 1
        elif aptSizes[ptr2] + k < desiredAptSizes[ptr1]:
            ptr2 += 1
        else:
            ptr1 += 1

            
    print(res)


# if __name__ == "__main__":
#     [n, m, k] = [int(i) for i in input().split()]

#     desiredAptSizes = [int(i) for i in input().split()]

#     aptSizes = [int(i) for i in input().split()]

#     res = 0

#     desiredAptSizes.sort()
#     aptSizes.sort()

#     for i in desiredAptSizes:

#         low = 0
#         high = len(aptSizes) - 1
#         idealIdx = -1

#         while low <= high:
#             mid = low + (high - low) // 2

#             if aptSizes[mid] >= i - k and aptSizes[mid] <= i + k:
#                 idealIdx = mid
#                 high = mid - 1
#             elif aptSizes[mid] < i - k:
#                 low = mid + 1
#             else:
#                 high = mid - 1

            
#         if idealIdx != -1:
#             res += 1
#             aptSizes = aptSizes[:idealIdx] + aptSizes[idealIdx + 1:]
            
    
#     print(res)

        

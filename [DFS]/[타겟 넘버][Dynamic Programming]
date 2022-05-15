#Link : https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    dp = [0.5 for _ in range(2**len(numbers))]
    dp[0] = numbers[0]
    dp[1] = numbers[0]*(-1)
    level = 1
    end = 2
    while level < len(numbers):
        for j in range(end,len(dp)):
            if dp[j] == 0.5: 
                end = j
                break
        for i in range((end*2)-1, -1, -2):
            dp[i] = dp[int((i-1)/2)] - numbers[level]
            dp[i-1] = dp[int((i-1)/2)] + numbers[level]
        level += 1
    answer = dp.count(target)
    return answer

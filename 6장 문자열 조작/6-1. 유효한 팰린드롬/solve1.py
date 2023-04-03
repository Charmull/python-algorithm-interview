# 풀이1: 리스트로 변환

# 조건:
# 1. 직접 입력을 받아 팰린드롬 여부 판별
# 2. 대소문자 구분하지 않음
# 3. 영문자, 숫자만을 대상으로 함

def isPalindrome(s: str) -> bool:
    # 전처리 과정(조건에 맞도록 input 문자열 정리)
    strs = []
    for char in s:
        # isalnum(): 영문자, 숫자 여부를 판별하는 함수
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
        
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
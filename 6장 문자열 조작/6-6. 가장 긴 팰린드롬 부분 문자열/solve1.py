# 풀이1: 중앙을 중심으로 확장하는 풀이

def longestPalindrome(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        # left와 right의 범위가 s의 처음과 끝 인덱스를 넘지 않도록 하고,
        # s[left]와 s[right]가 같으면, 좌우로 한 칸씩 확장
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    
    # 예외 처리: 문자열 전체 길이가 2보다 작거나, 전체 문자열이 팰린드롬인 경우
    if len(s) < 2 or s == s[::-1]:
        return s
    
    # 슬라이딩 윈도우 우측으로 이동하면서 max로 비교
    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    
    return result

print(longestPalindrome("babad"))
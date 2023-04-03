# 풀이1: 리스트 컴프리헨션, Counter 객체 사용

import collections
import re
from typing import List

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # 데이터 클렌징(입력값에 대한 전처리 작업) 필요
    # 정규식 \w는 단어 문자, ^는 not을 의미 -> 단어 문자가 아닌 모든 문자를 공백으로 치환
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]
    
    # # 다음과 같이 defaultdict 사용도 가능
    # counts = collections.defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    # return max(counts, key=counts.get)
    
    counts = collections.Counter(words)
    # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    # counts.most_common(1)의 리턴값 예시: [('ball', 2)]
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", "hit"))
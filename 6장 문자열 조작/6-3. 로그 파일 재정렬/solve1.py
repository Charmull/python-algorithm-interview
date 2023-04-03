# 풀이1: 람다와 +연산자를 이용

from typing import List

def reorderLogFiles(logs:List[str]) -> List[str]:
    # 문자로 구성된 로그와 숫자로 구성된 로그를 각각 담을 리스트 선언
    letters, digits = [], []
    for log in logs:
        # 식별자 다음 문자열이 숫자이면 digits에 append
        if log.split()[1].isdigit():
            digits.append(log)
        # 아니면 letters에 append
        else:
            letters.append(log)
    
    # 2개의 키를 람다 표현식으로 정렬
    # 식별자 제외한 문자열 [1:]을 키로 하여 정렬, 동일할 경우 후순위로 식별자를 키로 하여 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits
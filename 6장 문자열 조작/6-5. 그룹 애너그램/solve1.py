# 풀이1: 정렬하여 딕셔너리에 추가

from typing import List
import collections

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # 존재하지 않는 키 삽입 시 KeyError 발생하지 않도록 항상 디폴트를 생성해주는 defaultdict()로 선언
    anagrams = collections.defaultdict(list)

    for word in strs:
        # sorted(): 문자열, 리스트를 정렬하여 리스트 형태로 리턴
        # 정렬한 문자열을 키, 그 그룹에 해당하는 애너그램들을의 리스트를 값으로 하는 딕셔너리 구성
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
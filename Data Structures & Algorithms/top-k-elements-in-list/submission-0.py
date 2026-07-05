class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = [[] for _ in range(len(nums)+1)]
        answer = []
        for i in nums:
            d[i] = d.get(i,0) + 1
        for n,f in d.items():
            result[f].append(n)
        for i in range(len(result)-1,-1,-1):
            for j in result[i]:
                answer.append(j)
                k -= 1
                if k == 0:
                    return answer
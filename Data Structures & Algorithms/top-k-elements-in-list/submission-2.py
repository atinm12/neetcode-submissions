class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqcount = [[] for i in range(len(nums)+1)]
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
                number = freq[num]
                #remove num from freqcount[number-1], put num into freqcount[number]
                freqcount[number-1].remove(num)
                freqcount[number].append(num)
            else:
                freq[num] = 1
                freqcount[1].append(num)
        output = []
        for index in range (len(freqcount)-1, -1, -1):
            if not (freqcount[index] == []):
                for num in freqcount[index]:
                    output.append(num)
                    k -= 1
                    if k == 0: return output
        return output

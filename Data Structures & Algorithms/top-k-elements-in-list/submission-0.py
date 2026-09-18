class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # Step 1: Count frequencies
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] = freq[i] + 1
            else:
                freq[i] = 1

    # Step 2: Convert hashmap to list
        freq_list = list(freq.items())

    # Step 3: Sort by frequency (descending)
        freq_list.sort(key=lambda x: x[1], reverse=True)

    # Step 4: Take top k elements and extract numbers
        top_k = freq_list[:k]
        result = [num for num, count in top_k]

        return result

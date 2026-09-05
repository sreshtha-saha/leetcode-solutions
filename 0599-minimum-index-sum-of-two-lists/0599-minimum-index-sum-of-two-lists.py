class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}

        for i, word in enumerate(list1):
            index_map[word] = i

        min_sum = float('inf')
        answer = []

        for j, word in enumerate(list2):
            if word in index_map:
                total = index_map[word] + j

                if total < min_sum:
                    min_sum = total
                    answer = [word]
                elif total == min_sum:
                    answer.append(word)

        return answer
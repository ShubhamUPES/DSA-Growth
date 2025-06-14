class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = defaultdict(list)

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dict1[i + j].append(list1[i])

        min_sum = min(dict1)
        return dict1[min_sum]

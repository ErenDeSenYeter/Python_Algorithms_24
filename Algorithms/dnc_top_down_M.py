class Solution(object):
    def sortArray(self,nums):
        #Iterative merge sort using SORTED
        mid = len(nums) // 2
        left = sorted(nums[:mid])
        right = sorted(nums[:mid])
        C = []
        while min(len(left), len(right)) > 0:
            if left[0] > right[0]:
                insert = right.pop(0)
                C.append(insert)
            elif left[0] <= right[0]:
                insert = left.pop(0)
                C.append(insert)
        if len(left) > 0:
            for i in left:
                C.append(i)
            if len(right) > 0:
                for i in right:
                    C.append(i)
            return C
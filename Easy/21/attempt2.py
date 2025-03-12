class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # This solution doesnt work with linked lists
        newList = []
        if list1[0] < list2[0]: newList.append(list1.pop(0))
        else: newList.append(list2.pop(0))
        while len(list1) >= 0 or len(list2) >= 0:
            print(newList, list1, list2)
            
            if list1[0] <= list2[0]: 
                newList.append(list1.pop(0))
            else: 
                newList.append(list2.pop(0))
            
            if len(list1) < 1: 
                for i in list2: newList.append(i)
                return newList
            elif len(list2) < 1:
                for j in list1: newList.append(j)
                return newList
        return newList

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    print(Solution.mergeTwoLists(Solution, list1, list2))
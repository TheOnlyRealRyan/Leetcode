# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""LEARN ABOVE SINGLY-LINKED LISTS"""
""" IN PROGRESS"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = []
        count = 0
        while len(list1) != 0:
            for j in list2:
                if count >= len(list1):
                    count = 0
                    
                if j < list1[count]:                                     
                    newList.append(j)
                    count +=1
                elif j == list1[count]:              
                    newList.append(j)
                    newList.append(list1[count])
                    list1.pop(0)
                    count = 0
                    pass
                else:
                    newList.append(list1[count])
                    newList.append(j)
                    list1.pop(0)
                    count += 1
                    pass           
            
        return newList

        
if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    print(Solution.mergeTwoLists(Solution, list1, list2))
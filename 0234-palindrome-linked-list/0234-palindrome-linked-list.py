# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list=[]
        cur=head
        while cur is not None:
            list.append(cur.val)
            cur=cur.next
        l,r=0,len(list)-1
        while l<r and list[l]==list[r]:
            l+=1
            r-=1
        return l>=r
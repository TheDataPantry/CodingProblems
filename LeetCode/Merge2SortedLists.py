from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Instantiate an Empty ListNode class
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            # Evaluate if value in L1 is > value in L2 then add the lower value to the instanced ListNode above.
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
        # Last value capture after the loop above.
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next
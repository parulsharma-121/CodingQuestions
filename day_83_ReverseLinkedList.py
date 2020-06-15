'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

'''
def reverseList(head):
    if (head == None):
        return None
    else:
        slow = head
        fast = head.next
        newlist = None
        try:
            while slow:
                slow.next = newlist
                newlist = slow
                slow = fast
                fast = fast.next
        except:
            return newlist

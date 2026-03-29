# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # 创建一个哑节点作为新链表的起点
        dummy = ListNode()
        tail = dummy  # tail 用于指向新链表的最后一个节点

        # 合并链表
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # 如果有链表未完全遍历完，直接连接剩余部分
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # 返回新链表的头节点，即 dummy 的下一个节点
        return dummy.next
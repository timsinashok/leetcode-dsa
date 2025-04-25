"""
Edge cases:
Head == none


Solution: If node has children, explre chidlren first
Tehn go to the next
do dsf s put in stack
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(0)
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()
            
            # Link prev and curr
            prev.next = curr
            curr.prev = prev

            # Push next and child to stack (next last to be processed after child)
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # Clear child pointer

            prev = curr  # Advance prev

        # Detach dummy node
        dummy.next.prev = None
        return dummy.next
            
            

            
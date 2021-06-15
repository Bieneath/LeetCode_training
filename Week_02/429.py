class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        stack = [root]
        ret = []
        while stack:
            ret.append([node.val for node in stack])
            temp = []
            # for node in stack:
            #     for child in node.children:
            #         temp.append(child)
            # stack = temp
            stack = [child for node in stack for child in node.children]
        return ret
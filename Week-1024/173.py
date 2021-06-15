# 一次遍历法
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.data = [root]

    def next(self) -> int:
        while isinstance(self.data[-1], TreeNode):
            last = self.data.pop()
            if last.right: self.data.append(last.right)
            self.data.append(last.val)
            if last.left: self.data.append(last.left)
        return self.data.pop()

    def hasNext(self) -> bool:
        return self.data != []
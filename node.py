class Node:
    def __init__(self, name="", value=0, children=None):
        self.name = name
        self.value = value
        if children is None:
            children = []
        self.children = children

    def __str__(self):
        return "Node(name={name}, value={value}, children={children})".format(
            name = self.name, value = self.value, children = self.children)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getChild(self, index):
        return self.children[index];

    def getChildren(self):
        return self.children

    def getNumChildren(self):
        return len(self.children)

    def recursiveEquals(self, otherNode):
        if (not nodesCouldBeEqual(self, otherNode)):
            return False

        for i in range(self.getNumChildren()):
            if (not self.children[i].recursiveEquals(otherNode.getChild(i))):
                return False

        return True


    def iterativeEquals(self, otherNode):
        pass

    def __eq__(self, otherNode):
        return self.recursiveEquals(otherNode)


def nodesCouldBeEqual(n1, n2):
    if (n1.getName() != n2.getName()):
        return False

    if (n1.getValue() != n2.getValue()):
        return False

    if (n1.getNumChildren() != n2.getNumChildren()):
        return False

    return True

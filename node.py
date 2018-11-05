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

    def getChildren(self):
        return self.children

    def getNumChildren(self):
        return len(self.children)

    def recursiveEquals(self, otherNode):
        pass

    def iterativeEquals(self, otherNode):
        pass

    def __eq__(self, otherNode):
        return self.recursiveEquals(otherNode)

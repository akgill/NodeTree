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

    def getNumChildren(self):
        return len(self.children)

    def recursiveEquals(self, otherNode):
        if not nodesCouldBeEqual(self, otherNode):
            return False

        for i in range(self.getNumChildren()):
            if not self.children[i].recursiveEquals(otherNode.children[i]):
                return False

        return True


    def iterativeEquals(self, otherNode):
        if not nodesCouldBeEqual(self, otherNode):
            return False

        queue1 = self.children
        queue2 = otherNode.children
        while (len(queue1) > 0):
            new_queue1 = list()
            new_queue2 = list()
            for i in range(len(queue1)):
                if not nodesCouldBeEqual(queue1[i], queue2[i]):
                    return False

                new_queue1.extend(queue1[i].children)
                new_queue2.extend(queue2[i].children)

            queue1 = new_queue1
            queue2 = new_queue2

        return True

    def __eq__(self, otherNode):
        return self.recursiveEquals(otherNode)


def nodesCouldBeEqual(n1, n2):
    if (n1.name != n2.name):
        return False

    if (n1.value != n2.value):
        return False

    if (n1.getNumChildren() != n2.getNumChildren()):
        return False

    return True

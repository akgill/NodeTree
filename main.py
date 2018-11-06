from node import Node

def test(n1, n2, expected=""):
    print "expect: {expected}".format(expected=expected)
    print "iterative: ", n1.iterativeEquals(n2)
    print "recursive: ", n1.recursiveEquals(n2)


if __name__  == "__main__":
    n1 = Node("G", 5, [Node("1", 1, [Node("3", 3, [Node("4", 4)]), Node("5", 5)]), Node("2", 2)])
    n2 = Node("G", 5, [Node("1", 1, [Node("3", 3, [Node("4", 4)]), Node("5", 5)]), Node("2", 2)])
    test(n1, n2, True)

    n1 = Node("G", 5, [Node("1", 1, [Node("3", 3, [Node("5", 4)]), Node("5", 5)]), Node("2", 2)])
    n2 = Node("G", 5, [Node("1", 1, [Node("3", 3, [Node("4", 4)]), Node("5", 5)]), Node("2", 2)])
    test(n1, n2, False)

"""
Search Tree class, which contains the data of the backward search recursive matching on the FM-index
"""


class Node:

    def __init__(self, value, order, parent):
        self.value = value  # value of the string
        self.order = order  # order of the string
        self.parent = parent  # the parent Node

    def __repr__(self):
        return repr("Node: " + str(self.value) + str(self.order))


class SearchTree:
    latest_nodes = None

    def __init__(self, root):
        self.root = root  #a Node
        self.latest_nodes = [root]




    def new_iteration(self, new_nodes):
        self.latest_nodes.clear()
        self.latest_nodes = new_nodes



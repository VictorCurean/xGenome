"""
Search Tree class, which contains the data of the backward search recursive matching on the FM-index
"""


class Node:

    def __init__(self, value, rank ,first_position, parent):
        self.value = value                      # value of the string
        self.rank = rank                        # rank of the character in the bwt
        self.first_position = first_position    #absolute position of the character in the first list
        self.parent = parent                    # the parent Node

    def __repr__(self):
        return repr("Node: " + str(self.value) + str(self.rank) + " FIRST postition: " + str(self.first_position))


class SearchTree:
    latest_nodes = None

    def __init__(self, root):
        self.root = root  #a Node
        self.latest_nodes = [root]


    def new_iteration(self, new_nodes):
        self.latest_nodes.clear()
        self.latest_nodes = new_nodes



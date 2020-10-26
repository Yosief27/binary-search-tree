## Dictionary ADT ##
# Implemented with BS Tree
"""
Collection of key-value pair records, implemented as a binary search tree.
"""
# Name of class MUST be Dictionary


class Dictionary:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def getKey(self):
            return self.key  # Abstract method, add your own

        def getValue(self):
            return self.value  # Abstract method, add your own

        def get_value(self, key):
            if key < self.key and self.left is not None:
                return self.left.get(key)
            elif key > self.key and self.right is not None:
                return self.right.get(key)
            elif self.key == key:
                return self.value
            else:
                return None

        def insert(self, key, value):
            if key < self.key:
                if self.left is None:
                    self.left = Dictionary.Node(key, value)
                else:
                    self.left.insert(key, value)
            elif key > self.key:
                if self.right is None:
                    self.right = Dictionary.Node(key, value)
                    return True
                else:
                    self.right.insert(key, value)
                    return True
            else:
                return False

            pass   # Abstract method, add your own

        def get(self, key):
            if key < self.key and self.left is not None:
                return self.left.get(key)
            elif key > self.key and self.right is not None:
                return self.right.get(key)
            elif self.key == key:
                return self
            else:
                return None
              # Abstract method, add your own

        def minRightnode(self):
            if self.left is not None:
                return minRightnode(self.left)
            if self.left is None:
                return self

        def delete_child_node(self, key):

            if self.left is not None and self.left.key == key:
                self.left = None
                return True

            if self.right is not None and self.right.key == key:
                self.right = None
                return True
            else:
                if key < self.key:
                    return self.left.delete_child_node(key)
                elif key >= self.key:
                    return self.right.delete_child_node(key)

        def get_max_node(self):
            if self.right is None:
                return self
            else:
                return self.right.get_max_node()

        def get_min_node(self):
            if self.left is None:
                return self
            else:
                return self.left.get_min_node()

        def get_parent(self, key):
            if self.right is not None and self.right.key == key:
                return self
            elif self.left is not None and self.left.key == key:
                return self
            else:
                if key > self.key:
                    return self.right.get_parent(key)
                elif key < self.key:
                    return self.left.get_parent(key)

        def delete(self, key):
            if self.get(key) is None:
                return False
            else:
                delete_node = self.get(key)
                if delete_node.right is not None and delete_node.left is None:
                    par_node = self.get_parent(key)
                    if par_node.right.key == key:
                        par_node.right = delete_node.right
                    elif par_node.left.key == key:
                        par_node.left = delete_node.right

                    return True
                elif delete_node.left is not None and delete_node.right is None:
                    par_node = self.get_parent(key)
                    par_node.left = delete_node.left
                    return True

                # find the successor in the right sub tree
                # the smallest value next to the deleted node
                # check if it has a right child
                elif delete_node.right is not None and delete_node.left is not None:
                    min_node = delete_node.right.get_min_node()
                    delete_node.key = min_node.key
                    delete_node.value = min_node.value
                    if min_node.left is None and min_node.right is None:
                        if delete_node.right.key == min_node.key:
                            delete_node.right = None
                            return True
                        else:
                            return delete_node.right.delete_child_node(min_node.key)
                    elif min_node.right is not None:
                        return delete_node.right.delete(min_node.key)

                elif delete_node.right is None and delete_node.left is None:
                    return self.delete_child_node(key)

            # check if it is a root node and delete the node

            # if the key is root in a root node
            # if the key is not the root node and have no child

            # if the key is not the root node and  have a right or left child
            # if the key is  not the root node and have both the right and left child
            #
             # Abstract method, add your own

        def preorder(self):
            if self:
                print(self.key, self.value)
                if self.left:
                    self.left.preorder()
                if self.right:
                    self.right.preorder()

        def height(self):

            if self.left is None and self.right is None:
                return 0
            else:
                return max(1 + self.right.height() if self.right is not None else 0, 1 + self.left.height()if self.left is not None else 0)
        # print level node accepting level value in integer
        def levelNode(self, level):
            if level == 0:
                return (self.key, self.value)
            else:
                return(self.right.levelNode(level-1)if self.right is not None else None, self.left.levelNode(level-1)if self.left is not None else None)

            

        def __iter__(self):  # Should iterats over the Nodes in the tree
            # First, it yield itself
            yield (self.key, self.value)
            if self.nextNode is not None:
                x = self.nextNode  # If there is a follower
                for (k, v) in self.nextNode:     # we use the iterator in that node - sort of recursion
                    yield (k, v)

        def __str__(self):
            s = f" {self.key,self.value}"
            return s


# Dictionary methods start here:

    def __init__(self):
        self.__tree = None

    """
    Save key-value pair record. Returns 'True' if inserted and 'False' if key is already in the Dictionary
    """

    def insert(self, key, value):
        if self.__tree == None:
            self.__tree = Dictionary.Node(key, value)
            return True

        else:
            return self.__tree.insert(key, value)
          # Abstract method, add your own

    def height(self):
        if self.__tree.right is None and self.__tree.left is None:
            return 0
        else:
            # height_dic={'r':0,'l':0}
            return self.__tree.height()
   # level nodes print out
    """
    Returns value that is identified by `key`, or None if no such key exists.
    """

    def get(self, key):
        if self.__tree:
            node = self.__tree.get(key)
            if node is not None:
                return node
            else:
                return None
          # Abstract method, add your own

    def get_value(self, key):
        if self.__tree:
            node = self.__tree.get(key)
            if node is not None:
                return node.value
            else:
                return None
    """
    Delete key-value pair identified by `key` and returns 'True' if deleted, 'False' if not found in the Dictionary.
    """

    def delete(self, key):
        if self.__tree:
            return self.__tree.delete(key)
        else:
            return False

        pass   # Abstract method, add your own
    """
    traversaling  the binary tree 
    """

    def preorder(self):
        self.__tree.preorder()
    """
        Returns a gererator that could iterate over the tupel (key, value) objects (orderd by key, smallest to largest)
    """
      # level nodes print out

   def levelNode(self, level):
        if self.__tree is not None:
            if level == 0:
                return (self.__tree.key, self.__tree.value)
            else:
                return self.__tree.levelNode(level-1)
    def __iter__(self):
        if self.__tree is not None:
            # Necessary since None does not have an __iter__ method
            for node in self.__tree:   # Get values from the generator in the Node class
                yield node
    #     pass

    """ Returns a string representation of the key, values in the tree in order after key value (smallest to largest)
    """

    def __str__(self):
        s = "["
        if self.__tree is not None:
            for node in self.__tree:  # Note that we are using the generator
                s += f" {node},"
        return s + "]"


def main():
    d = Dictionary()

    d.insert(15, 'dawit')
    d.insert(8, 'goney')
    d.insert(6, 'bini')
    d.insert(12, 'sham')
    d.insert(25, 'welid')
    d.insert(20, 'abi')

    d.insert(30, 'mic')
    d.insert(27, 'Esaias')
    d.insert(35, 'midu')
    d.insert(28, 'sami')
    # d.insert(21,'Issac')
    # d.insert(6,'sami')
    # d.insert(5,'Issac')
    # d.insert(4,'josi')
    # d.insert(7,'wintu')
    # d.insert(18,'midu')
    # d.insert(21,'micu')

    d.preorder()
    print(d.delete(25))

    d.preorder()

    print(d.get_value(15))


if __name__ == '__main__':
    main()

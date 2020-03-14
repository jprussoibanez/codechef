from bst_operations.binarysearchtree import BinarySearchTree
import sys

def main(args = None):
    bst = BinarySearchTree()
    try:
        for _ in range(int(input())):
            input_line = input().split()
            
            command = str(input_line[0])
            value = int(input_line[1])
            
            if(command == 'i'):
                position = bst.insertNode(value)
            elif(command == 'd'):
                position = bst.deleteNode(value)
            if position >= 1:
                print(position)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
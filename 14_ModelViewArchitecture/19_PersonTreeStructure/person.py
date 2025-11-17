from typing import List, Optional


class Person:
    def __init__(self, data: list[str] = None, parent: 'Person' = None):

        self._column_fields = data or []
        self._parent = parent 
        self._children : list[Person] = []

    def append_child(self, child: 'Person'):
        self._children.append(child)

    def child(self, row: int) -> 'Person':
        if 0 <= row < len(self._children):
            return self._children[row]
        return None
    
    def child_count(self) -> int:
        return len(self._children)
    
    def data(self,column: int) -> str:
        if 0 <= column < len(self._column_fields):
            return self._column_fields[column]
        return ""
    
    def parent_person(self) -> 'Person':
        return self._parent
    
    def row(self) -> int:
        """
        Get the row of this person in its parent's children list
        
        :return: Row index or 0 if no parent
        """
        if self._parent:
            return self._parent._children.index(self)
        return 0
    
    def set_data(self, column: int, value: str) -> bool:
        if 0 <= column < len(self._column_fields):
            self._column_fields[column] = value
            return True
        return False
    
    def insert_children(self, position: int, count: int, columns: int) -> bool:
        if position < 0 or position > len(self._children):
            return False
        for _ in range(count):
            child = Person([""]*columns, self)
            self._children.insert(position, child)
        return True
    
    def remove_children(self, position: int, count: int) -> bool:
        if position < 0 or position + count > len(self._children):
            return False
        del self._children[position:position + count]
        return True
    

    def print_tree(self, indent: int = 0):
        """
        Recursively print information about this person and their descendants
        
        :param indent: Indentation level for printing
        """
        print('  ' * indent + f"{' | '.join(self._column_fields)} - {self.child_count()} children")
        for child in self._children:
            child.print_tree(indent + 1)   


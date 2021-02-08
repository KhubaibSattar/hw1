class MyListIterator:
    ''' Iterator class to make MyList iterable.
    https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
    '''

    def __init__(self, lst):
        # MyList object reference
        self._lst: MyList = lst
        # member variable to keep track of current index
        self._index: int = 0

    

    def __next__(self):
        ''''Returns the next value from the stored MyList instance.'''
        if self._index < len(self._lst):
            value = self._lst[self._index]
            self._index += 1
            return value
        
        # End of Iteration
        raise StopIteration


class MyList:
    '''A list interface.'''

    def __init__(self, lst, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.
        The list is static. It only has space for size elements.
        Args:
        - size: size of the list; space is reserved for these many elements.
        - value: the optional initial VALUE of the created elements.
        Returns:
        none
        """
        self.lst = lst
        self.size = size
        if len(lst) <= size:
            return True
        else:
            return False


        # pass

    def __len__(self, lst) -> int:
        '''Returns the size of the list. Allows len() to be called on it.
        Ref: https://stackoverflow.com/q/7642434/1382487
        Args:
        Returns:
        the size of the list.'''
        total_el = lst
        return len(total_el)

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487
        Args:
        - i: the index from which to retrieve the value.
        Returns:
        the value at index i.
        '''
        
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
            return self[i]
        # pass

    def __setitem__(self, lst, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487
        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set
        Returns:
        none
        '''
        # Ensure bounds.
        assert 0 <= i < len(self),\
            f'Setting invalid list index {i} in list of size {len(self)}'
            value = self.lst[i] 
        # pass

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.
        Ref: https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
        Args:
        Returns:
        an iterator that allows iteration over this list.
        '''
        for i in self:
            return i
        return MyListIterator(self)

    def get(self, i: int):
        '''Returns the value at index, i.
        Alternate to use of indexing syntax.
        Args:
        - i: the index from which to retrieve the value.
        Returns:
        the value at index i.
        '''
        return self[i]

    def set(self, i: int, value) -> None:
        '''Sets the element at index, i, to value.
        Alternate to use of indexing syntax.
        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set
        Returns:
        none
        '''
        self[i] = value


class ArrayList(MyList):
    def __init__(self,lst ,size: int, value=None):
        super().__init__(size: int, value=None)    
    
    def __len__(self):
        super().__len__(size: int, value = None)

    def __getitem__(self, i: int):

    def __setitem__(self, i: int, value):
    
    def __iter__(self):
    
    def get(self, i: int):
    
    def set(self, i: int, value):
    
    
    # pass


class PointerList(MyList):
    pass 

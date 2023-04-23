from functools import reduce

class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        
        try:
            for i, x in enumerate(self.list_of_lists):
                while isinstance(x, list):    
                    self.list_of_lists[i:i+1] = x
                    x = self.list_of_lists[i]
        except IndexError:
            pass

        self.number_of_elements = len (self.list_of_lists)
              

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= self.number_of_elements:
            raise StopIteration
        item = self.list_of_lists[self.counter]
        self.counter += 1
             
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    my_test_list = [
        [],
        [1, 2, 3, 4],
        []
    ]

    for i in FlatIterator(my_test_list):
        print(i, end =',')

    test_3()
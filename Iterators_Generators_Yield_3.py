from functools import reduce

class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.list_elements = [len(x) for x in list_of_lists]
        self.number_of_elements = reduce(lambda x,y: x+y, self.list_elements, 0)
              

    def __iter__(self):
        self.counter = 0
        self.current_list = 0
        self.current_element = 0
        return self

    def __next__(self):
        if self.counter >= self.number_of_elements:
            raise StopIteration
        if self.list_elements[self.current_list] == 0:
            self.current_element = 0
            self.current_list += 1
            item = ''
        else:
            item = self.list_of_lists[self.current_list][self.current_element]
            self.current_element += 1
            self.counter += 1
            if self.current_element >= self.list_elements[self.current_list]:
                self.current_element = 0
                self.current_list += 1
            
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    


    my_test_list = [
        [],
        [],
        [1, 2]
    ]

    for i in FlatIterator(my_test_list):
        print(i, end =',')
     
    test_1()

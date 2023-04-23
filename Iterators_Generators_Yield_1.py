
class FlatIterator:

    def __init__(self, list_of_lists):
        self.flatten_list = [item for sublist in list_of_lists for item in sublist]
        self.number_of_elements = len(self.flatten_list)
                

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= self.number_of_elements:
            raise StopIteration
        item = self.flatten_list[self.counter]
        self.counter += 1
             
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
        [1,2,3,'a'],
        []
    ]

    for i in FlatIterator(my_test_list):
        print(i, end =',')
     
    test_1()
    

    
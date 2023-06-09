import types


def flat_generator(list_of_lists):
    flat_list = [item for sublist in list_of_lists for item in sublist]

    for item in flat_list:
        yield item
    


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':

    my_test_list = [
        [],
        [1,2,3,'a'],
        []
    ]

    for i in flat_generator(my_test_list):
        print(i, end =',')

    test_2()

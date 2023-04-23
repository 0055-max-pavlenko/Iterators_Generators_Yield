import types


def flat_generator(list_of_lists):
    try:
        for i, x in enumerate(list_of_lists):
            while isinstance(x, list):    
                list_of_lists[i:i+1] = x
                x = list_of_lists[i]
    except IndexError:
        pass

    for item in list_of_lists:
        yield item
 
 


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

    my_test_list = [
        [],
        [1,2,3,'h'],
        []
    ]

    for i in flat_generator(my_test_list):
        print(i, end =',')

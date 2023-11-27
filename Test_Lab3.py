import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])
def test_more_10():
    result=1
    input_arr=[1,2,3243,645453,35,53,35,46,2354,35,53,3]
    actual=Lab3.bubble_sort(input_arr,3)
    assert (actual==1)
def test_0():
    result=0
    input_arr=[]
    actual=Lab3.bubble_sort(input_arr,3)
    assert (actual==0)

def test_not_numbers():
    input_arr=["a","b","c",1,2]
    actual=Lab3.bubble_sort(input_arr,3)
    assert actual==2


from index import add

def test_add():
    assert add(1,2) == 3
    assert add(1, "asdf") == "Invalid Input"

    # assert add(1,"abc") == "Invalid Input"

from Notes.class_notes import Animal

def test_get_name():
    testanimal = Animal("bob", "bobcat", 22, "male", "legendary")
    name = testanimal.get_name()
    assert name == "bob"

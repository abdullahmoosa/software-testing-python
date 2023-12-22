from student_db import StudentDB
import pytest

# # This is not a good approach because we have to initialize the database multiple times
# def test_scott_data():
#     db = StudentDB()
#     db.connect('data.json')
#     scott_data = db.get_data('Scott')

#     assert scott_data['id'] == 1
#     assert scott_data['name'] == 'Scott'
#     assert scott_data['result'] == 'pass'

# def test_mark_data():
#     db = StudentDB()
#     db.connect('data.json')
#     mark_data = db.get_data('Mark')

#     assert mark_data['id'] == 2
#     assert mark_data['name'] == 'Mark'
#     assert mark_data['result'] == 'fail'

# To solve the above issue, we can use the 'setup module' to initialize the database single time at first.
db = None
def setup_module(module):
    print('----setup----')
    global db
    db = StudentDB()
    db.connect('data.json')

def teardown_module(module):
    print('----teardown----')
    db.close()

def test_scott_data():
    scott_data = db.get_data('Scott')

    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data():
    mark_data = db.get_data('Mark')

    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
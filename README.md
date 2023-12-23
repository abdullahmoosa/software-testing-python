## Software Testing

Software Testing is essential for developing the final product. It is essential to understand whether the final product is the "right one" or "the product is working right".

"Right one" means whether the product satisfies the customer requirement.

"The product working right" means whether the product is working correctly without any bugs.
Two types of testing 
- Functional Testing 
- Non-Functional Testing

![image](https://github.com/abdullahmoosa/software-testing-python/assets/67234038/64c0c819-b534-4354-b122-cb33dd537e6b)

Unit Testing is used to check if each class of the codebase is working. 
Integration Testing is used to check if the software as a whole is working as intended.
System testing is used to check if the overall software is working without any issues after deployment.
Acceptance Testing is used to check if the final product matches with the customer requirement.


**As a software developer, it is essential to design the "unit tests" to check if each class is working properly.**

**Functional Testing : ** Testing the codebase of the software. whether each class,function work as expected. Fixing code related bugs.
**Non-Functional Testing** : Testing the performance(response time , scalability, load-balancing etc)
pytest is a python module for executing test-files for python project.
pytest documentation : [https://docs.pytest.org/en/7.1.x/contents.html]()

For installing pytest run the following command : 
```
pip install -U pytest
```
After installation, you can type the following command to get to know about the available pytest features :
```
pytest -h
```

**You may follow the project [sample_test](sample_test) for understanding the below codes better.**
- For executing all the tests you can type py.test inside cmd when you are in the same directory as the test files.:
```
py.test
```
- For executing a specific test file you can type pytest 'test_file_name'
```
pytest test_math_func.py
```
- For executing a specific method inside a specific file you can type pytest test_file_name::function_name
```
pytest test_main_func.py::test_add
```
- For executing a test file with more explanation to each test function you can add 'v' flag after the code.
```
pytest test_main_func.py -v
```
- Suppose, you have multiple test functions with a specific keyword in the function name. You want to execute those functions which match the keyword. For that you can use 'k' flag.
```
pytest -v -k 'add'
```
The above function will execute all the functions from all the test-files that has the keyword 'add' in their name.
- You can also integrate 'add', 'or' keywords with 'k' flag to execute functions containing multiple keywords.
```
pytest -k "add or string"
```
This will execute the functions containing either "add" or "string" keywords or both.
- You can add "markers" for your python test functions. Markers are decorators which can be used to identify similar test functions to run only those.

**You may follow the project [pytest_with_options](pytest_with_options) for better understanding**

```
import pytest
@pytest.mark.number

def test_add():

    assert math_func.add(7,3) == 10

    assert math_func.add(7) == 9

@pytest.mark.number

def test_product():

    assert math_func.product(5,5) == 25

    assert math_func.product(5) == 10
```
In the above code, we have added 'number' marker to the two functions because these are for designed for testing 'numbers'.
We can execute these tests from command line using 'm' flag.
```
pytest -m number
```
- You can skip a particular test using a 'skip' marker.
```
import pytest
@pytest.mark.skip(reason="Do not run number add test")
def test_add():

    assert math_func.add(7,3) == 10

    assert math_func.add(7) == 9

@pytest.mark.number

def test_product():

    assert math_func.product(5,5) == 25

    assert math_func.product(5) == 10
```
When you execute from cmd :
```
pytest -v
```

![image](https://github.com/abdullahmoosa/software-testing-python/assets/67234038/fcf1aa5e-e958-4c9c-89bf-6d61a374c165)

You can see the add function is skipped with the reason printed.
- You can use 'skipif' marker to check for a certain condition when executing the test functions.
```
@pytest.mark.skipif(sys.version_info < (3,12),reason="Unsupported Python version")

@pytest.mark.number

def test_product():

    assert math_func.product(5,5) == 25

    assert math_func.product(5) == 10
```
This code will skip the test_product function is the python version is less than 3.12.
![image](https://github.com/abdullahmoosa/software-testing-python/assets/67234038/cbc2cd97-5fe9-491d-b7e9-0dde0b04ead6)
- In general, when executing the test functions, pytest does not print any statements even if it is inside the function.
```
def test_add():

    assert math_func.add(7,3) == 10

    assert math_func.add(7) == 9

    print("---Execution Successful---")
```
To print the statement, we can use 's' flag.
```
pytest -s -v
```
![image](https://github.com/abdullahmoosa/software-testing-python/assets/67234038/3b9b1e00-9f75-4019-8f71-f5355595db5a)
- To execute the tests in quiet mode(Without any extra details) we can use the 'q' flag.
```
pytest -q
```
![image](https://github.com/abdullahmoosa/software-testing-python/assets/67234038/1aecc11d-dbe5-4236-aa96-be0dcc74b764)
We can see no extra details have been printed.

### Adding parametrize decorator:
Follow [pytest_parameterizing](pytest_parameterizing) codebase for understanding below
There may be situations when you are testing the same function but for different data types and values. Example can be : 
```
def test_add():

    assert math_func.add(7,3) == 10

    assert math_func.add(7) == 9

    print("---Execution Successful---")

@pytest.mark.skipif(sys.version_info < (3,12),reason="Unsupported Python version")

@pytest.mark.strings

def test_add_strings():

    result = math_func.add('Hello ', 'world')

  

    assert result == 'Hello world'

    assert type(result) is str

    assert 'Heldio' not in result
```
Here we are testing the 'add' functionality once with one function for testing numbers and another function for testing string. We can reduce this hassle by using the marker "parametrize" decorator.
We can refactor the code like this :
```
import pytest

import math_func

@pytest.mark.parametrize('num1,num2,result',

                         [(7,3,10),

                          ('Hello',' world', 'Hello world'),

                          (3.5,4.5,8)])

def test_add(num1,num2,result):

    assert math_func.add(num1,num2) == result
```
Here, the 'parametrize' marker accepts two arguments. First argument is a string where the values are separated by ','. The first two values are the inputs to 'add' functionality and the 'result' is used to check if the functionality works correctly or not.
The second argument is a list of tuple which is iterated over and in each iteration each tuple is passed as an input to the 'test_add' function.
The main advantage using parametrizing is we can reduce clusters of code and make code more efficient.


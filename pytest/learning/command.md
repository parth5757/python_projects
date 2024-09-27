# pytest notes and command

to run all test file in current working directory we hvae to run the following command

-    notes everyfunction which have to run test that must be start with the "tets_" ex: test_function.py

```shell
pytest
```

- pytest command to run an single file only

```shell
pytest test_function.py
```

- to test an particular function name we want test with following command by adding there function namw.

```shell
pytest tets_function.py::test_cube
```

- if we want to test any number of word(sub string) name function which will be avilable in our file then we can use folwing command

- It will automatically select match name and test that function
```shell
pytest test_function.py -k cube
```


<!-- Now Test classes journey -->

- if we want to do an group of class of multiple function at that time we can also use pytest

- to run all testclass we use following command
```
pytest --collectonly
```

- same as for particular file we use following command
```shell
pytest test_class.py (pytest filename)
```

- To run particular test class we use this command
```shell
pytest test_class.py::TestClass
```


Skipping Tests

there are lot of test when we want to skip some test at that time we use skipping test function

test_skip_0.py
- it show example how skip test

test_skip_1.py
- in this show example of TestClass 

test_skip_2.py
- it show the example where without using the pytest decorater we can use pytest

test_skip_3.py
- it add reason the why we added to skip the test.

'''shell
pytest test_skip_3.py -rs
'''
this command use get reason in terminal

test_skip_4.py
- it is use for adding version specification when we want any function must be test with an particular version 
'''shell
pytest test_skip_3.py -rs
'''
this command use get reason and version info in terminal

test_skip_5.py
- it is use to skip any module import in file

XFail test

XFail: mark test functions as expected to fail

- You can use the xfail marker to indicate that you expect a test to fail:
read for more 
https://docs.pytest.org/en/stable/how-to/skipping.html#










# fixture learning from unit  testing example

- In testing, a fixture provides a defined , reliable and consistent context for the tests.


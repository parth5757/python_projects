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






<h2>Skipping Tests</h2>

there are lot of test when we want to skip some test at that time we use skipping test function

test_skip_0.py  [code](pytest_skip/test_skip_0.py)
- it show example how skip test

test_skip_1.py  [code](pytest_skip/test_skip_1.py)
- in this show example of TestClass 

test_skip_2.py  [code](pytest_skip/test_skip_2.py)
- it show the example where without using the pytest decorater we can use pytest

test_skip_3.py  [code](pytest_skip/test_skip_3.py)
- it add reason the why we added to skip the test.

```shell
pytest test_skip_3.py -rs
```
this command use get reason in terminal

test_skip_4.py  [code](pytest_skip/test_skip_4.py)
- it is use for adding version specification when we want any function must be test with an particular version 
'''shell
pytest test_skip_3.py -rs
'''
this command use get reason and version info in terminal

test_skip_5.py [code](pytest_skip/test_skip_5.py)
- it is use to skip any module import in file

<h2>xFail test</h2>

XFail: mark test functions as expected to fail

- You can use the xfail marker to indicate that you expect a test to fail

- to read for more [click here](https://docs.pytest.org/en/stable/how-to/skipping.html#)


<h2>Parametrize</h2> 

-   It use for multiple parameter are use to test the any function.

```shell
pytest --collectonly test_parametrize_0.py
```
read for more [click here](https://docs.pytest.org/en/6.2.x/parametrize.html)


test_parametrize_0.py [code](parametrize/test_parametrize_0.py)
- it shows the single function multiple parameter with only input.

test_parametrize_1.py   [code](parametrize/test_parametrize_1.py)

- it shows the input with excepted output parametrize test


test_parametrize_2.py   [code](parametrize/test_parametrize_2.py)

- In this example we show how we can take pair of multiple input with expectation 

test_parametrize_3.py   [code](parametrize/test_parametrize_3.py)
-   ``` pytest.param(3, marks=pytest.mark.skip ```
    this thing use in skipping any particular in given test parameters

(Note: in this if you have use ```pytest``` & ```pytest test_parametrize_3.py``` command to run then it regularly see as skip test but not in collectonly command ```pytest --collectonly test_parametrize_3.py```)


test_parametrize_4.py   [code](parametrize/test_parametrize_4.py)

-  nothing new just add id of each parameter shown in example. 

-   want to execute the specific id test then only use then use following command
```
pytest --collectonly test_parametrize_4.py -k id_of_test_parameter
```
else 
other command like
```pytest```, ```pytest test_parametrize_4.py```, ```pytest --collectonly test_parametrize_4.py```

<h2>fixture testing example</h2>

[Documentation](https://docs.pytest.org/en/4.6.x/fixture.html#:~:text=fixtures%20have%20explicit%20names%20and%20are%20activated%20by%20declaring)

- It initialize the test function with give value.
- pytest fixture is provide adding initial value in separate value in pytest this thing make now require to add pytest parameters.

- In testing, a fixture provides a defined , reliable and consistent context for the tests.

test_fixture_0.py [code](fixtures/test_fixture_0.py)

- in this simple fixture value been initialize. and without adding any pytest decorator we can easily test the function.
way of executing ```pytest test_fixture_0.py```, ```pytest --collectonly test_fixture_0.py``` & last one is that the fixture where we see all fixture detail for initialization
```pytest --fixtures test_fixture_0.py```.

test_fixture_1.py [code](fixtures/test_fixture_1.py)

- to add log message while testing. run using ```pytest test_fixture_1.py -s``` command.


test_fixture_2.py [code](fixtures/test_fixture_2.py)
- It use to combine test multiple function once using scope module or function.
- If you change it to function then it separately initialize sane value for function.


<h2>pytest fixture conftest file</h2>
- It is an file provided with already added configuration for pytest fixture don't even 

test_conftest_0.py [code](conftest/test_conftest_0.py)

- In this code the how initialize fixture with conftest is shown

test_conftest_1.py [code](conftest/test_conftest_1.py)

- It show how to give message while testing any function.

test_conftest_2.py [code](conftest/test_conftest_2.py)
- In that it made for parent and current directory diffence understand in file directory there is an conftest.py file then it directly use that directory file not parent directory.

(Note: here no parent current directory made if you want to show example)


## forwarding_parameter_fixture [code](forwarding_parameter_fixture/test_param_forwarding_fixtures_0.py)

- is use for same time parameter forward from conftest perform fixture initialize value.

please check the code fpr more information.

## indirect_parameterization

https://docs.pytest.org/en/7.1.x/example/parametrize.html#indirect-parametrization

read this doc example (here written example are is not working)


## yield fixture [code](Yield_fixtures/test_yield_fixtures.py)

yield fixture are generate initial value and to give the result when we use that value (here when we are use result variable to print the values)

Run command 
```bash test_yield_fixtures.py ```


## pytest addoption [code]

- pytest addoption not running check documentation to know about.

```bash 
pytest test_name.py -s --name=Parth 
```

## pytest Dynamic parameterization

- It is use for sending multiple different parameter from pytest fixture conftest file.


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


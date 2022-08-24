# Writing our first test

## Post

- Any post has 2 attributes: title and content

## Blog

- Any blog has 3 attributes: title, author, and posts

---

- In general, each test suit is a class

- A test is a method in the test suite class

- Run python unittest class

```bash
# -m means module
# -v means verbose
python -m unittest -v <test_file_or_test_files_selector>
python -m unittest -v <test_file_and_maybe_test_files_selector>.ClassName
```

- TDD is a fancy name for 'think what you are about to implement before do it

# Kinds of tests

- Unit tests

```
Test things in a isolated way
May test just one funciton or just one method
```

- Integration tests

```
Test things together
May test a bunch of methods together
May test a whole class
May test a bunch of functions at once
```

# Mock

## Patch

- <a href="https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch" Documentation>

- To change output of some class, method or function

- To check the last call output of some class, method or function

- There is <code><mock_obj>.assert_called_once_with</code>

- This check if the mock object is called just one time

- This check the output, too

```python
# Check the last output of print function

from unittest.mock import patch

# If patch() is used as a context manager
# the created mock is returned by the context manager.

with patch('builtins.print') as mocked_print:

	print('hi')

	# last call and last output
	mocked_print.assert_called_with('hi')

	# one call and its output
	mocked_print.assert_called_once_with('hi')
```
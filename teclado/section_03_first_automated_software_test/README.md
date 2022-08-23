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

- TDD is a fancy name for 'think what you are about to implement before do it'
source ../venv-teclado/bin/activate

# https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure

# Discover run tests in any folder
# -> way 01
# all test*.py files
# python -m unittest discover

# -> way 02
# specifying a folder (-s)
# specifying a pattern (-p)
# python -m unittest discover -s tests -p '*test*'

# -> way 03
# specifying only the pattern
python -m unittest discover -p '*test*.py'



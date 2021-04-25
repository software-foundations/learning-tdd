from typing import List, Union, Tuple, Dict, Any, NewType, Callable

# -> Primitives
number: int = 10
floatibng: float = 3.4
boolean: bool = False
string: str = ''

# -> Sequencies
my_list: List[int] = [1, 2, 3]
lis_str_int: List[Union[int, str]] = [1, 2, 'Bruno']
my_tuple: tuple = (1, 2, 3)
my_tuple_2: Tuple = (1, 2, 3)
my_tuple_3: Tuple = (1, 2, 'asdf')
my_tuple_4: Tuple[int, int, str] = (1, 2, 'asdf')

# -> Dictionaries and sets
person_1: Dict[str, str] = {'name': 'Bruno', 'last_name': 'Conde', 'age': '24'}
person_2: Dict[str, Union[str, int]] = {'name': 'Bruno', 'last_name': 'Conde', 'age': 24}
person_3: Dict[str, Union[str, int, List[int]]] = {'name': 'Bruno', 'last_name': 'Conde', 'age': 24, 'l': [1, 2]}
person_4: Dict[str, Any] = {'name': 'Bruno', 'last_name': 'Conde', 'age': 24}

# -> Creating Alias for a Type
MyDict = Dict[str, Union[str, int, List[int]]]
person_5: MyDict = {'name': 'Bruno', 'last_name': 'Conde', 'age': 24, 'l': [1, 2]}

# -> Creating new Type
UserId = NewType('UserId', int)
user_id_1 = UserId(4893421)
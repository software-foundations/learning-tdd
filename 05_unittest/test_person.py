"""
class Person
    __init__
        name str
        last_name str
        data_obtained bool (initalizate False)

    API:
        get_all_data -> method
            OK
            404

            if OK, Person.data_obtained = True
"""

import unittest
from unittest.mock import patch
from person import Person
class TestPerson(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('Bruno', 'Conde')
        self.p2 = Person('Amy', 'Martin')

    ####################
    # Parameter Checking
    ####################
    
    # -> Person.name    
    def test_person_attr_name_have_correct_value(self):
        self.assertEqual(
            first=self.p1.name,
            second='Bruno',
            msg='Person obj has no attr name or it does not match'
            )
        self.assertEqual(
            first=self.p2.name,
            second='Amy',
            msg='Person obj has no attr name or it does not match'
        )

    def test_person_attr_name_is_str(self):
        self.assertIsInstance(
            obj=self.p1.name,
            cls=str,
            msg=f"Person.name should be <class 'str'> instead of '{type(self.p1.name)}'"
        )
        self.assertIsInstance(
            obj=self.p2.name,
            cls=str,
            msg=f"Person.name should be <class 'str'> instead of '{type(self.p1.name)}'"
        )

    # -> Person.last_name
    def test_person_attr_last_name_have_correct_value(self):
        self.assertEqual(
            first=self.p1.last_name,
            second='Conde',
            msg='Person obj has no attr last_name or it does not match'
        )
        self.assertEqual(
            first=self.p2.last_name,
            second='Martin',
            msg='Person obj has no attr last_name or it does not match'
        )

    def test_person_attr_last_name_is_str(self):
        self.assertIsInstance(
            obj=self.p1.last_name,
            cls=str,
            msg=f"Person.last_name should be <class 'str'> instead of '{type(self.p1.name)}'"
        )
        self.assertIsInstance(
            obj=self.p2.last_name,
            cls=str,
            msg=f"Person.last_name should be <class 'str'> instead of '{type(self.p1.name)}'"
        )

    # -> Person.data_obtained
    def test_person_attr_data_obtained_initializate_False(self):
        self.assertFalse(
            expr=self.p1.data_obtained,
            msg='Person obj has no attr dat_obtained or it is not False by its initialization'
        )
        self.assertFalse(
            expr=self.p2.data_obtained,
            msg='Person obj has no attr dat_obtained or it is not False by its initialization'
        )

    ##################
    # Method Checking
    ##################

    # -> Person.get_all_data()
    def test_method_get_all_data_response_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(
                first=self.p1.get_all_data(),
                second='CONECTED',
                msg="Not connected sucessfully"
            )            
            self.assertTrue(
                expr=self.p1.data_obtained,
                msg="p1.data_obtained should be setted to True when CONECTED"
            )
            
            self.assertEqual(
                first=self.p2.get_all_data(),
                second='CONECTED',
                msg="Not connected sucessfully"
            )            
            self.assertTrue(
                expr=self.p2.data_obtained,
                msg="p2.data_obtained should be setted to True when CONECTED"
            )

    def test_method_get_all_data_response_ERROR_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(
                first=self.p1.get_all_data(),
                second='ERROR 404',
                msg="response is not 'ERROR 404' while trying to connect"
            )
            self.assertFalse(
                expr=self.p1.data_obtained,
                msg="p1.data_obtained should be setted to False when ERROR 404"
            )

            self.assertEqual(
                first=self.p2.get_all_data(),
                second='ERROR 404',
                msg="response is not 'ERROR 404' while trying to connect"
            )
            self.assertFalse(
                expr=self.p2.data_obtained,
                msg="p2.data_obtained should be setted to False when ERROR 404"
            )

    def test_method_get_all_data_response_OK_and_ERROR_404_in_sequence(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(
                first=self.p1.get_all_data(),
                second='CONECTED'                
            )
            self.assertTrue(
                expr=self.p1.data_obtained,
                msg="p1.data_obtained should be setted to True when CONECTED"
            )
            self.assertEqual(
                first=self.p2.get_all_data(),
                second='CONECTED'                
            )
            self.assertTrue(
                expr=self.p2.data_obtained,
                msg="p2.data_obtained should be setted to True when CONECTED"
            )

            fake_request.return_value.ok = False
            self.assertEqual(
                first=self.p1.get_all_data(),
                second='ERROR 404'                
            )
            self.assertFalse(
                expr=self.p1.data_obtained,
                msg="p1.data_obtained should be setted to False when ERROR 404"
            )
            self.assertEqual(
                first=self.p2.get_all_data(),
                second='ERROR 404'                
            )
            self.assertFalse(
                expr=self.p2.data_obtained,
                msg="p2.data_obtained should be setted to False when ERROR 404"
            )


if __name__ == '__main__':
    unittest.main(verbosity=2)

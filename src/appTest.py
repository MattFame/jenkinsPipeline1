import unittest
from app import insert_mock_name


class Test(unittest.TestCase):
    
    def test_insert(self):
        inserted_person = insert_mock_name("jason",5)
        self.assertEqual(inserted_person, 'Person Jason added to Phonebook successfully')

if __name__ == '__main__':
    unittest.main()
import unittest
import app


class Test(unittest.TestCase):
    
    def test_insert(self):
        inserted_person = app.insert_mock_name("jason",5559990101)
        self.assertEqual(inserted_person, 'Person Jason added to Phonebook successfully')
    
    def test_insert_person(self):
        inserted_person = app.insert_person("jason",5559990101)
        self.assertEqual(inserted_person, 'Person Jason added to Phonebook successfully')
    
    def test_update_person(self):
        updated_person = app.update_person("jason",5559990102)
        self.assertEqual(updated_person, 'Phone record of Jason is updated successfully')

if __name__ == '__main__':
    unittest.main()
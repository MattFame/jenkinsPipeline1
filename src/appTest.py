import unittest
import app


class Test(unittest.TestCase):
    
    def test_insert(self):
        
        inserted_person = app.insert_person("jason",5)
        self.assertEqual(inserted_person, "Person Jason added to Phonebook successfully")

if __name__ == '__main__':
    unittest.main()
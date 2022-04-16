import unittest
import main
class TestMain(unittest.TestCase):
    def test_Alist(self):
        self.assertEqual(main.Alist(['ABCDEFGHIJKLMNOPQRST']),{'ABCDEFGHIJKLMNOPQRST': {'type': 'str', 'tag': '', 'description': '', 'required': False}} )
    def test_Schema(self):
        self.assertEqual(main.Schema('ABCDEFGHIJKLMNOPQRSTUVWXY', "str"),{'type': 'str', 'tag': '', 'description': '', 'required': False} )
    def test_CreateDict(self):
        data = {'id': 'ABCDEFGHIJKLMN', 'nickname': 'ABCDEFGHIJKLMN', 'title': 'ABCDEFGHIJK', 'accountType': 'ABCDEFGHIJKLMNOPQRSTUVWX', 'countryCode': 'ABCDEFGH', 'orientation': 'ABCDEFGHIJKLMNOPQRSTUVWXY'}
        result = {'id': {'type': 'str', 'tag': '', 'description': '', 'required': False}, 'nickname': {'type': 'str', 'tag': '', 'description': '', 'required': False}, 'title': {'type': 'str', 'tag': '', 'description': '', 'required': False}, 'accountType': {'type': 'str', 'tag': '', 'description': '', 'required': False}, 'countryCode': {'type': 'str', 'tag': '', 'description': '', 'required': False}, 'orientation': {'type': 'str', 'tag': '', 'description': '', 'required': False}}
        self.assertEqual(main.CreateDict(data), result)
        
    
if __name__ == '__main__':
   unittest.main()
   

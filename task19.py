#task1

import pytest
import unittest

class OpenFile():
    counter = 0
    def __enter__(self):
        OpenFile.counter += 1
        print('Hello , im going to help you with this file')
        return self.file.read()
    def __init__(self, filename, mode,*args,**kwargs):
        self.file = open(filename, mode,*args,**kwargs)
    def __exit__(self, type, value, traceback):
        self.file.close()
        print(f'My work is done {self.counter} times')

x = 0
while x != 4:
 with OpenFile('text', 'r') as res:
   print(res)
 x +=1
#task2

class TestOpenFile(unittest.TestCase):
    counter = 0
    filename = 'task11.py'
    mode = 'r'
    file = open(filename, mode)
    def __enter__(self):
        TestOpenFile.counter += 1
        print('Hello , im going to help you with this file')
        return self.file.read()
    def __exit__(self, type, value, traceback):
        self.file.close()
        print(f'My work is done {self.counter} times')
    def test_context(self):
        self.assertEqual(type(self.filename),str)
        self.assertTrue(self.counter != 0)
        self.assertEqual(len(self.mode), 1)


with TestOpenFile() as res:
    print('test')
if __name__ == '__main__':

 unittest.main()

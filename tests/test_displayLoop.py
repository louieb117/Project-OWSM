import sys
sys.path.insert(1, '/home/lbello/Code/Project_OWSM/Project-OWSM/app')      # Moves path to method to be tested.
from interdimensional_story_reader import interdimensional_story_reader
import aiounittest
import asyncio
import keyboard
import random

class Test(aiounittest.AsyncTestCase):

    def test_typing_sim(self):
        #Qustion, does a slower output equal a fast output?
        t1 = interdimensional_story_reader('TestFile.txt')
        output_sim = t1.typing_sim(t1.Story_file)
        output_test = 'This is text in a file.\n'
        print(type(output_sim))
        self.assertEqual(output_sim , output_test)
        # AssertionError:
        # <coroutine object interdimensional_story_reader.typing_sim at 0x7fcec8ac1ec0> != 'This is text in a file.\n'

if __name__ == '__main__':
    #asyncio.run(main())
    unittest.main()

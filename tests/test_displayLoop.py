import sys
sys.path.insert(0, '~/Code/Project_OWSM/Project_OWSM/app')      # Moves path to method to be tested.
import interdimensional_story_readers
import aiounittest
import asyncio
import keyboard
import random

    def setup():
        t1 = interdimensional_story_reader('TestFile.txt')

class Test(aiounittest.AsyncTestCase):

    def test_typing_sim():
        setup()
        #Qustion, does a slower output equal a fast output?
        output_sim = t1.typing_sim(t1.Story_file)
        output_test = 'This is text in a file.\n'
        self.assertEqual(output_sim , output)


if __name__ == '__main__':
    #asyncio.run(main())
    unittest.main()

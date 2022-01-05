import unittest
from slowprint.slowprint import *
import asyncio
import aioconsole

class output_test(unittest.TestCase):

    def test_file_read(self):
        with open("TestFile.txt","r") as test_object:
            self.assertEqual(test_object.read(),'This is text in a file.\n')
            test_object.close()

    def test_async_func(self):
        async def interupter(self):
            stdin = await aioconsole.get_standard_streams()
            for command in stdin:
                if command == '^[' or '\n':
                    sim_input = await aioconsole.ainput('^[')

            self.exceptedFailure(sim_input,'^[')

    def test_async_input(self):
        async def ainput(string: str) -> str:
            await asyncio.get_event_loop().run_in_executor(None, lambda s=string: sys.stdout.write(s+' '))
            self.stream = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
            self.assertEqual(self.stream,'\n','Hello')

    def teardown(self):
        print('Hello')
        print(self.stream)


if __name__ == '__main__':
    unittest.main()

import aiounittest
import asyncio
import keyboard

    def slowPrint(string):
    for char in range(len(string)):
        print(string[char], end="")
        #time.sleep(x) can be used for a longer wait but is not needed...
        #for a noticable reduction in output speed
    print("")


    asyncio def machine_loop():
        test_object = open("TestFile.txt","r")
        for


    asyncio def pause_loop():
        await keyboard.wait('esc')
        print('\n\n\t\tPaused\n\n\tEnter esc again to exit the program: ')
        keyboard.wait('esc')





class Test(aiounittest.AsyncTestCase):



    asyncio def main():
        task1 = asyncio.create_task(machine_loop())
        task2 = asyncio.create_task(pause_loop())

        value = await task1
        print(value)

        asyncio.run(main())

if __name__ == '__main__':
    unittest.main()

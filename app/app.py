import sys, getopt


class app():
    def __init__(self):
        self.file_name = ''
        self.number = 1
        self.story = ''

    def cli_arg(self, argv):
        try:
            opts, args = getopt.getopt(argv,"h:f:s:",["file=","number="])
        except getopt.GetoptError:
            print ('app.py -f <inputfile> -s <number1-3>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print ('app.py -f <inputfile> -s <number1-3>')
                sys.exit()
            elif opt in ("-f", "--file"):
                self.file_name = arg
            elif opt in ("-s", "--number"):
                self.number = arg

    def reader_call(self):
        from interdimensional_story_reader import interdimensional_story_reader
        self.story = interdimensional_story_reader(self.file_name, self.number)
        return self.story.display_text()

    async def interupter(self):
            async for command in stdin:
                if command == '^[' or '\n':
                    self.story.end()
                    sys.exit()


if __name__ == "__main__":
    app1 = app()
    app1.cli_arg(sys.argv[1:])

    app1.reader_call()

    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(interupter())

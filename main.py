class Input:
    # self.message
    pass

class EventHubsInput(Input):
    # set up connection from settings
    pass

class TelegramEventHubsInput(EventHubsInput):
    pass

class LoggingEventHubsInput(EventHubsInput):
    pass

class AirflowEventHubsInput(EventHubsInput):
    pass

class ConsoleInput(Input):
    def __init__(self):
        self.message = input("")





class Output:
    pass

class TelegramOutput(Output):
    pass

class ActionOutput(Output):
    pass

class AzureVMActionOutput(ActionOutput):
    pass





from dynaconf import settings

class Bot:
    def __init__(self):
        self.name = settings.BOT_NAME
        self.processors = []

    def add_processor(self, processor):
        self.processors.append(processor)


# The processor connects Input to Output
class Processor:
    pass

class DropToStdoutProcessor(Processor):
    def __init__(self, _input):
        print(_input.message)



bot = Bot()
print(bot.name)

bot.add_processor(DropToStdoutProcessor(ConsoleInput()))


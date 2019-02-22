class Input:
    # self.message
    pass

class EventHubsInput(Input):
    # set up connection from settings
    pass
    
class TelegramEventHubsInput(EventHubsInput):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return f"[TelegramEventHubsInput]: {self.msg}"

class LoggingEventHubsInput(EventHubsInput):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return f"[LoggingEventHubsInput]: {self.msg}"

class BotRequestInput(Input):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return f"[BotRequestInput]: {self.msg}"

class AzureRequestInput(Input):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return f"[AzureRequestInput]: {self.msg}"
    
class AirflowEventHubsInput(EventHubsInput):
    pass

class ConsoleInput(Input):
    def __init__(self):
        self.message = input("")
    
    def __str__(self):
        return f"[ConsoleInput]: {self.msg}"

    
class InputFactory:
    @staticmethod
    def determine(_input):
        if _input.startswith("1"):
            return TelegramEventHubsInput(_input)
        if _input.startswith("2"):
            return LoggingEventHubsInput(_input)
        if _input.startswith("A"): 
            return AzureRequestInput(_input)
        if _input.startswith("B"): 
            return BotRequestInput(_input)


class Output:
    pass

class LogOutput(Output):
    def run(self, string):
        print(f"<LogOutput> {string}")

class TelegramOutput(Output):
    pass

class ActionOutput(Output):
    pass



class BotListActionOutput(ActionOutput):
    def run(self, string):
        print(f"<BotListActionOutput> {string}: {len(bot.get_processors())}")

class BotWhoamiActionOutput(ActionOutput):
    def run(self, string):
        print(f"<BotWhoamiActionOutput> {string}: this is you")
        
class BotVersionActionOutput(ActionOutput):
    def run(self, string):
        print(f"<BotWhoamiActionOutput> {string}: {bot.version}")      
        
        
class BotCommandsActionOutput(ActionOutput):
    def run(self, string):
        print(f"<BotCommandsActionOutput> {string}:")

class AzureVMActionOutput(ActionOutput):
    def run(self, string):
        print(f"<AzureVMActionOutput> {string}")





from dynaconf import settings

class Bot:
    def __init__(self):
        self.version = "0.0.1"
        
        self.name = settings.BOT_NAME
        self.processors = []
    
    def add_processor(self, processor):
        self.processors.append(processor)
        
    def get_processors(self):
        return self.processors
    
    def process(self, _input):
        for processor in self.processors:
            processor.process(_input)
    
    def get_commands(self):
        return ["list", "version", "whoami"]

    
class Cloud:
    pass
    

# The processor connects Input to Output
class Processor:
    pass

class DropToStdoutProcessor():   
    def process(self, _input):
        print(f"(DropToStdoutProcessor) {str(_input)}")
        return LogOutput().run(str(_input))

class BotRequestProcessor():
    def process(self, _input):
        if type(_input) is BotRequestInput:
            print(f"(BotRequestProcessor) {str(_input)}")
            
            sinput = str(_input)
            if "list" in sinput:
                print(f"(BotRequestProcessor) further processing for list")
                BotListActionOutput().run(sinput)
            if "version" in sinput:
                print(f"(BotRequestProcessor) further processing for version")
                BotVersionActionOutput().run(sinput)
            if "whoami" in sinput:
                print(f"(BotRequestProcessor) further processing for whoami")
                BotWhoamiActionOutput().run(sinput)

class AzureRequestProcessor():
    def process(self, _input):
        if type(_input) is AzureRequestInput:
            print(f"(AzureRequestProcessor) {str(_input)}")
            
            if "list" in str(_input):
                print(f"(AzureRequestProcessor) further processing for list")
                AzureVMActionOutput().run(str(_input))
            
            # machines = azure.mgmt.compute.list("RESOURCEGROUPNAME", 
            # for machine in machines:
            # 

from azure.mgmt.compute.v2018_10_01.operations import VirtualMachinesOperations as vmo   



bot = Bot()
bot.add_processor(DropToStdoutProcessor())
bot.add_processor(AzureRequestProcessor())
bot.add_processor(BotRequestProcessor())

factory = InputFactory()
inputs = []
inputs.append(factory.determine("1 Hallo"))
inputs.append(factory.determine("A list machines"))
inputs.append(factory.determine("B list processors"))
inputs.append(factory.determine("B whoami"))
inputs.append(factory.determine("B version"))
#print(factory.determine(ConsoleInput().str()))

for x in inputs:
    bot.process(x)





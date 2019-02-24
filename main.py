from inputmethods.inputmethods import InputFactory




class Output:
    pass

class LogOutput(Output):
    def run(self, string):
        print(f"<LogOutput> {string}")

class TelegramOutput(Output):
    pass


class PostRoloTelegramOutput(TelegramOutput):
    def run(self, string):
        print(f"<PostRoloTelegramOutput> {string}: ROLOOOOOOOOOOOO")


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

    
class CloudManager:
    pass

class TelegramManager:
    pass    

class StateManager:
    def __init__(self):
        self.airflow_mutes = {}

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





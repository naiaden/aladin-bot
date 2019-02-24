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

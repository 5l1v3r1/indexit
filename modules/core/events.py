class Events:

    # Listeners subscribed
    subscribers = {}

    # Events constructor
    def __init__(self):
        pass

    # Listen for event
    @staticmethod
    def listen(self, name, handler):
        self.subscribers[name] = []
        self.subscribers[name].append(handler)

    # Emit an event
    @staticmethod
    def emit(self, name, payload):
        for event in self.subscribers[name]:
            event(payload)
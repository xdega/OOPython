# This is the parent "Command" class that all commands will inherit from
class Command:
    def __init__(self):
        # The shared property we are creating here is help text
        self.help = ""
    # We could define shared functions below

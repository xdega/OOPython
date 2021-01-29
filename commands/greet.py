from classes.command import Command


class Greet(Command):
    # We inherit the Command class above, then set the shared "help" property here
    Command.help = "Greet the user"

    # This is where the "meat and potatoes" of the command would live.
    def exec(input):
        print(f"Greetings, {input}")

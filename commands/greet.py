from classes.command import Command

class Greet(Command):
  Command.help = "Greet the user"
  
  def exec(input):
    print(f"Greetings, {input}")
  
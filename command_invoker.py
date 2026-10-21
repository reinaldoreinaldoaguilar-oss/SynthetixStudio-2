class CommandInvoker:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command_obj):
        self.commands[command_name] = command_obj

    def execute_command(self, user_input):
        parts = user_input.strip().split()
        if not parts:
            return ""
        
        command_name = parts[0]
        args = parts[1:]

        if command_name in self.commands:
            return self.commands[command_name].execute(*args)
        else:
            return f"Error: Comando '{command_name}' no reconocido."
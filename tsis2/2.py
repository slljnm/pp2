class Solution:
    def interpret(self, command):
        command = command.replace("(al)", "al")
        command = command.replace("()", "o")
        return command
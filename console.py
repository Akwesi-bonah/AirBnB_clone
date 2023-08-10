#!/usr/bin/python3
""" console for HBNB"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """exit"""
        return True

    def emptyline(self):
        """ Do nothing """
        pass
    
    def do_quit(self, line):
        """ Quit command line"""
        return True
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()

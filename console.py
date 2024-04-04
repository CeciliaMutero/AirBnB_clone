#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines hbnb command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing if line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

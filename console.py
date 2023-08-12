#!/usr/bin/env python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
from shlex import split
cls_dic = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }


class HBNBCommand(cmd.Cmd):
    """Defines HBnB command interpreter.

    """

    def __init__(self):
        """
        Initialize HBNBCommand
        Attributes:
        prompt (str): The command prompt.
        """
        self. prompt = "(hbnb) "
        super().__init__()

    @classmethod
    def pre_cmd(cls, arg):
        curly_braces = re.search(r"\{(.*?)\}", arg)
        brackets = re.search(r"\[(.*?)\]", arg)
        if curly_braces is None:
            if brackets is None:
                return [i.strip(",") for i in split(arg)]
            else:
                lexer = split(arg[:brackets.span()[0]])
                retl = [i.strip(",") for i in lexer]
                retl.append(brackets.group())
                return retl
        else:
            lexer = split(arg[:curly_braces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curly_braces.group())
            return retl

    def emptyline(self):
        """Do nothing """
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_cmd = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_cmd[1])
            if match is not None:
                command = [arg_cmd[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_cmd[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def do_create(self, arg):
        """
        Create a new class instance and print its id.
        """
        arg_cmd = self.pre_cmd(arg)
        if len(arg_cmd) == 0:
            print("** class name missing **")
        elif arg_cmd[0] not in cls_dic:
            print("** class doesn't exist **")
        else:
            print(eval(arg_cmd[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Display the string representation
        of a class instance of a given id."""

        arg_cmd = self.pre_cmd(arg)
        objdict = storage.all()
        if len(arg_cmd) == 0:
            print("** class name missing **")
        elif arg_cmd[0] not in cls_dic:
            print("** class doesn't exist **")
        elif len(arg_cmd) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_cmd[0], arg_cmd[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_cmd[0], arg_cmd[1])])

    def do_destroy(self, arg):
        """
        Delete a class instance of a given id."""
        arg_cmd = self.pre_cmd(arg)
        objdict = storage.all()
        if len(arg_cmd) == 0:
            print("** class name missing **")
        elif arg_cmd[0] not in cls_dic:
            print("** class doesn't exist **")
        elif len(arg_cmd) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_cmd[0], arg_cmd[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg_cmd[0], arg_cmd[1])]
            storage.save()

    def do_all(self, arg):
        """
        Display string representations
         of all instances of a given class.
        """
        arg_cmd = self.pre_cmd(arg)
        if len(arg_cmd) > 0 and arg_cmd[0] not in cls_dic:
            print("** class doesn't exist **")
        else:
            obj_len = []
            for obj in storage.all().values():
                if len(arg_cmd) > 0 and arg_cmd[0] == obj.__class__.__name__:
                    obj_len.append(obj.__str__())
                elif len(arg_cmd) == 0:
                    obj_len.append(obj.__str__())
            print(obj_len)

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class."""
        arg_cmd = self.pre_cmd(arg)
        count = 0
        for obj in storage.all().values():
            if arg_cmd[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating
        attribute (save the change into the JSON file)
        """
        arg_cmd = self.pre_cmd(arg)
        obj_dict = storage.all()

        if len(arg_cmd) == 0:
            print("** class name missing **")
            return False
        if arg_cmd[0] not in cls_dic:
            print("** class doesn't exist **")
            return False
        if len(arg_cmd) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_cmd[0], arg_cmd[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_cmd) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_cmd) == 3:
            try:
                type(eval(arg_cmd[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_cmd) == 4:
            obj = obj_dict["{}.{}".format(arg_cmd[0], arg_cmd[1])]
            if arg_cmd[2] in obj.__class__.__dict__.keys():
                val = type(obj.__class__.__dict__[arg_cmd[2]])
                obj.__dict__[arg_cmd[2]] = val(arg_cmd[3])
            else:
                obj.__dict__[arg_cmd[2]] = arg_cmd[3]
        elif type(eval(arg_cmd[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_cmd[0], arg_cmd[1])]
            for key, value in eval(arg_cmd[2]).items():
                hold = obj.__class__.__dict__
                if (key in hold.keys() and
                        type(hold[key]) in {str, int, float}):
                    val = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

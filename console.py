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

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self, obj):
        """Create new object instance"""

        if obj is None or len(obj) == 0:
            print("** class name missing **")
            return
        if obj in mod:
            my_ob = mod[obj]()
            my_ob.save()
            print(my_ob.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, obj):
        """Print string representation of object"""
        if obj is None or len(obj) == 0:
            print(" ** class name missing **")
            return

        ob_id = obj.split()
        if ob_id[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(ob_id) < 2:
            print("** instance id missing **")
            return
        a_o = models.storage.all()
        key = str(ob_id[0]) + "." + str(ob_id[1])
        if key in a_o:
            del a_o[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_destroy(self, obj):
        """ Deletes an instance on the object"""
        if obj is None or len(obj) == 0:
            print(" ** class name missing **")
            return

        ob_id = obj.split()
        if ob_id[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(ob_id) < 2:
            print("** instance id missing **")
            return
        a_o = models.storage.all()
        key = str(ob_id[0]) + "." + str(ob_id[1])
        if key in a_o:
            print(a_o[key])
        else:
            print("** no instance found **")

    def do_all(self, obj):
        """ Prints all """
        if obj is None or len(obj) == 0:
            print("** class name missing **")
            return
        objs = obj.split()

        if objs[0] == "BaseModel":
            print("** class doesn't exist **")
            return
        a_o = models.storage.all()
        lt = []
        for key, val in a_o.items():
            ob_n = val.__class__.__name__
            if ob_n == objs[0]:
                lt.append(str(val))
            print(lt)

    def do_update(self):
        pass
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()

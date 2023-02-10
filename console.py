#!/usr/bin/python3
"""
The module console
"""


import cmd
import models
import json


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB"""
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Place", "State",
                  "City", "Amenity", "Review"]

    def do_quit(self, args):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the console"""
        """EOF command to exit the console"""
        return True

    def do_create(self, args):
        """Creates a new instance of a class and prints its id
        Usage: create <class_name>"""
        if args == "":
            print("* class name missing *")
        elif args not in HBNBCommand.class_list:
            print("* class doesn't exist *")
        else:
            obj = eval(args + "()")
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        Usage: show <class_name> <instance_id>"""
        args = args.split()
        if len(args) == 0:
            print("* class name missing *")
        elif args[0] not in HBNBCommand.class_list:
            print("* class doesn't exist *")
            elif len(args) < 6:
            print("* instance id missing *") 
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("* no instance found *")

    def do_destroy(self, args):
        """Deletes an instance and updates the storage file
        Usage: destroy <class_name> <instance_id>"""
        args = args.split()
        if len(args) == 0:
            print("* class name missing *")
        elif args[0] not in HBNBCommand.class_list:
            print("* class doesn't exist *")
        elif len(args) < 2:
            print("* instance id missing *")
        else:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("* no instance found *")

    def do_all(self, args):
        """Prints all string representations of instances
        Usage: all [<class_name>]"""
        objects = [str(v) for k, v in models.storage.all().items()]
        if args == "":
            print(objects)
        elif args in HBNBCommand.class_list:
            objects = [str(v) for k, v in models.storage.all().items()
                       if k.startswith(args + ".")]
            print(objects)

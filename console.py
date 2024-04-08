#!/usr/bin/python3
"""Define the hbnb console"""
import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, arg):
        """command that creates new instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            new_instance = storage.classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """command that prints the str rep of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """command that destroys an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """command that prints all str rep of instance regardless of
        class name and id"""
        args = arg.split()
        instances = []
        if arg:
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                for instance in storage.all().values():
                    if type(instance).__name__ == arg:
                        instances.append(str(instance))
        else:
            for instance in models.storage.all().values():
                instances.append(str(instance))
        if instances:
            print(instances)

    def do_update(self, arg):
        """command that updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = " ".join(args[3:]).strip('"')

        key = "{}.{}".format(class_name, instance_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        instance = all_objs[key]
        if hasattr(instance, attribute_name):
            attribute_type = type(getattr(instance, attribute_name))
            try:
                casted_value = attribute_type(attribute_value)

            except ValueError:
                print("** invalid value type **")
                return
            if attribute_name in ["id", "created_at", "updated_at"]:
                print("** cannot update id, created_at, updated_at **")
                return
            setattr(instance, attribute_name, casted_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

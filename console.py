#!/usr/bin/python3
"""Console for the HBnB project."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parses command arguments."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        lexer = split(arg[:brackets.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(brackets.group())
        return retl
    lexer = split(arg[:curly_braces.span()[0]])
    retl = [i.strip(",") for i in lexer]
    retl.append(curly_braces.group())
    return retl


class HBNBCommand(cmd.Cmd):
    """
    Implements the command processor for the HolbertonBnB CLI

    Attributes:
        prompt (str): Command line prompt indicating readiness for user input
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
    }

    def emptyline(self):
        """Ignores empty lines."""
        pass

    def default(self, arg):
        """Handles invalid commands."""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict:
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()

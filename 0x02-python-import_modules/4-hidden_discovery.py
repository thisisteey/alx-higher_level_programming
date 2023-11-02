#!/usr/bin/python3
# python program that prints all names defined by a compiled module

if __name__ == "__main__":
    import hidden_4 as hidden_module
    defined_names = dir(hidden_module)
    for name in defined_names:
        if not name.startswith("__"):
            print(name)

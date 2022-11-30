from termcolor import colored


def cprint(msg, color="blue"):
    msg = colored(msg, color)
    print(f"{msg}")

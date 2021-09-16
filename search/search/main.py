#  add a module-level docstring to describe the purpose of this program
"""The program is for checking if a word exists in a certain file"""
from rich.console import Console

from pathlib import Path

import typer

cli = typer.Typer()
#  create a Typer object to support the command-line interface


def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    if file is not None:
        # the file is valid
        if file.is_file():
            return True
    # the file was either none or not valid
    return False


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    if answer:
        return "Yes"
    return "No"
    #  determine if the boolean value is True or False
    # if it is True, then return "Yes"
    # if it is False, then return "No"


def word_search(text: str, word: str) -> bool:
    """Determine whether or not a word is found in the text in case-sensitive fashion."""
    files = open(text, "r").read()
    for line in files:
        for _ in line.split():
            if _ == word:
                return True
    return False
    #  perform a case-sensitive search for the word in the provided text


@cli.command()
def word(
    word: str = typer.Option(None),
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
):
    """Process a file by searching for a specified word."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    file_fully_qualified = dir / file
    print(
        "\N{Grinning Face}",
        f"Searching through the file called {file_fully_qualified}!",
    )
    # We can get the input by using code above which connects the input as a file with my program
    if confirm_valid_file(file_fully_qualified) is False:
        print(f"{file_fully_qualified} was not a valid file")
    else:

        print(
            f"Was the word '{word}'found in the file {file_fully_qualified}? {human_readable_boolean(word_search(file_fully_qualified,word))}"
        )
    #  display a message to explain the file that will be input
    #  confirm the file is valid and so the program should search through it for the word
    # -->  read in the contents of the file
    # -->  search for the word in the contents of the file by calling function
    # -->  display a message about whether the word was or was not found
    #  since the file was not valid and thus you cannot install it display a message

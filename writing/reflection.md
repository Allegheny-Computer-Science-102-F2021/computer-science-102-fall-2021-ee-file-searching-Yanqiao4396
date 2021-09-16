# File Searching

# Yanqiao Chen

## Program Output

### What is the output from running the following commands?

: Use a fenced code block to provide the output for this command.

- `poetry run search --word ethical --dir input --file file.txt`
```
😀 Searching through the file called input/file.txt!
input/file.txt was not a valid file
```
: Use a fenced code block to provide the output for this command.

- `poetry run search --word ethical --dir input --file proactive.txt`
```

😀 Searching through the file called input/proactive.txt!
Was the word 'ethical'found in the file input/proactive.txt? Yes
```
## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### A function that confirms that a file containing data is valid
```
def word_search(text: str, word: str) -> bool:
    """Determine whether or not a word is found in the text in case-sensitive files."""
    fashion = open(text, "r").read().splitlines()
    for line in files:
        for _ in line.split():
            if _ == word:
                return True
    return False
```
First, the terminal checks if file exists, regardless of if file is "file". Only if the outcome is true, go to the next the step where the terminal checks whether file behaves as the type of file. If file can meet these two conditions, then return True, otherwise return False.

: Use a fenced code block to provide the requested source code
: Write at least one paragraph to explain the request source code

#### A function that produces a human readable response for a boolean value
```
def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    if answer:
        return "Yes"
    return "No"
```
: Use a fenced code block to provide the requested source code
: Write at least one paragraph to explain the request source code
Just use a if statement to achieve this requirement and return yes or no.
#### A function that performs a case-sensitive search for a word in a file
```
def word_search(text: str, word: str) -> bool:
    """Determine whether or not a word is found in the text in case-sensitive fashion."""
    files = open(text, "r").read()
    for line in files:
        for _ in line.split():
            if _ == word:
                return True
    return False
```
I open this file by use open("r") and read it. At the same time, I splite the file so that each line can be a seperate block. Then what we should do is split lines into smaller blocks and use == operator to check if there is a value equal to the string we want. If not return False, otherwise return True.
: Use a fenced code block to provide the requested source code
: Write at least one paragraph to explain the request source code

### What is the purpose of the `pyproject.toml` file?
pyproject.toml is the specified file format of which contains the build system requirements of Python projects.
: Provide a one-paragraph response that answers this question in your own words.
: You may leverage your answer from the S.O.S Checkpoint assignment!

### What is the purpose of the `poetry.lock` file?
cIf you have never run the command before and there is also no poetry.lock file present, Poetry simply resolves all dependencies listed in your pyproject.toml file and downloads the latest version of their files.
When Poetry has finished installing, it writes all of the packages and the exact versions of them that it downloaded to the poetry.lock file, locking the project to those specific versions. You should commit the poetry.lock file to your project repo so that all people working on the project are locked to the same versions of dependencies (more below).
: Provide a one-paragraph response that answers this question in your own words.
: You may leverage your answer from the S.O.S Checkpoint assignment!

### What are three different ways in which you can run the `search` program?
Sorry the only way I know is to use poetry run. I know docker may make sense as well, but I don't know how to do with it.

: Describe the first way for running the program, giving a command and a paragraph

- : provide a command

: Describe the second way for running the program, giving a command and a paragraph

- : provide a command

: Describe the third way for running the program, giving a command and a paragraph

- : provide a command

### What was the greatest challenge that you faced when completing this assignment?
The greatest challenge must be to find a good approach to read the file and split it.

: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?
I want to improve my understanding of docker container.
: Provide a one-paragraph response that answers this question in your own words.

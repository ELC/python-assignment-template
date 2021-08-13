# Autograding Python Assignments
A template repository to create assignments in Github Classroom

This README is all the documentation you need to get started. Jump to the
section of interest:

- [Structure of the template](#structure-of-the-template)
- [Methodology](#methodology)
- [Github Classroom Configuration](#github-classroom-configuration)
- [Code Style](#code-style)
- [Docstrings](#docstrings)


## Structure of the template

The template provides examples of different approaches to Github Classroom
Assignments:

- Doctests
- Assertion Tests
- Doctests and Assertion Tests
- Hidden Tests
- Property Testing

Each has its features:

**Doctests** are tests that are part of the docstring (i.e. the string one line
below the function/class declaration). The purpose is twofold, on one hand,
they show the developer exactly what is the expected behavior, on the other
hand, they also encourage good and updated documentation and provide useful
examples to the consumer of the functions/classes. As a drawback, the developer
could be tempted to "just pass the test" and thus not providing an
implementation that fulfills the requirement. The **Exercise 1** is an example.

**Assertion Tests** are tests that validate a given expression is **True**,
they usually are of the form "expected vs actual". This idea is similar to the
one expressed in the doctest, there are some differences though. **Assertion
Tests** are not part of the function/class *per se* and hence they require
external code statements. They are not reflected in the documentation of the
function/class and could lead the developer to the same "just pass the test"
temptation. That being said, using them provides more flexible workflows since
mocking components is usually too verbose for doctests. The **Exercise 2** is
an example.

**Doctests and Assertion Tests** is the combination of the two above-mentioned
tests. The **Exercise 3** is an example.

**Hidden Tests** refers to the separation of developer code and test code
rather than a test methodology. These tests are in a separate folder than the
code they are testing and are usually **assertion tests**. The main advantage
is that, although the developer has still access to them, it is much more
complicated to modify them or alter them by accident. These tests are well
suited to mock complex steps and processes and therefore allow not only unit
tests but also integration tests. The **Exercise 4** is an example.

**Property Testing** is a methodology for testing functionality where instead
of using examples of "expected vs actual", properties the code should have been
tested. This is trivial for math-related code since properties arise naturally
in the context of math. However, for enterprise software with several layers of
abstractions, this is not transparent. For more information and examples there
is the [talk by Zac
Hatfield-Dodds](https://www.youtube.com/watch?v=uN6JjpzVsAo) from PyCon 2021.
The **Exercise 5** is an example of how to use them with a toy example, here,
the Hypothesis test framework is used (i.e it should also be installed in the
setup command).

## Methodology

There are multiple ways to implement assignments, below are some ideas, divided
by the level of experience

### Begginer

- **Complete the code**: A function/class **with** signature and docstring is
  given but without a body, the student must write the body so that the tests
  pass.

- **Find the bug**: A function/class **with** signature, docstring and **body**
  is given but the tests are currently failing, the student must find the cause
  and fix it so that tests pass.

### Intermediate

- **Refactor**: A function/class that is working and whose tests are passing
  are given but, a new style decision is posed and the student should refactor
  the code to meet that new requirement and keep the code working, passing the
  test. For instance: one style decision might be "No loops allow" so it would
  be expected that recursion is used instead without explicitly saying that to
  the student.

- **Add Functionality**: A function/class that is working and whose tests are
  passing is given but, a new requirement is provided, the student then needs
  to add that functionality for which tests are given and should make sure old
  test keep passing.

- **Add Test**: A function/class with the necessary docstring is given that is
  not properly working but there are no tests to show it. The student should
  write tests, identify the problem and fix it so that tests pass.

### Advanced

- **Architecture Design**: Only a text description of a system is given and the
  student should write all the code and tests to fulfill the requirements.

## Github Classroom Configuration

To create assignments follow these steps:

1. Fork this repo and modify it to add the necessary exercise. Including
   **modifying** this README page
1. Make the forked repo a template repo.
1. Create an assignment once logged in to Github Classroom.
1. Select the forked repo.
1. Add a Test of type "Run Python". One globally or one for each exercise (see
   below).
1. Share the link with the students.

### Test Details

To configure the "Run Python" test

To set up a Github Classroom assignment, 5 fields should be specified:

- **Title**: Choose a descriptive title for your exercise.
- **Setup Command**: Install all necessary dependencies, if using the standard
  library only, running  `sudo -H pip3 install pytest` should suffice. Pip's
  install path is not included in the PATH var by default, so without
  installing via `sudo -H`, pytest would be inaccessible.
- **Run Command**: Specify a test command to run either one particular file or
  a whole directory of files. In the most basic configuration `python -m pytest
  -vvv tests/exercise1_test.py` will suffice. (Explanation below)
- **Timeout**: This is the execution timeout for the tests.
- **Points**: How many points are this particular exercise worth.


#### Run Command Details

The command might seem arbitrary but each part has its purpose


```bash
python -m pytest -vvv tests/exercise1_test.py
```

The `python -m` ensures the files are executed as modules, this is necessary to
properly handle imports inside tests; `pytest -vvv` defines the command to run
the tests, pytest is the name of the testing library, and the flag `-vvv` means
that the output should include as many details as possible; then comes the
specific file `tests/exercise1_test.py`, in this case, it is for a single file
but if one-test assignments are preferred, it could have been replaced with
`tests`, meaning that the whole directory will be scanned for tests.

## Code Style

In addition to the tests described in the previous section, this repo includes
a pre-commit test that has no points assigned but that ensures the same style
(Flake8) is applied to all files in the repo. This serves as a static style
check for the students' code. However, its importance should be assessed by the
teacher in the PR.

If this style check should be graded, then add a test with:

- **Setup Command**: `sudo -H pip3 install flake8`
- **Run Command**: `flake8`

## Docstrings

Having your code well documented is crucial in any production project. The
style guide for Python is defined in the [PEP
257](https://www.python.org/dev/peps/pep-0257/) but, some industry conventions
are shown below. It is **recommended** that whenever applicable, one of these
conventions is used in the exercise so that the student gets familiar with
docstrings.

Since docstring writing could be a repetitive task, it is **recommended** to
use some extension to automate the process. In VS Code the [Autodocstring
Extension](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
serves this purpose.

**Note**: The examples below do not deserve a docstring because the
functionality is something trivial, that being said, it is useful to show a
common scenario with types, return types, and raising exceptions. In production
code, such functions should not have docstrings.

### Sphinx

The full guide can be found in the [official
documentation](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)

```python
def function(key: str, dictionary: Dict[str, str]) -> str:
    """This is a dummy function that returns the value of a dictionary given a
    key.

    :param key: The key to look for in the dictionary
    :type key: str
    :param dictionary: The dictionary where the key will be looked for
    :type dictionary: Dict[str, str]
    :return: The value of the dictionary at the given key
    :rtype: str
    :raises KeyError: If key is not in the dictionary.
    """
    return dictionary[key]
```

### Google
The full guide can be found in the [official
documentation](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).
Moreover, [comprehensive
example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
is shown in the Napoleon Sphinx Plugin
```python
def function(key: str, dictionary: Dict[str, str]) -> str:
    """This is a dummy function that returns the value of a dictionary given a
    key.

    Args:
        key (str): The key to look for in the dictionary.
        dictionary (Dict[str, str]): The dictionary where the key will be
            looked for.

    Returns:
        str: The value of the dictionary at the given key.

    Raises:
        KeyError: If key is not in the dictionary.
    """
    return dictionary[key]
```

### Numpydoc

The full guide can be found in the [official
documentation](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard).
Moreover, [comprehensive
example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
is shown in the Napoleon Sphinx Plugin

```python
def function(key: str, dictionary: Dict[str, str]) -> str:
    """This is a dummy function that returns the value of a dictionary given a
    key.

    Parameters
    ----------
    key : str
        The key to look for in the dictionary.
    dictionary : Dict[str, str]
        The dictionary where the key will be looked for.

    Returns
    -------
    str
        The value of the dictionary at the given key.

    Raises
    ------
    KeyError
        If key is not in the dictionary.
    """
    return dictionary[key]
```

# KWIC - Keyword in Context

This project implements KWIC algorithm using **Pipeline** programming style. As a refernce we used the book _Exercises in Programming Style_ by Cristina Lopes.

## Objective

The goal of this program is to take a list of titles from the 
´´´input.txt``` file and generate an ordered list of keywoards in context

- Read ```input.txt```
- Remove stop words from the titles
- Generate circular shifts
- Sort the output alphabetically
- Print the results

## Project Structure

KWIC/
```
↳ .gitignore        # ignore files and folder when committing
↳ kwic.py           # main implementations of the project
↳ README.md         # Project documentation
↳ input.txt         # input titles
↳ stop_words.txt    # list of stop words
↳ test_KWIC.py      # unit test using pytest
```
## How to run

1. Requirements: 
    - Python 3.10+
    - pytest

2. Installing pytest:

    ```pip install pytest```

3. Run kwic.py

    ```python kwic.py```

## Running the test

    pytest test_KWIC.py


## Input and Output

### Input

**input.txt**
    ```The quick brown fox
    A brown cat sat
    The cat is brown```

**stop_words.txt**
    ```The
    is
    a```


### Output

```
brown cat sat a             from A brown cat sat
brown fox the quick         from The quick brown fox
brown the cat is            from The cat is brown
cat is brown the            from The cat is brown
cat sat a brown             from A brown cat sat
fox the quick brown         from The quick brown fox
quick brown fox the         from The quick brown fox
sat a brown cat             from A brown cat sat
the cat is brown            from The cat is brown
the quick brown fox         from The quick brown fox
```

## Authors

- Gabriel Bismarck - 17/0103323

## Video

- [](#)

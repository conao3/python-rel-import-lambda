# rel-import-lambda

A reference implementation demonstrating how to properly use relative imports in Python AWS Lambda functions.

## Overview

When deploying Python code to AWS Lambda, managing imports can be tricky, especially when using relative imports within your function code. This project provides a working example of a Lambda function structure that correctly handles relative imports.

## Project Structure

```
app/
  function/
    sample_function/
      index.py      # Lambda handler entry point
      util.py       # Utility module with shared functions
test/
  app/
    function/
      sample_function/
        test_main.py
```

## Key Concept

The project demonstrates using relative imports (`from . import util`) instead of absolute imports within Lambda function code. This approach:

- Keeps function code modular and organized
- Avoids import path issues when Lambda executes your code
- Makes local development and testing more straightforward

## Requirements

- Python 3.8 or higher
- Poetry (for dependency management)

## Getting Started

### Installation

```bash
poetry install
```

### Running Tests

```bash
poetry run pytest
```

## Usage

The sample function shows the pattern:

```python
# index.py
from . import util

def main():
    return util.version()
```

```python
# util.py
def version():
    return "0.0.1"
```

## License

This project is provided as a reference implementation.

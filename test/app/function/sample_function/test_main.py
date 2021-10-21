import sys

print(sys.path)

from app.function.sample_function.index import main

def test_main():
    assert main() == "0.0.1"

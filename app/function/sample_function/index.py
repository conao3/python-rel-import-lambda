import importlib

util = type("object", (), {})
util = importlib.import_module(("." if __package__ else "") + "util", __package__)

# from . import util
# import util

def main():
    print(util.version())
    return util.version()

if __name__ == '__main__':
    main()

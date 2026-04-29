from typing_extensions import TypedDict
import sys

print(f"Python version: {sys.version}")
try:
    from typing_extensions import __version__ as te_version
    print(f"typing-extensions version: {te_version}")
except ImportError:
    print("typing-extensions version: unknown")

try:
    class T(TypedDict, extra_items=int):
        x: int
    print("TypedDict with extra_items supported")
except TypeError as e:
    print(f"TypedDict with extra_items NOT supported: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

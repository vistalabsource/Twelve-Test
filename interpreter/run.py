import sys
import os
from eval.eval import *
from pyparsing import *

EXT = ".12"

def run(code: str):
    try:
        program.parseString(code)
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: twelve <filename>{EXT}")
        sys.exit(1)

filepath = sys.argv[1] 

# 拡張子チェック    
if not filepath.endswith(EXT):
    print(f"Error: File must have the extension '{EXT}'")
    sys.exit(1)

if not os.path.isfile(filepath):
    print("Error; File not found")
    sys.exit(1)

with open(filepath, 'r') as file:
    code = file.read()

run(code)
        
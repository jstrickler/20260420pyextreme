"""
Module documentation...
"""

import sys



# this is the function providing the 'actual' script
# you can also import this module normally and use this function 

def sample_function(*args):
    """
    Sample function documentation...
    """
    print("sample weasels function")


# this is a wrapper that is used to create the callable cli version of the function
def _sample_function_cli():  # name can be anything
    # access sys.argv as needed (copied from script's args)
    args = sys.argv[1:]
    print(f"Args to script: {args}")  # diagnostic -- delete
    sample_function(*args)  # call the 'real' function
    # note: change '*args' to actual params needed

#  in pyproject.toml, add this section
#
#  [scripts]
#  script_name = 'weasels:_sample_function_cli'
#
# then you can run my_script_name from the command line



if __name__ == "__main__":
    # the code in this block (and all the code above) will be run when
    # either
    #    python weasels.py
    # or 
    #    python -m weasels
    # is executed, but NOT when imported like
    #    import weasels
    print(f"Hello from {__file__}")

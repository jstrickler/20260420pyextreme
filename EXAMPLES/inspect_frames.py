import inspect

def eggs():
    print("EGGS")
    # get frame (function call stack) info
    current_frame = inspect.currentframe()
    print("Current frame:", inspect.getframeinfo(current_frame))

eggs()
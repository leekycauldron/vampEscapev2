class Logger():
    def __init__(self):
        pass
    # V is the verbose argument, if passed it will print the log.
    def log(self, msg, v):
        if v is not None: print(msg)

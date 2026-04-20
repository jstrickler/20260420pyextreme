import logging

class Foo:
    def __init__(self, *, enable_logging=True) -> None:
        self.logger = logging.getLogger("root.foo")
        if not enable_logging:
            self.logger.disabled = True  # log messages will not be written

    def doit(self):
        self.logger.warning("log message from Foo")

class Bar:
    def __init__(self, *, enable_logging=True) -> None:
        self.logger = logging.getLogger("root.bar")
        if not enable_logging:
            self.logger.disabled = True # log messages will not be written

    def doit(self):
        self.logger.warning("log message from Bar")

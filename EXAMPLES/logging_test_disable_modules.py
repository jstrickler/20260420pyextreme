import logging
from logging_disable_modules import Foo, Bar

logging.basicConfig(
    format="%(levelname)s:%(name)s:%(message)s",
    filename="../LOGS/disabled.log",
)

logger = logging.getLogger()  # get root logger

logger.warning("in the main script")

foo = Foo()
bar = Bar(enable_logging=False)

foo.doit() # will write to log
bar.doit() # will not write to log

logger.warning("end of script")

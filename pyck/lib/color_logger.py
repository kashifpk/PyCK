import sys
import logging


class ColorLogger(logging.getLoggerClass()):
    """
    Logger class that by default outputs to stderr
    """

    out = sys.stdout
    err = sys.stderr

    INFO = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

    def __init__(self, name, output_file=sys.stdout, error_file=sys.stderr):
        self.out = output_file
        self.err = error_file

    def log(self, msg):
        self.out.write(msg + '\n')

    def warn(self, msg):
        self.err.write(self.WARNING + msg + self.ENDC + '\n')

    def error(self, msg):
        self.err.write(self.ERROR + msg + self.ENDC + '\n')

    def info(self, msg):
        self.out.write(self.INFO + msg + self.ENDC + '\n')


class ConsoleColorHandler(logging.StreamHandler):
    """
    Log Handler for console that outputs colored log messages according to their severity
    """

    _log_colors = {
        logging.CRITICAL: '\033[91m',  # red
        logging.ERROR: '\033[91m',     # red
        logging.WARNING: '\033[93m',   # yellow
        logging.INFO: '\033[92m',      # green
        logging.DEBUG: '\033[94m',     # blue
        logging.NOTSET: '\033[0m',     # white
    }

    terminator = '\033[0m\n'

    def __init__(self, stream=None):
        super(ConsoleColorHandler, self).__init__(stream)

    def emit(self, record):

        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(self._log_colors[record.levelno])
            stream.write(msg)
            stream.write(self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

# ============================================================================
# Simplified version of logging module
# ============================================================================

class Logger(object):
    def __init__(self, log_level=WARNING):
        self._log = print
        self.level = log_level

    def setDevice(self, method):
        self._log = method

    def setLevel(self, log_level=WARNING):
        self.level = log_level

    def debug(self, *kw):
        if self.level <= DEBUG:
            msg = " ".join(map(str, kw))
            self._log(msg)

    def info(self, *kw):
        if self.level <= INFO:
            msg = " ".join(map(str, kw))
            self._log(msg)

    def warning(self, *kw):
        if self.level <= WARNING:
            msg = " ".join(map(str, kw))
            self._log(msg)

    def error(self, *kw):
        if self.level <= ERROR:
            msg = " ".join(map(str, kw))
            self._log(msg)

    def critical(self, *kw):
        if self.level <= CRITICAL:
            msg = " ".join(map(str, kw))
            self._log(msg)

    def always(self, *kw):
        msg = " ".join(map(str, kw))
        self._log(msg)


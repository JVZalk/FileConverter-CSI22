import logging

class ConditionalLogger:
    def __init__(self, enabled=True, name="activity_logger", log_file="activity.log"):
        self.enabled = enabled
        self.logger = None
        if self.enabled:
            self.logger = logging.getLogger(name)
            if not self.logger.hasHandlers():
                handler = logging.FileHandler(log_file, mode='a')
                formatter = logging.Formatter(
                    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                )
                handler.setFormatter(formatter)
                self.logger.addHandler(handler)
                self.logger.setLevel(logging.INFO)

    def set_enabled(self, enabled: bool):
        if enabled and not self.enabled:
            # Re-initialize logger if enabling
            self.__init__(enabled=True)
        self.enabled = enabled

    def info(self, msg):
        if self.enabled and self.logger:
            self.logger.info(msg)

    def error(self, msg):
        if self.enabled and self.logger:
            self.logger.error(msg)

    def warning(self, msg):
        if self.enabled and self.logger:
            self.logger.warning(msg)

logger = ConditionalLogger(enabled=False)

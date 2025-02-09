"""
This module provides a Logger class for setting up and managing loggers.
"""

import logging
import os
from pathlib import Path


class Logger:
    def __init__(self, name, log_file, level=logging.INFO):
        """
        Initializes the Logger class with a name, log file, and logging level.

        Parameters:
        name (str): The name of the logger.
        log_file (str): The name of the log file.
        level (int): The logging level (default is logging.INFO).
        """

        self.name = name
        self.log_file = os.path.join("logs", log_file)
        self.level = level
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """
        Sets up and returns a logger with the specified configuration.

        Returns:
        logger (logging.Logger): The configured logger instance.
        """

        if not os.path.exists(Path("../logs")):
            os.makedirs(Path("../logs"))

        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        handler = logging.FileHandler(self.log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        logger.addHandler(handler)

        return logger

    def get_logger(self):
        return self.logger

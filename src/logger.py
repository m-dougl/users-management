import logging
import os
from pathlib import Path 

class Logger:
    def __init__(self, name, log_file, level=logging.INFO):
        self.name = name
        self.log_file = os.path.join('logs', log_file)
        self.level = level
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Function to setup a logger"""
        if not os.path.exists(Path('../logs')):
            os.makedirs(Path('../logs'))
        
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        
        handler = logging.FileHandler(self.log_file)
        handler.setFormatter(formatter)
        
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        logger.addHandler(handler)
        
        return logger

    def get_logger(self):
        return self.logger

# Example usage:
# logger_instance = Logger('my_logger', 'my_log_file.log')
# logger = logger_instance.get_logger()
# logger.info('This is an info message')
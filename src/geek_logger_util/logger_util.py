import logging
import json
from datetime import datetime

class CustomJsonFormatter(logging.Formatter):
    def __init__(self, service_name):
        super().__init__()
        self.service_name = service_name

    def format(self, record):
        log_object = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "message": record.getMessage(),
            "service": self.service_name,
        }

        # Add custom fields
        #log_object["custom_field"] = getattr(record, 'custom_field', 'default_custom_value')

        # Include exception info if present
        if record.exc_info:
            log_object["exception"] = self.formatException(record.exc_info)

        # Include any extra attributes from the record
        for key, value in record.__dict__.items():
            if key not in ["args", "asctime", "created", "exc_info", "exc_text", "filename",
                           "funcName", "levelname", "levelno", "lineno", "module",
                           "msecs", "message", "msg", "name", "pathname", "process",
                           "processName", "relativeCreated", "thread", "threadName"]:
                log_object[key] = value

        return json.dumps(log_object)

class LoggerUtil:
    @staticmethod
    def setup_logger(name, service_name, level=logging.INFO, custom_field=None):
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CustomJsonFormatter(service_name=service_name))
        logger.addHandler(console_handler)

        # File handler
        file_handler = logging.FileHandler(f"{service_name}.log")
        file_handler.setFormatter(CustomJsonFormatter(service_name=service_name))
        logger.addHandler(file_handler)

        # Add custom field as a filter
        class CustomFieldFilter(logging.Filter):
            def filter(self, record):
                record.custom_field = custom_field
                return True

        logger.addFilter(CustomFieldFilter())

        return logger

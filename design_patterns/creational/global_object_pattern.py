class GlobalLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GlobalLogger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.log_level = "INFO"

    def set_log_level(self, level):
        set.log_level = level

    def log(self, message):
        print(f"[{self.log_level}] - {message}")

from logging import FileHandler, getLogger, StreamHandler, INFO

class Setting:
    def __init__(self):
        pass
    
    def set_logger(self, logger_name=None, logger_level=INFO):
        if not logger_name:
            logger_name = "tmp_logger.txt"
        # Set Logger
        logger = getLogger(__name__)
        handler = FileHandler(filename=logger_name)
        logger.setLevel(logger_level)
        logger.addHandler(handler)
        logger.propagate = False
        logger.info("Executing {}".format(__name__))
        return logger
    
if __name__ == "__main__":
    setting = Setting()
    tmp_log = setting.set_logger(logger_name="exec_setting.txt")
    tmp_log.info("Finished executing setting.py")
    print(tmp_log.handlers[0].baseFilename)
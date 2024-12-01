import logging


class BaseClass:


    @staticmethod
    def get_Log_Details():
        logger = logging.getLogger(__name__)
        logFile = logging.FileHandler('UI_Assessment_Log_File.log')
        logFormatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        logFile.setFormatter(logFormatter)
        logger.addHandler(logFile)
        logger.setLevel(logging.INFO)
        return logger
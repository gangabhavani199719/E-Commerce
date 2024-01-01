import logging
import inspect

class LogGen:
    @staticmethod

    def loggen(logLevel=logging.DEBUG):
        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # create console handler or file handler and set the log level
        fh = logging.FileHandler("C:\\python-selenium\\E-commerce\\Logs\\automation.log",
                                 mode='a')  # by default its append mode or u can update as override mode as 'w'
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # add formatter to conole or file handler
        fh.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(fh)
        return logger

    #     def loggen():
    #
    #         logging.basicConfig(filename="C:\\python-selenium\\E-commerce\\Logs\\automation.log", format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    #         logger=logging.getLogger()
    #         logger.setLevel(logging.INFO)
    #         return logger











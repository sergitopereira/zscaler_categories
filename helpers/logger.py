import logging


def get_logger(logger_name, log_file):
    log = logging.getLogger(logger_name)
    log.setLevel(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(f'{log_file}.log')
    fh.setLevel(level=logging.DEBUG)
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setLevel(level=logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(fh)
    log.addHandler(ch)
    return log

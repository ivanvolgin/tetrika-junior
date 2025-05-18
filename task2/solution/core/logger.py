import logging


def setup_logger(debug=False):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(module)s:%(lineno)d | %(message)s",
    )


def get_logger(name=None):
    return logging.getLogger(name)

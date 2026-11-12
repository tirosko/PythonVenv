import logging
logger = logging.getLogger(__name__)
logger.propagate = False
logger.setLevel(logging.DEBUG)
logger.info('hello from helper')

"""Example script to show the capabilities of the logging module."""
import logging

# taken from Logging HOWTO
# create logger
logger = logging.getLogger('example')

logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s -'
                              ' %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

logger.debug('test')
logger.info('test')

# DEBUG < INFO < WARNING < ERROR < CRITICAL

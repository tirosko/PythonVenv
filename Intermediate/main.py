# https://docs.python.org/3/library/logging.html
# import helper
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message) s',
#                     datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
#
# Vyššie uvedený kód bude zapisovať správy na rôznych úrovniach závažnosti.
# Modul logging je súčasťou štandardnej knižnice Pythonu a poskytuje flexibilný rámec na zapisovanie logovacích správ z Python programov.
# Modul logging sa používa na sledovanie udalostí, ktoré sa dejú počas behu softvéru. Môže sa použiť na zapisovanie správ do rôznych cieľov, ako je konzola, súbory alebo vzdialené servery.
# Modul logging je výkonný nástroj na ladenie a monitorovanie Python aplikácií.
# Umožňuje zapisovať správy na rôznych úrovniach závažnosti, ako sú debug, info, warning, error a critical.
# Modul logging môžete tiež nakonfigurovať na zapisovanie správ do rôznych cieľov, ako je konzola, súbory alebo vzdialené servery.

# Vlastnosti modulu logging

# import logging

# logging.config.fileConfig('logging.conf')

# logger = logging.getLogger(__name__)

# # create handler
# stream_h = logging. StreamHandler()
# file_h = logging. FileHandler('file.log')

# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging. Formatter('%(name)s -%(levelname)s -%(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning')
# logger.error('this is an error')
# ---------------------------------------------------------
# import logging
# import logging.config

# logging.config.fileConfig('logging.conf')

# logger = logging.getLogger('simpleExample')
# logger.debug('This is a debug message')
# ----------------------------------------------------------
# import logging
# import traceback

# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     print(e)
#     logging.error("The error is %s", traceback.format_exc())
# -----------------------------------------------------------
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger. setLevel(logging. INFO)

# roll over after 2KB, and keep backup logs app. log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger. addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world! ')

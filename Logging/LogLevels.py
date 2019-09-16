import logging

logging.basicConfig(filename="Features.log",
                    format="%(asctime)s:%(levelname)s:%(funcName)s:%(message)s:%(lineno)s")

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
a=10
b=20

print("The sum of two number is {}".format(a+b))
logger.debug("The sum of two number is {}".format(a+b))
logger.info("The sum of two number is {}".format(a+b))
logger.warning("The sum of two number is {}".format(a+b))
logger.error("The sum of two number is {}".format(a+b))
logger.critical("The sum of two number is {}".format(a+b))

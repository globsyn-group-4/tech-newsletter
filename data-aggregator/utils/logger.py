import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s || %(levelname)s || %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger('data-aggregator')
logger.info("Established logger config....")


import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

handler = logging.StreamHandler(sys.stdout)
handler.setLevel('DEBUG')

formatter = logging.Formatter('[%(asctime)s][%(levelname)s] - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
